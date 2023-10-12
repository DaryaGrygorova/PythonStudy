"""
Creates a new output file called myfile.txt and writes
the string "Hello file world!" in it
"""

# Creates new file in the directory where scripts was run
with open('myfile.txt', 'a', encoding="UTF-8") as file_obj:
    file_obj.write("Hello file world!\n")

# Creates new file in the directory 'src' that was included in the directory where scripts was run
with open('src\\myfile.txt', 'a', encoding="UTF-8") as file_obj:
    file_obj.write("Hello file world!\n")
