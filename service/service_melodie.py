from domain.melodie_validator import ValidatorMelodie
from repository.repo_melodie import FileRepoMelodie
from sortari.merge_sort import merge_sort

from domain.melodie_entities import Melodie


class ServiceMelodie:

    def __init__(self, validator, repo):
        """
        Initializeaza service de melodii cu validator si repository pentru melodii
        :param validator: validator de melodii
        :type validator: ValidatorMelodie
        :param repo: repository de melodii
        :type repo: RepoFileMelodie
        """
        self.__validator = validator
        self.__repo = repo

    def modificare_melodie(self, titlu, artist, gen_nou, data_noua):
        """
        Modifica genul si data unei melodii
        :param titlu: titlul melodiei de modificat
        :type titlu: str
        :param artist: artistul melodiei de verificat
        :type artist: str
        :param gen_nou: genul nou pentru melodie de modificat
        :type gen_nou: str
        :param data_noua: data noua pentru melodie de modificat
        :type data_noua: str
        return: melodia modificata
        """
        m = Melodie(titlu, artist, gen_nou, data_noua)
        self.__validator.validate(m)
        self.__repo.update(m, gen_nou, data_noua)
        return m

    def genereaza_aleator(self, numar_melodii, lista_titluri, lista_artisti):
        """
        Functie care genereaza aleator melodii cu titluri si artisti introdusi de utilizator
        :param numar_melodii: numarul de melodii de generat
        :type numar_melodii: int
        :param lista_titluri: lista de titluri cu care se genereaza melodii
        :type lista_titluri: str
        :param lista_artisti: lista de artisti cu care se genereaza melodii
        :type lista_artisti: str
        """
        self.__repo.genereaza_melodii_random(numar_melodii, lista_titluri, lista_artisti)

    def export_melodii(self, nume_fisier):
        """
        Exporta melodii sortate dupa data aparitiei
        :param nume_fisier: numele fisierului in care se exporta
        """
        with open(nume_fisier, 'w') as f:
            lista = self.__repo.get_all()
            lista = merge_sort(lista)
            for elem in lista:
                elem_string = f"{elem.getArtist()},{elem.getTitlu()},{elem.getDataAparitie()},{elem.getGen()}\n"
                f.write(elem_string)

    def get_all(self):
        return self.__repo.get_all()


def teste_service():
    repo = FileRepoMelodie('teste_service.txt')
    validator = ValidatorMelodie()
    service = ServiceMelodie(validator, repo)
    titlu = 'titlu3'
    artist = 'artist1'
    gen = 'Jazz'
    data = '08.08.2008'
    m = Melodie(titlu, artist, gen, data)
    service.modificare_melodie(titlu, artist, gen, data)
    lista = service.get_all()
    for elem in lista:
        if elem.getTitlu() == titlu and elem.getArtist() == artist:
            assert elem.getGen() == gen
            assert elem.getDataAparitie() == data
    gen = 'Pop'
    data = '18.18.2018'
    try:
        service.modificare_melodie(titlu, artist, gen, data)
        assert False
    except ValueError:
        assert True

    lista_veche= repo.get_all()
    service.genereaza_aleator(3, 'titlu200,titlu300,titlu400,titlu500', 'artist1000,artist2000')
    lista_noua = repo.get_all()
    assert len(lista_noua) == len(lista_veche) + 3

    melodie1 = Melodie('titlu1', 'artist9000', 'alt_gen', '13.12.2021')
    melodie2 = Melodie('titlu1', 'artist90000', 'Jazz', '13.13.2021')
    try:
        service.modificare_melodie('titlu1','artist9000',  'alt_gen', '13.12.2021')
        assert False
    except Exception:
        assert True

    try:
        service.modificare_melodie('titlu1', 'artist90000', 'Jazz', '13.12.2021')
        assert False
    except Exception:
        assert True

    repo2 = FileRepoMelodie('melodii_de_test.txt')
    service2 = ServiceMelodie(validator, repo2)
    service2.export_melodii('fisier_de_export.txt')


if __name__ == '__main__':
    teste_service()

