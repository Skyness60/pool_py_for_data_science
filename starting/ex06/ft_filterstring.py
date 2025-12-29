import sys

from ft_filter import ft_filter


def main():
    """
    Filter words in a string based on their length.
    """
    assert len(sys.argv) == 3
    s = sys.argv[1]
    n = sys.argv[2]

    assert n.isdigit()
    n = int(n)

    words = s.split(" ")

    filtered_words = ft_filter(lambda w: len(w) > n, words)

    result = list(filtered_words)
    print(result)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("AssertionError: the arguments are bad")
