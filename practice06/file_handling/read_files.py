import shutil
import os

with open("test.txt", "w") as file:
    file.write("Hello\n")
    file.write("World\n")

with open("test.txt", "r") as file:
    content = file.read()

print(content)

with open("test.txt", "a") as file:
    file.write("My name is Aktilek")

shutil.copy("test.txt", "test_backup.txt")

if os.path.exists("test_backup.txt"):
    os.remove("test_backup.txt")
    print("File deleted successfully")
else:
    print("File does not exist")