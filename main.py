def is_palindrome(n):
    """
    determina daca nr e palindrom
    :param n: nr. intreg
    :return: true daca nr. e palindrom,iar false in caz contrar
    """
    cn = n
    pal = 0
    while cn != 0:
        pal = pal * 10 + cn % 10
        cn = cn // 10
    if (n == pal):
        return True
    else:
        return False


def test_is_palindrome():
    """
    testeaza daca functia is_palindrom functioneaza
    :return: true daca  e palindrom,iar false in caz contrar
    """
    assert is_palindrome(12) is False
    assert is_palindrome(100) is False
    assert is_palindrome(121) is True
    assert is_palindrome(1331) is True
    assert is_palindrome(1) is True


def is_superprime(n):
    """
    Determina daca un numar e superprim
    :param n: nr. intreg
    :return:True daca n e nr. superprim si False in caz contrar
    """
    if n < 2:
        return False
    else:
        while n != 0:
            for i in range(2, n // 2 + 1):
                if n % i == 0:
                    return False
            n = n // 10
    return True


def test_is_superprime():
    """
    testeaza daca functia is_superprime functioneaza
    :return: true daca nr. e superprim, false in caz contrar
    """
    assert is_superprime(233) is True
    assert is_superprime(237) is False
    assert is_superprime(1) is False


def is_prime(n):
    """
    Determina daca un numar dat este prim
    :param n: nr. intreg
    :return: True daca acesta este numar prim, False in caz contrar
    """
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
    else:
        return False
    return True


def get_largest_prime_below(n):
    """
    Calculeaza ultimul nr. prim mai mic decat un nr. dat
    :param n: nr. intreg
    :return: numarul prim mai mic decat nr. dat
    """
    for i in reversed(range(n)):
        if is_prime(i):
            return i


def test_get_largest_prime_below():
    """
    Testeaza daca functia get_largest_prime_below(n) functioneaza
    :return: true daca nr. e superprim, false in caz contrar
    """
    assert get_largest_prime_below(4) == 3
    assert get_largest_prime_below(5) == 3
    assert get_largest_prime_below(11) == 7
    assert get_largest_prime_below(14) == 13


def main():
    test_is_palindrome()
    test_is_superprime()
    test_get_largest_prime_below()
    while True:
        print("1. Determinati palindromul unui numar")
        print("2. Determinati daca un numar este superprim")
        print("3. Determinati ultimul nr. prim mai mic decat un nr. dat")
        print("x. Iesire")

        optiune = input("Dati optiunea: ")
        if optiune == "1":
            n = int(input("Dati numarul pentru care doriti sa vedeti daca e palindrom: "))
            if is_palindrome(n):
                print(" este palindrom")
            else:
                print(" nu este palindrom")
        elif optiune == "2":
            n = int(input("Dati numarul pentru care doriti sa vedeti daca e superprim: "))
            if is_superprime(n):
                print(" este superprim")
            else:
                print(" nu este superprim")
        elif optiune == "3":
            n = int(input("Dati numar: "))
            if get_largest_prime_below(n):
                print(get_largest_prime_below(n))
            else:
                print("Nu exista nr. prim mai mic ca n")
        elif optiune == "x":
            break
        else:
            print("Optiune gresita. Incercati din nou!")


if __name__ == '__main__':
    main()