import os
from tqdm import tqdm


def file_cleanup(files, SYSTEM_COMMANDS):
    current_files = []
    for f in files:
        if f.startswith(".") or f in SYSTEM_COMMANDS:
            if not f.startswith("."):
                print(
                    "\33[91m",
                    f,
                    "is already a default bash command and will not be used\n",
                    "\33[0m")
            continue

        elif f in [__file__, "existing_commands.txt"]:
            continue

        current_files.append(f)

    return current_files


if __name__ == "__main__":
    with open("existing_commands.txt") as f:
        SYSTEM_COMMANDS = f.readline().split(",")

    files = input("What files to refresh (Enter for all): ")

    current_files = file_cleanup(
        os.listdir() if files == "" else files.strip().split(" "),
        SYSTEM_COMMANDS)

    for name in current_files:
        try:
            work_file = open(name)
            operation_file = open("../" * 5 + f"usr/local/bin/{name}", "w+")

            print("\33[93m" + f"Cloning script {name}" + "\33[0m")

            for line in tqdm(work_file.readlines(), ncols=100, ascii=True):
                operation_file.write(line)

        except FileNotFoundError:
            print("\33[91m" + f"{name} does not exists\n" + "\33[0m")
            continue

        operation_file.close()
        work_file.close()

        print("\33[92m" + f"Cloned script  {name}\n" + "\33[0m")
