import shutil
import os
for i in range(1,11):
    print(i)

shutil.copy("main.py", "maon2.py")
# shutil.copy("main.py", "newpy")
# shutil.move(".")
# shutil.move("main.py", "../file.text")
os.remove("maon2.py")
