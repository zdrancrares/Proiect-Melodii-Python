from domain.melodie_entities import Melodie


def comapara_date(data1, data2):
    """
    Comapara doua date
    :param data1: prima data
    :param data2: a doua data
    :return: True daca data1 este mai 'mica' decat data2
    """
    data1_string = data1.split('.')
    zi_data1 = int(data1_string[0])
    luna_data1 = int(data1_string[1])
    an_data1 = int(data1_string[2])

    data2_string = data2.split('.')
    zi_data2 = int(data2_string[0])
    luna_data2 = int(data2_string[1])
    an_data2 = int(data2_string[2])

    if an_data1 < an_data2:
        return True
    elif an_data1 == an_data2 and luna_data1 < luna_data2:
        return True
    elif an_data1 == an_data2 and luna_data1 == luna_data2 and zi_data1 < zi_data2:
        return True
    return False


def merge(arr1, arr2):
    """
    Interclaseaza doua liste
    :param arr1: prima list
    :type arr1: lista cu obiecte de tip Melodie
    :param arr2: a doua lista
    :type arr2: lista cu obiecte de tip Melodie
    :return: cele doua liste interclasate
    """
    result = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if comapara_date(arr1[i].getDataAparitie(), arr2[j].getDataAparitie()):
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result


def merge_sort(arr):
    """
    Functie de sortare a unei liste
    :param arr: lista de sortat
    :type arr: lista cu obiecte de tip Melodie
    :return: lista sortata dupa data aparitiei
    """
    lungime = len(arr)
    if lungime <= 1:
        return arr
    middle = lungime // 2
    arr_left = merge_sort(arr[:middle])
    arr_right = merge_sort(arr[middle:])
    return merge(arr_left, arr_right)


def test_merge():
    m1 = Melodie('melodie1', 'abc', 'Jazz', '05.12.2022')
    m2 = Melodie('melodie2', 'abcd', 'Pop', '19.11.2021')
    m3 = Melodie('melodie3', 'abcde', 'Rock', '14.04.2022')
    m4 = Melodie('melodie4', 'abcdef', 'Pop', '01.01.2021')
    m5 = Melodie('melodie5', 'abcdefg', 'Jazz', '16.12.2020')
    m6 = Melodie('melodie6', 'apsdasd', 'Pop', '08.08.2022')
    m7 = Melodie('melodie7', 'aapsdpaspd', 'Rock', '02.02.2023')

    lista = [m1, m2, m3, m4, m5, m6, m7]
    lista = merge_sort(lista)

    assert (lista[0] == m5)
    assert (lista[1] == m4)
    assert (lista[2] == m2)
    assert (lista[3] == m3)
    assert (lista[4] == m6)
    assert (lista[5] == m1)
    assert (lista[6] == m7)


if __name__ == '__main__':
    test_merge()


