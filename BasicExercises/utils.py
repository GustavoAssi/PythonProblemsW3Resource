class Input:

    @staticmethod
    def get_character(message: str = "Type a character: ") -> str:
        """
        This method is used to get characters from user on terminal.

        :param message: (str) a message displayed on terminal for the user.
        :return:        (str) the charcater inputed by the user.
        """
        character = input(f"{message}")
        while len(character) != 1:
            print("Input must be a single character! Try again...")
            character = input(f"{message}")

        return character


    @staticmethod
    def get_string(message: str = "Type a string:", stripped: bool = False) -> str:
        """
        This method is used to get strings from user on terminal.

        :param message:  (str) a message displayed on terminal for the user.
        :param stripped: (bool) if the string should have spaces removed in the beggining and in the end.
        :return:         (str) the string inputed by the user.
        """
        string = input(f"{message}")
        if stripped:
            string = string.strip()

        return string
	

    @staticmethod
    def get_integer_number(message: str = "Type an integer number: ", must_be_positive: bool = False) -> int:
        """
        This method is used to get integer numbers from user on terminal.

        :param message:            (str) a message displayed on terminal for the user.
        :param must_be_positive:   (bool) if the number must be positive.
        :return:                   (int) the integer number inputed by the user.
        """
        while True:
            try:
                integer = int(input(f"{message}").strip())
                if integer < 0 and must_be_positive:
                    print("The number must be positive! Try again...")
                    continue
                return integer
            except ValueError as e:
                print(f"Couldn't get the integer number -> {e}")


    @staticmethod
    def get_float_number(message: str = "Type a float number: ", must_be_positive: bool = False) -> float:
        """
        This method is used to get float numbers from user on terminal.

        :param message:            (str) a message displayed on terminal for the user.
        :param must_be_positive:   (bool) if the number must be positive.
        :return:                   (float) the float number inputed by the user.
        """
        while True:
            try:
                float_number = float(input(f"{message}").strip())
                if float_number < 0 and must_be_positive:
                    print("The number must be positive! Try again...")
                    continue
                return float_number
            except ValueError as e:
                print(f"Couldn't get the float number -> {e}")
