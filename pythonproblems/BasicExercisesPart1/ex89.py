from pythonproblems.functions.utils import Input


def conditional_action() -> None:
    """
    This program perform an action given a condition.
    Author: Gustavo Assi Alencar.
    Date:   13/11/2025.
    """

    try:
        # Step 1: Get an condition.
        result = {}
        condition = Input.get_string("Type a single line condition (Python command): ", stripped=True)
        exec(f"condition_result = {condition}", result)
        condition_result = result["condition_result"]

        # Step 2: Get an action.
        action = Input.get_string("Type an single line action (Python command): ", stripped=True)

        # Step 3: Execute the action if condition is True.
        if condition_result:
            exec(f"{action}")

    except Exception as e:
        print(f"Failed to run program: {e}")


def main() -> None:
    conditional_action()


if __name__ == "__main__":
    main()
