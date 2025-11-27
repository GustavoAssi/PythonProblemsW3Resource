import subprocess


def system_command_output() -> None:
    """
    This program gets system command outputs.
    Author: Gustavo Assi Alencar.
    Date:   14/11/2025.
    """

    # Step 1: Display system outputs.
    returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
    print(returned_text)

def main() -> None:
    system_command_output()


if __name__ == "__main__":
    main()
