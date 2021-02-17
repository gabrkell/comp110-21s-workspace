"""Fortune cookie exercise redux as a structured program."""

from random import randint
__author__ = "730230426"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """This is my fortune cookie function."""
    Fortune_1 = str("You will succeed in this class.")
    Fortune_2 = str("You will have a great day.")
    Fortune_3 = str("You will have a happy life.")
    Fortune_4 = str("You will be successful in life.")
    number: int = randint(1, 100)
    if number <= 25:
        return Fortune_1
    else:
        if number <= 50:
            return Fortune_2
        else:      
            if number <= 75:
                return Fortune_3
            else:
                return Fortune_4
                

# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
