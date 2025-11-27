import time

from ex129 import add_leading_zeros


def program_runtime_calculator() -> None:
    """
    This program calculates the time runs (difference between start and current time) of a program.
    Author: Gustavo Assi Alencar.
    Date:   20/11/2025.
    """

    # Step 1: Mark the execution start.
    start = time.time()

    # Step 2: Run any program from this Project.
    add_leading_zeros()

    # Step 3: Mark the execution end.
    end = time.time()

    # Step 4: Display the execution duration.
    execution_duration = round(end - start, 3)
    print(f">>> Execution time: {execution_duration} s")


def main():
    program_runtime_calculator()


if __name__ == "__main__":
    main()
