
from prac_06.programming_languange import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(ruby)
print(python)
print(visual_basic)

list_language = [ProgrammingLanguage("Ruby", "Dynamic", True, 1995), ProgrammingLanguage("Python", "Dynamic", True, 1991),
                 ProgrammingLanguage("Visual Basic", "Static", False, 1991)]

print('The dynamically typed language are: ')
for language in list_language:
    if language.is_dynamic():
        print(language.language_name)  #language_name as initialized in class


