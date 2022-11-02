import os
import argparse
import datetime


today = datetime.date.today() 
YEAR = "{0:0=2d}".format(today.year)
MONTH = "{0:0=2d}".format(today.month)
DAY = "{0:0=2d}".format(today.day)
AUTHOR = "Muzamil Yahia"
INSTITUTE = "University of Hawaii"


def main(args):
    print("Today is {} / {} / {}".format(args.year, args.month, args.day))
    #check if the dir of year exists
    pwd = os.path.dirname(__file__)
    year_folder = pwd + "/" + args.year + "/"
    if not os.path.exists(year_folder):
        print("Error: folder {} does not exist!".format(pwd))
        print("Creating a new folder {}".format(args.year))
        os.mkdir(year_folder)    

    print("Adding new entry to folder: {}".format(args.year))
    file_name  = "{}-{}-{}".format(args.year, args.month, args.day)
    file_path = year_folder + "/" + file_name + ".tex"

    if os.path.exists(file_path):    
        print("File called ")
        return 1

    month_int_to_month_str = {1:"January", 2:"February", 3:"March", 4:"April",5:"May", 6:"June", 7:"July", 8:"August", 9:"September",10:"October",11:"November",12:"December"}

    arguments = {"file_name":file_name, "year":args.year, "month":args.month, "month_str":month_int_to_month_str[today.month], "day":args.day,"author":args.author, "institute":args.institute}
    tex_entry = """%%% Research Diary - Entry
\documentclass[11pt,letterpaper]{{article}}

\\newcommand{{\\workingDate}}{{\\textsc{{{year} $\\mid$ {month_str} $\\mid$ {day}}}}}
\\newcommand{{\\userName}}{{{author}}}
\\newcommand{{\\institution}}{{institute}}
\\usepackage{{research_diary}}

\\begin{{document}}
\\logoPNG % you can find this in research_diary.sty

{{\\Huge {month_str} {day} }}
\\section*{{ }}





\\end{{document}}
""".format(**arguments)

    #copy to file
    out_file = open(file_path, 'w')
    out_file.write(tex_entry)
    print("done!")

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
    parser.add_argument(
        "-mo", 
        "--month", 
        type=str,
        default=MONTH,
        help = "name of the institute"
        )
    parser.add_argument(
        "-d", 
        "--day", 
        type=str,
        default=DAY,
        help = "name of the institute"
        )
    args = parser.parse_args()
    #fancy way to print arguments
    arguments = {'year':args.year, 'institute':args.institute, 'author':args.author, 'month': MONTH, 'day':DAY}
    print("Creating research diary for year {year}, author {author}, and institute {institute}".format(**arguments))
    main(args)
