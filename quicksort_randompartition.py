#
# Opis: Implementacja algorytmu sortowania szybkiego (quicksort) z wyborem losowego elementu jako pivotu.
# (Randomized partition)
# Złożoność czasowa: O(n*log(n))
# Złożoność pamięciowa: O(log(n))
#
import random


# Wybierz element nazwany Pivot
# Idąc w górę znajdź pierwszy element >= Pivot
# Idąc w dół znajdź pierwszy element <= Pivot
# Zamień te elementy miejscami
# Powtarzaj aż do momentu, gdy indeksy górny i dolny się przetną
# Argumenty: A - tablica; l - indeks dolny; h - indeks górny
def partition(A, l, r):
    # Pivot ustawiony na pierwszy element
    pivot = A[l]
    i = l
    j = r

    while True:
        # Idąc w górę (przesuwamy i) znajdź pierwszy element >= Pivot
        while A[i] < pivot:
            i = i + 1
        # Idąc w dół (przesuwamy j) znajdź pierwszy element <= Pivot
        while A[j] > pivot:
            j = j - 1

        # Jeśli indeksy się przetną to zwróć j
        if i >= j:
            return j

        # Zamień elementy miejscami
        A[i], A[j] = A[j], A[i]

        # Przesuń indeksy
        i = i + 1
        j = j - 1

# Wybierz losowy element jako pivot
# Zamień go z pierwszym elementem
# Wykonaj partition
# Argumenty: A - tablica; l - indeks dolny; h - indeks górny
def random_partition(A, l, r):
    pivot = random.randint(l, r)
    # Zamiana pivota na początek tablicy
    A[l], A[pivot] = A[pivot], A[l]
    return partition(A, l, r)


# Podziel tablicę A na dwie części: A1[p..q] i A2[q+1..r], gdzie każdy element z A1 <= każdy element z A2
# Sortuj rekurencyjnie A1 i A2
# Argumenty: A - tablica; p - indeks dolny; r - indeks górny
def quicksort(A, l, r):
    if l < r:
        # Znajdź indeks pivotu taki, że elementy na lewo od pivotu są mniejsze, a na prawo większe
        pi = partition(A, l, r)

        # Sortowanie rekurencyjne lewej i prawej części
        quicksort(A, l, pi)
        quicksort(A, pi + 1, r)


if __name__ == '__main__':
    array = [10, 7, 8, 9, 1, 5]
    N = len(array)

    quicksort(array, 0, N - 1)
    print('Posortowana tablica:')
    for x in array:
        print(x, end=" ")
