import os
from tqdm import tqdm

files = input("What files to refresh (Enter for all): ")
if files == "":
    current_files = [f for f in os.listdir() if not f.startswith(".")]
    current_files.remove(__file__)

else:
    current_files = [f for f in files.split(" ")]


for name in current_files:
    try:
        work_file = open(name)
        operation_file = open("../" * 5 + f"usr/local/bin/{name}", "w+")
        print("\33[93m" + f"Cloning script {name}" + "\33[0m")
        lines = work_file.readlines()
        for line in tqdm(lines, ncols=100, ascii=True):
            operation_file.write(line)
    except FileNotFoundError:
        print("\33[91m" + f"{name} does not exists" + "\33[0m")
        continue

    operation_file.close()
    work_file.close()

    print("\33[92m" + f"Cloned script  {name}" + "\33[0m")
