from Static.Values import StaticValues

class Handler:
    @staticmethod
    def integer_handler(question, min=0, max=0):
        while True:
            try:
                value = int(input(f"{question} "))
                if value < min or (max != 0 and value > max):
                    print(f"{StaticValues.WARNING} Input must be between {min} and {max}.")
                else:
                    return value
            except ValueError:
                print(f"{StaticValues.WARNING} Invalid input, please enter a valid integer!")
