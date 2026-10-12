import os
import shutil

os.makedirs("practice06/data/students/exam", exist_ok=True)

items = os.listdir("practice06")
path = "pratice06"

for item in items:
    full_path = os.path.join(path, item)

    if os.path.isdir(full_path):
        print("Directory:", item)
    else:
        print("File:", item)

for item in items:
    if item.endswith(".txt"):
        print(item)


source = "./test.txt"
destination = "practice06/test.txt"

if os.path.exists(source):
    shutil.move(source, destination)
    print("File copied successfully.")
else:
    print("Source file does not exist.")