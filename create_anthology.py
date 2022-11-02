#!/usr/bin/python

import os
import argparse
import glob #getting all files with pattern matching
import datetime

YEAR   = "2022"
AUTHOR = "Muzamil Yahia"
INSTITUTE = "University of Hawaii"

def copy_from_file_to_file(start, end, input_file):
    """Copy from input_file to output_file beginning from line containing start, and ending with line containing end"""
    output = ""
    with open(input_file) as infile:
        copy = False
        for line in infile:
            if line.strip() == start:
                copy = True
                continue
            elif line.strip() == end:
                copy = False
                continue
            elif copy:
                if line.strip() == start or line.strip() == end :
                    line = ""
                output += line
    return output 

def main(args):
    """ main function """
    name = "{}-Research-Diary".format(args.year)
    file_name  = name + ".tex"
    pwd = os.path.dirname(__file__)
    year_folder = pwd + "/{}/".format(args.year)
    images_folder = year_folder + "images/" 

    print(year_folder)
    arguments = {"file_name":file_name,"author":args.author, "year":args.year, "institute":args.institute,"pwd":pwd,"year_folder":year_folder, "images_folder":images_folder}
    
    # check if the directory with year args.year exists
    if not os.path.exists(pwd):
        print("Error: folder {} does not exist!".format(pwd))
        return 1
    if not os.path.exists(year_folder):
        print("Error: folder {} does not exist!".format(year_folder))
        return 1
    if not os.path.exists(images_folder):
        print("Error: folder {} does not exist!".format(images_folder))
        return 1
    # creating preamble for the main tex file 
    preamble = """
% 
% Research Diary for {author} ({institute}), {year}
%
%
\documentclass[letterpaper,11pt]{{article}}
\\newcommand{{\\userName}}{{{author}}}
\\newcommand{{\\institution}}{{{institute}}}
\\usepackage{{{pwd}/research_diary}}

\\title{{Research Diary - {year}}}
\\author{{{author}}}

\\chead{{\\textsc{{Research Diary}}}}
\\lhead{{\\textsc{{\\userName}}}}
\\rfoot{{\\textsc{{\\thepage}}}}
\\cfoot{{\\textit{{Last modified: \\today}}}}
\\lfoot{{\\textsc{{\\institution}}}}
\\graphicspath{{{{{year}/}}{{{images_folder}}}}}

\\begin{{document}}
\\begin{{center}} \\begin{{LARGE}}
\\textbf{{Research Diary}} \\\\[3mm]
\\textbf{{{year}}} \\\\[2cm]
\\end{{LARGE}} \\begin{{large}}
{author} \\end{{large}} \\\\
{institute} \\\\[7in]
\\textsc{{Compiled \\today}}
\\end{{center}}
\\thispagestyle{{empty}}
\\newpage

""".format(**arguments)

    formatter = '%Y-%m-%d'
    month_int_to_month_str = {1:"January", 2:"February", 3:"March", 4:"April",5:"May", 6:"June", 7:"July", 8:"August", 9:"September",10:"October",11:"November",12:"December"}
    start = "\\begin{document}"
    end = "\\end{document}"

    
    file_path = pwd + "/" + file_name # main tex file
    print("Writing to main file: ", file_path)
    out_file = open(file_path, 'w')
    out_file.write(preamble)
    #Copy the content of tex files of year folder into main file in decreasing order
    for tex_file in sorted(glob.glob(year_folder+"/*.tex"), reverse=True):
        file = os.path.basename(tex_file) #extract the base name
        date_str = file[:-4] # extract the date
        date_title = date_str
        date_title = datetime.datetime.strptime(date_str, formatter).date()
        sub_content = "%%% --- {} --- %%%\n \n".format(file)
        sub_content += "\\rhead{{{} $\mid$ {} $\mid$ {} }}\n \n".format(date_title.year, month_int_to_month_str[date_title.month], "{0:0=2d}".format(date_title.day))

        sub_content += "\\newpage\n \n"
        sub_content += copy_from_file_to_file(start, end, tex_file) + "\n"
        out_file.write(sub_content)
    last_line = "\\end{document}"
    out_file.write(last_line)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-y", 
        "--year",
        type=str,
        default=YEAR,
        help = "research diary year"
        )
    parser.add_argument(
        "-au", 
        "--author", 
        type=str,
        default=AUTHOR,
        help = "author"
        )
    parser.add_argument(
        "-ins", 
        "--institute", 
        type=str,
        default=INSTITUTE,
        help = "name of the institute"
        )
    args = parser.parse_args()
    #fancy way to print arguments
    arguments = {'year':args.year, 'institute':args.institute, 'author':args.author}
    print("Creating research diary for year {year}, author {author}, and institute {institute}".format(**arguments))
    main(args)