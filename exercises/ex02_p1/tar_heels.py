"""Tar Heels exercise redux as a structured program."""

__author__ = "730230426"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))


def tar_heels(number: int) -> str:
    """This is a function that will return words."""
    if number % 2 == 0:
        if number % 2 == 0 and number % 7 == 0:
            return("TAR HEELS") 
        else: 
            return("TAR")
    else:
        if number % 7 == 0: 
            return("HEELS")
        else: 
            return("CAROLINA")


if __name__ == "__main__":
    main()