def print_menu():
    print("1. Citire date")
    print("2. Determinare cea mai lunga subsecventa cu proprietatea ca produsul numerelor este impar")
    print("3. Determinare cea mai lunga subsecventa cu proprietatea ca concatenarea numerelor din subsecventa are cifrele in ordine crescatoare")
    print("4. Determina cea mai lunga subsecventa cu proprietatea ca toate numerele sunt prime")
    print("5. Iesire")

def citire_lista():
    l = []
    n = int(input("Dati numarul de elemente: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l


def produsul_numerelor_este_impar(l):
    '''
    Determina produsul numerelor dintr-o lista
    :param l: o lista de numerele intregi
    :return: True, daca produsul este impar, False in caz contrar
    '''
    if len(l)==0:
        return False
    produs=1
    for x in l:
        produs=produs*x
    if produs%2==1:
        return True
    return False

def test_produsul_numerelor_este_impar():
    '''
    Functie de test
    '''
    assert produsul_numerelor_este_impar([]) == False
    assert produsul_numerelor_este_impar([1,3,5]) == True
    assert produsul_numerelor_este_impar([2]) == False
    assert produsul_numerelor_este_impar([11,7]) == True

def get_longest_product_is_odd(l):
    '''
    Determinare cea mai lunga subsecventa cu proprietatea ca produsul numerelor este impar
    :param l: o lista de numere intregi
    :return: cea mai lunga subsecventa din l cu proprietatea ca produsul numerelor este impar
    '''
    subsecventa_maxima = []
    for i in range(len(l)):
        for j in range(i,len(l)):
            if produsul_numerelor_este_impar(l[i:j+1]) and len(subsecventa_maxima) < len(l[i:j+1]):
                subsecventa_maxima = l[i:j+1]
    return subsecventa_maxima

def test_get_longest_product_is_odd():
    '''
    Functie de test
    '''
    assert get_longest_product_is_odd([1,2,3,5]) == [3, 5]
    assert get_longest_product_is_odd([1]) == [1]
    assert get_longest_product_is_odd([4, 2, 3, 5, 7]) == [3, 5, 7]

def concatenarea_numerelor_ordine_crescatoare(l):
    '''
    Concateneaza numerele dintr-o lista
    :param l: o lista de numere naturale
    :return: True, daca concatenarea are cifrele in ordine crescatoare, False in caz contrar
    '''
    if len(l) == 0:
        return False
    numar_format = l[0]
    for i in range(1,len(l)):
        numar_format = int(str(numar_format) + str(l[i]))
    while numar_format > 9:
        if numar_format%10 < numar_format//10%10:
            return False
        numar_format = numar_format//10
    return True

def test_concatenarea_numerelor_ordine_crescatoare():
    '''
    Functie de test
    '''
    assert concatenarea_numerelor_ordine_crescatoare([1,23,4]) == True
    assert concatenarea_numerelor_ordine_crescatoare([]) == False
    assert concatenarea_numerelor_ordine_crescatoare([12,345,2]) == False
    assert concatenarea_numerelor_ordine_crescatoare([1,2,3,4,56789]) == True

def get_longest_concat_digits_asc(l):
    '''
    Determina cea mai lunga subsecventa cu proprietatea ca concatenarea numerelor din subsecventa are cifrele in ordine crescatoare
    :param l: o lista de numere naturale
    :return: cea mai lunga subsecventa din l cu proprietatea ca concatenarea numerelor din subsecventa are cifrele in ordine crescatoare
    '''
    subsecventa_maxima = []
    for i in range(len(l)):
        for j in range(i,len(l)):
            if concatenarea_numerelor_ordine_crescatoare(l[i:j+1]) and len(subsecventa_maxima) < len(l[i:j+1]):
                subsecventa_maxima = l[i:j+1]
    return subsecventa_maxima

def test_get_longest_concat_digits_asc():
    '''
    Functie de test
    '''
    assert get_longest_concat_digits_asc([1,3,1,23,4,1]) == [1,23,4]
    assert get_longest_concat_digits_asc([9,7,4,3]) == [9]
    assert get_longest_concat_digits_asc([4,4,2,1,2]) == [4,4]

def is_prime(x):
    '''
    Verifica daca un numar este prim
    :param x: un numar intreg
    :return: True, daca x este prim, False in caz contrar
    '''
    if x<2:
        return False
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    return True

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(1) == False
    assert is_prime(23) == True

def toate_numere_prime(l):
    '''
    Verifica daca numerele dintr-o lista sunt prime
    :param l: o lista de numere intregi
    :return: True, daca toate numerele din lista sunt prime, False in caz contrar
    '''
    for x in l:
        if is_prime(x) == False:
            return False
    return True

def test_toate_numere_prime():
    assert toate_numere_prime([1, 2, 3, 4, 5]) == False
    assert toate_numere_prime([2, 3, 5]) == True
    assert toate_numere_prime([23]) == True

def get_longest_all_primes(l):
    '''
    Determina cea mai lunga subsecventa cu proprietatea ca toate numerele sunt prime
    :param l: o lista de numere intregi
    :return: cea mai lunga subsecventa din l cu proprietatea ca toate numerele sunt prime
    '''
    subsecventa_maxima = []
    for i in range(len(l)):
        for j in range(i,len(l)):
            if toate_numere_prime(l[i:j+1]) and len(subsecventa_maxima) < len(l[i:j+1]):
                subsecventa_maxima = l[i:j+1]
    return subsecventa_maxima

def test_get_longest_all_primes():
    assert get_longest_all_primes([1, 2, 3, 5]) == [2, 3, 5]
    assert get_longest_all_primes([1, 2, 3, 4, 5]) == [2, 3]
    assert get_longest_all_primes([1, 4, 6, 8, 10]) == []

def main():
    test_produsul_numerelor_este_impar()
    test_get_longest_product_is_odd()
    test_concatenarea_numerelor_ordine_crescatoare()
    test_get_longest_concat_digits_asc()
    test_is_prime()
    test_toate_numere_prime()
    test_get_longest_all_primes()
    l = []
    while True:
        print_menu()
        optiune = int(input("Dati optiunea: "))
        if optiune == 1:
            l = citire_lista()
        elif optiune == 2:
            print(get_longest_product_is_odd(l))
        elif optiune == 3:
            print(get_longest_concat_digits_asc(l))
        elif optiune == 4:
            print(get_longest_all_primes(l))
        elif optiune == 5:
            break
        else:
            print("Optiune gresita! Reincercati!")

main()