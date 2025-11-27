import sys
from pathlib import Path

def create_python_file(file_name, template) -> None:
    with open(file_name, "w") as fn, open(template, "r") as t:
        for line in t:
            fn.write(line)


def main():

    if len(sys.argv) == 3:

        # Step 1: Get the files.
        first_file = sys.argv[1]
        last_file = sys.argv[2]

        # Step 2: Create files.
        first_index = int(first_file.replace("ex", "").replace(".py", ""))
        last_index = int(last_file.replace("ex", "").replace(".py", ""))
        if first_index > last_index:
            first_index, last_index = last_index, first_index

        for file_index in range(first_index, last_index + 1):
            file_name = f"ex{file_index}.py"
            template = Path(__file__).parent / "ex_template.txt"
            create_python_file(file_name, template)

    else:
        print("Failed to create script: use python3 ex_initial.py ex_final.py to create ex files.")


if __name__ == "__main__":
    main()
