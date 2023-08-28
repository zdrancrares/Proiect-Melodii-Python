from sortari.merge_sort import comapara_date


class ValidatorMelodie:

    def validate(self, m):
        """
        Valideaza obiect de tip Melodie
        :param m: obiectul de validat
        :type m: Melodie
        :raises: ValueError daca se intalnesc probleme la validarea melodiei
        """
        errors = []
        data = m.getDataAparitie()

        if not comapara_date(data, '03.02.2023'):
            raise ValueError('Data aceasta nu exista.')

        parts = data.split('.')
        zi = parts[0]
        luna = parts[1]
        an = parts[2]

        try:
            int(zi)
            int(luna)
            int(an)
        except Exception:
            raise ValueError('Ziua, luna si anul trebuie sa fie numere intregi')

        luni_cu_31_zile = ['01', '03', '05', '07', '08', '10', '12']
        luni_cu_30_zile = ['04', '06', '09', '11']
        luni_cu_28_zile = ['02']

        if luna in luni_cu_28_zile:
            if not (1 <= int(zi) <= 28):
                errors.append('Luna februarie trebuie sa aibe maxim 28 de zile.')
        if luna in luni_cu_30_zile:
            if not (1 <= int(zi) <= 30):
                errors.append('Aceasta luna trebuie sa aibe maxim 30 de zile.')
        if luna in luni_cu_31_zile:
            if not (1 <= int(zi) <= 31):
                errors.append('Aceasta luna trebuie sa aibe maxim 31 de zile.')
        zi = int(zi)
        luna = int(luna)
        an = int(an)
        if not (1 <= zi <= 31):
            errors.append('Ziua trebuie sa fie un numar intreg intre 1 si 31.')
        if not (1 <= luna <= 12):
            errors.append('Luna trebuie sa fie un numar intreg intre 1 si 12.')
        if not (0 <= an <= 2023):
            errors.append('Anul trebuie sa fie un numar intreg intre 0 si 2023.')

        lista_genuri = ['Rock', 'Pop', 'Jazz']
        if m.getGen() not in lista_genuri:
            errors.append('Genul trebuie sa fie unul dintre: Rock, Pop sau Jazz.')
        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)



