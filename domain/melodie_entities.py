class Melodie:

    def __init__(self, titlu, artist, gen, data_aparitie):
        """
        Initializeaza obiect de tip Melodie cu titlu, artist, gen, data_aparitie
        :param titlu: titlul melodiei
        :type titlu: str
        :param artist: artistul melodiei:
        type artist: str
        :param gen: genul melodiei
        :type gen: str
        :param data_aparitie: data aparitiei pentru melodie
        :type data_aparitie: str (dd.MM.yyyy)
        """
        self.__titlu = titlu
        self.__artist = artist
        self.__gen = gen
        self.__data_aparitie = data_aparitie

    def getTitlu(self):
        return self.__titlu

    def getArtist(self):
        return self.__artist

    def getGen(self):
        return self.__gen

    def getDataAparitie(self):
        return self.__data_aparitie

    def setTitlu(self, value):
        self.__titlu = value

    def setArtist(self, value):
        self.__artist = value

    def setGen(self, value):
        self.__gen = value

    def setDataAparitie(self, value):
        self.__data_aparitie = value

    def __str__(self):
        return f"Titlu: {self.__titlu}; Artist: {self.__artist}; Gen: {self.__gen}; Data aparitie: {self.__data_aparitie}"

    def __eq__(self, other):
        """
        Verifica daca doua obiecte de tip Melodie sunt egale
        :param other: obiectul cu care comparam
        :type other: Melodie
        :return: True - daca cele doua melodii sunt 'egale' (au acelasi titlu si artist), False - in caz contrar
        """
        return self.__titlu == other.getTitlu() and self.__artist == other.getArtist()


def teste_entities():
    m1 = Melodie('melodie1', 'abc', 'Jazz', '05.05.2022')
    assert (m1.getTitlu() == 'melodie1')
    assert (m1.getArtist() == 'abc')
    assert (m1.getGen() == 'Jazz')
    assert (m1.getDataAparitie() == '05.05.2022')
    m1.setGen('Rock')
    m1.setTitlu('melodie2')
    m1.setArtist('abcd')
    m1.setDataAparitie('06.12.2022')
    assert (m1.getTitlu() == 'melodie2')
    assert (m1.getArtist() == 'abcd')
    assert (m1.getGen() == 'Rock')
    assert (m1.getDataAparitie() == '06.12.2022')
    m2 = Melodie('melodie3', 'abcd', 'Rock', '06.12.2022')
    try:
        assert m1 == m2
        assert False
    except AssertionError:
        assert True
    m3 = Melodie('melodie2', 'abcd', 'Rock', '07.12.2022')
    assert m1 == m3
    m4 = Melodie('melodie4', 'abcdefghi', 'Pop', '18.04.2022')
    assert (m4.getGen() == 'Pop')
    assert (m4.getTitlu() == 'melodie4')
    assert (m4.getArtist() == 'abcdefghi')
    assert (m4.getDataAparitie() == '18.04.2022')


if __name__ == '__main__':
    teste_entities()


