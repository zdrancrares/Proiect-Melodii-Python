class Consola:

    def __init__(self, service):
        """
        Initializeaza obiect de tip Consola cu service
        :param service: service cu care lucreaza consola
        :type service: ServiceMelodie
        """
        self.__service = service

    def _print_menu(self):
        print("Introduceti una dintre optiunile: modificare_melodie, generare_melodii, export_melodii, exit")

    def _modificare_melodie(self):
        titlu = input('Introduceti titlul melodiei de modificat: ')
        artist = input('Introduceti artistul melodiei de modificat: ')
        gen = input('Introduceti noul gen pentru melodie: ')
        data = input('Introduceti noua data pentru melodie(dd.MM.yyyy): ')
        try:
            self.__service.modificare_melodie(titlu, artist, gen, data)
            print(f"Melodia {titlu}({artist}) a fost modificata cu succes!")
        except Exception as e:
            print(e)
            return

    def _generare_melodii(self):
        numar_melodii = input("Introduceti numarul de melodii de generat: ")
        try:
            numar_melodii = int(numar_melodii)
        except Exception:
            print("Numarul de melodii trebuie sa fie un numar intreg >= 0.")
            return
        lista_titluri = input("Introduceti lista cu titluri de generat(separate prin virgula): ")
        lista_artisti = input("Introduceti lista cu artisti de generat(separate prin virgula): ")
        self.__service.genereaza_aleator(numar_melodii, lista_titluri, lista_artisti)
        print(f"Au fost adaugate {numar_melodii} melodii.")

    def _export_melodii(self):
        nume_fisier = input("Introduceti numele fisierului text in care doriti sa exportati melodiile: ")
        self.__service.export_melodii(nume_fisier)

    def run_melodii_ui(self):
        while True:
            self._print_menu()
            option = input("Optiunea dvs: ")
            if option == 'modificare_melodie':
                self._modificare_melodie()
            elif option == 'generare_melodii':
                self._generare_melodii()
            elif option == 'export_melodii':
                self._export_melodii()
            elif option == 'exit':
                exit()
            else:
                print("Nu ati introdus o optiune valida.")