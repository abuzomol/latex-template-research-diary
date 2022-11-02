# latex-template-research-diary
This is a latex template to automatically generate tex files each research day and compile all of them together based on year.

To add an entry run the following code

```
python3 add_entry.py
```

You can change the author and the institute or add them as argument to the python file. 

You can change the logo picture by adding your own and modifing \logoPNG in research_diary.sty file


Finally, you produce the entire year diary in a single pdf file by running the command:

```
  python3 create_anthology.py
```

or simply writing:

```
  make
```


Note: tested on python3 verion 3.10.8. It might work on verion 3.9 but not less!
