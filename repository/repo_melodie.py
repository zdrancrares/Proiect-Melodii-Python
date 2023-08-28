import random

from domain.melodie_entities import Melodie


class FileRepoMelodie:

    def __init__(self, filename):
        """
        Initializeaza repository de melodii cu numele fisierului ce lucreaza cu o lista de melodii
        :param filename: numele fisierului
        :type filename: str
        """
        self.__filename = filename

    def __load_from_file(self):
        """
        Incarca lista de melodii din fisier
        :return: lista de melodii din fisier
        """
        with open(self.__filename, 'r') as f:
            lines = f.readlines()
            melodii = []
            for line in lines:
                line = line.strip()
                if line != '':
                    parts = line.split(';')
                    titlu = parts[0]
                    artist = parts[1]
                    gen = parts[2]
                    data_aparitie = parts[3]
                    m = Melodie(titlu, artist, gen, data_aparitie)
                    melodii.append(m)
            return melodii

    def _save_to_file(self, lista):
        """
        Salveaza o lista de melodii in fisier
        :param lista: lista de melodii
        :type lista: list (care contine obiecte de tip Melodie)
        """
        with open(self.__filename, 'w') as f:
            for elem in lista:
                elem_string = f"{elem.getTitlu()};{elem.getArtist()};{elem.getGen()};{elem.getDataAparitie()}\n"
                f.write(elem_string)

    def _find_by_title_artist(self, titlu, artist):
        """
        Cauta o melodie in lista dupa titlu si artist
        :param titlu: titlul de cautat
        :type titlu: str
        :param artist: artistul de cautat
        :type artist: str
        :return: True - daca exista in lista o melodie cu acest titlu si artist, False - in caz contrar
        """
        lista = self.__load_from_file()
        for elem in lista:
            if elem.getTitlu() == titlu and elem.getArtist() == artist:
                return True
        return False

    def update(self, m, gen_nou, data_noua):
        """
        Modifica genul si data unei melodii care contine titlul si artistul introduse
        :param m: melodia de modificat
        :type m: Melodie
        :param gen_nou: genul nou pentru melodie
        :type gen_nou: str
        :param data_noua: data_noua pentru melodie
        :type data_noua: str
        :return: melodia modificata(daca s-a reusit modificarea)
        :raises: ValueError daca nu exista melodie cu titlu si artist intrduse
        """
        if not self._find_by_title_artist(m.getTitlu(), m.getArtist()):
            raise ValueError('Nu exista nicio melodie cu acest titlu si artist.')
        lista = self.__load_from_file()
        for elem in lista:
            if elem.getTitlu() == m.getTitlu() and elem.getArtist() == m.getArtist():
                elem.setGen(gen_nou)
                elem.setDataAparitie(data_noua)

        self._save_to_file(lista)

    def genereaza_melodii_random(self, nr_melodii, lista_titluri, lista_artisti):
        """
        Genereaza random melodii cu titluri si artisti introdusi de autor
        :param nr_melodii: numarul de melodii de generat
        :type nr_melodii: int
        :param lista_titluri: lista cu titluri cu care se genereaza melodiile
        :type lista_titluri: str
        :param lista_artisti: lista cu artisti cu care se genereaza melodiile
        :type lista_artisti str
        """
        lista_genuri = ['Jazz', 'Pop', 'Rock']

        titluri = lista_titluri.split(',')
        titluri_de_ales = []
        for elem in titluri:
            titluri_de_ales.append(elem)

        artisti = lista_artisti.split(',')
        artisti_de_ales = []
        for elem in artisti:
            artisti_de_ales.append(elem)

        lista = self.__load_from_file()

        lista_cu_luni = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        lista_cu_zile = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']
        for i in range(nr_melodii):
            titlu_generat = random.choice(titluri_de_ales)
            artist_generat = random.choice(artisti_de_ales)
            gen_generat = random.choice(lista_genuri)
            zi = random.choice(lista_cu_zile)
            luna = random.choice(lista_cu_luni)
            an = str(random.randint(1000, 2022))
            lista_data = [zi, luna, an]
            data = '.'.join(lista_data)
            m = Melodie(titlu_generat, artist_generat, gen_generat, data)
            lista.append(m)

        self._save_to_file(lista)

    def get_all(self):
        """
        Returneaza lista de melodii
        :return: lista de melodii
        """
        return self.__load_from_file()

    def delete_all(self):
        """
        Sterge toate elementele din lista
        """
        lista = []
        self._save_to_file(lista)


def test_repo():
    repo = FileRepoMelodie('test_repo.txt')

    lista = repo.get_all()
    assert (len(lista) == 6)

    m1 = Melodie('melodie1', 'abc', 'Jazz', '07.07.2022')
    repo.update(m1, 'Jazz', '07.07.2022')

    lista = repo.get_all()
    for elem in lista:
        if elem.getTitlu() == m1.getTitlu() and elem.getArtist() == m1.getArtist():
            assert elem.getGen() == 'Jazz'
            assert elem.getDataAparitie() == '07.07.2022'

    m2 = Melodie('titlu3', 'artist3', 'Rock', '10.10.1800')
    repo.update(m2, 'Rock', '10.10.1800')

    lista = repo.get_all()
    for elem in lista:
        if elem.getTitlu() == m2.getTitlu() and elem.getArtist() == m2.getArtist():
            assert elem.getGen() == 'Rock'
            assert elem.getDataAparitie() == '10.10.1800'

    m3 = Melodie('titlu1000', 'artist1000', 'Jazz', '12.12.2022')
    try:
        repo.update(m3, 'Jazz', '12.12.2022')
        assert False
    except ValueError:
        assert True

    m4 = Melodie('titlu1', 'artisti40', 'Rock', '11.12.2022')
    try:
        repo.update(m4, 'Rock', '11.12.2022')
        assert False
    except ValueError:
        assert True

    lista_veche = repo.get_all()
    repo.genereaza_melodii_random(3, 'titlu200,titlu300,titlu400,titlu500', 'artist1000,artist2000')
    lista_noua = repo.get_all()
    assert len(lista_noua) == len(lista_veche) + 3
    repo._save_to_file(lista_veche)


if __name__ == "__main__":
    test_repo()

