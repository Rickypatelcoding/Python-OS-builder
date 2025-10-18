import os 

Totaldir = os.listdir("data")

for index, tdir in enumerate(Totaldir , start=1):
    path = os.path.join("data", tdir)
    if not os.path.isdir(path):
        continue

    items = os.listdir(path)
    if not items:
        continue
    else:
        print(f"{items} index {index} value {tdir}")