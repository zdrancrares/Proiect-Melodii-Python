from domain.melodie_validator import ValidatorMelodie
from prezentare.consola import Consola
from repository.repo_melodie import FileRepoMelodie
from service.service_melodie import ServiceMelodie

repo = FileRepoMelodie('C:\\Users\\dorin\\PycharmProjects\\examenFP_03_02\\data\\melodie.txt')
validator = ValidatorMelodie()
service = ServiceMelodie(validator, repo)

c = Consola(service)
c.run_melodii_ui()
