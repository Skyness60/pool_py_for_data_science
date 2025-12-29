import sys


def main():
    """
    Déterminer la parité d’un entier fourni en ligne de commande.

    Usage:
        python program.py <integer>

    Contrat:
        - Un seul argument est attendu en ligne de commande
        - L’argument doit représenter un entier décimal valide
        - Les entiers négatifs sont acceptés

    Comportement:
        - Affiche "I'm Even." si l’entier est pair
        - Affiche "I'm Odd." si l’entier est impair

    Erreurs:
        - AssertionError si le nombre d’arguments est incorrect
        - AssertionError si l’argument n’est pas un entier valide

    Effets de bord:
        - Écriture sur la sortie standard
    """
    if len(sys.argv) != 2:
        raise AssertionError("more than one argument is provided")
    elif not sys.argv[1].lstrip("-").isdigit():
        raise AssertionError("argument is not a positive integer")

    elif int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
