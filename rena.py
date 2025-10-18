import os


for i in range(0, 10):
    old = f"data/Day{i+1}"
    new = f"data/VideonDay-{i+1}"
    if os.path.exists(old):
        os.rename(old, new)

    