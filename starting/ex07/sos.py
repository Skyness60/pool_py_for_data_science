import sys


def main():
    """
    Main function to run the program.
    """
    assert len(sys.argv) > 1
    assert all(map(str.isalnum, sys.argv[1].split()))
    MORSE = dict(
        zip(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ",
            ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- "
            ".--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. "
            "----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----. /".split(),
        )
    )
    for word in sys.argv[1].split():
        for char in word:
            print(MORSE[char.upper()], end=" ")
        print()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("AssertionError: the argument are bad")
