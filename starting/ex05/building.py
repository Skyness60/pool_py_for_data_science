import sys


def count_if(pred, it: str) -> int:
    """Compter les éléments d’un itérable satisfaisant un prédicat."""
    return sum(map(pred, it))


def is_punctuation(c: str) -> bool:
    """True si c est une ponctuation (ni alphanumérique, ni espace)."""
    return not c.isalnum() and not c.isspace()


def main() -> None:
    """
    Compter majuscules/minuscules/ponctuation/espaces/chiffres dans un texte.

    - 0 argument : prompt puis lecture stdin (\\n compte comme espace)
    - 1 argument : texte = argv[1]
    - >1 argument : affiche AssertionError
    """
    argc = len(sys.argv)

    if argc == 1:
        print("What is the text to count?")
        try:
            text = sys.stdin.read()
        except EOFError:
            text = ""
    elif len(sys.argv) == 2:
        text: str = sys.argv[1]

    else:
        print("AssertionError: more than one argument is provided")
        return

    print(f"The text contains {len(text)} characters:")
    print(f"{count_if(str.isupper, text)} upper letters")
    print(f"{count_if(str.islower, text)} lower letters")
    print(f"{count_if(is_punctuation, text)} punctuation marks")
    print(f"{count_if(str.isspace, text)} spaces")
    print(f"{count_if(str.isdigit, text)} digits")


if __name__ == "__main__":
    main()
