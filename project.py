from main_functions import start_program, add_item, remove_item, exit_program


def main():
    """
    The main interface that allows graceful dealing with the codebase.
    It allows to start program, add an item and exit.
    """
    menu_options = {
        "s" : start_program,
        "a" : add_item,
        "r" : remove_item,
        "e" : exit_program
    }

    while True:
        print("Options: ")
        print("[s] start program")
        print("[a / r] add / remove item")
        print("[e] exit program")

        try:
            var = input("").lower()[0]
        except IndexError:
            print("Invalid Input. Type in the correc letter from av. options.")

        if var in menu_options:
            menu_options[var]()
        else:
            print("Invalid input. Please choose [s|a|r|e].")


if __name__ == "__main__":
    main()
