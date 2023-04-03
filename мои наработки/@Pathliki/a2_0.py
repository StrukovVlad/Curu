import os

def func(__file__):
    print(os.path.join(os.path.abspath(os.path.dirname(__file__)),'111.txt'))

p = '/Users/Влад/Desktop/html'

func(p)  # C:\Users\Влад\Desktop\111.txt
# _____________________________________________________________________________
combined_path = os.path.join(p, "main_file.py")

print(combined_path) # /Users/Влад/Desktop/html\main_file.py
# _____________________________________________________________________________
# absolute path
p = '/Users/Влад/Desktop/html'

combined_path = os.path.join(p, "tutorials", "main_file.py")

print(combined_path) # /Users/Влад/Desktop/html\tutorials\main_file.py
# _______________________________________________________________________________
# absolute path
p = '/Users/Влад/Desktop/html'

combined_path = os.path.join("tutorials", p,  "main_file.py")

print(combined_path)  # /Users/Влад/Desktop/html\main_file.py
# ________________________________________________________________________________
# absolute path
p = '/Users/Влад/Desktop/html'

combined_path = os.path.join("tutorials", "main_file.py", p)

print(combined_path)  # /Users/Влад/Desktop/html
# ___________________________________________________________________________________
# absolute path
p = '/Users/Влад/Desktop/html'

combined_path = os.path.join(p, "tutorials", "main_file.py", "")

print(combined_path)  # /Users/Влад/Desktop/html\tutorials\main_file.py\
# ____________________________________________________________________________________
path = ["home", "tutorial", "main.py"]

combined_path = os.path.join(*path)

print(combined_path) # home\tutorial\main.py
# ______________________________________________________________________________________