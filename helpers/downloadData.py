from zipfile import ZipFile
import requests
import pathlib
import os


def obtainData():

    rootDir = pathlib.Path.cwd()  # Obtemos o diretório principal do programa

    # Obtemos o diretório onde os dados serão baixados
    resourcesDir = rootDir.joinpath('resources')

    databasePath = resourcesDir.joinpath('DadosMegasena.html')
    # Endereço do arquivo compactado com os dados
    url = "http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbwMPI0sDBxNXAOMwrzCjA0sjIEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wNnUwNHfxcnSwBgIDUyhCvA5EawAjxsKckMjDDI9FQE-F4ca/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0K8DBC0QPVN93KQ10G1/res/id=historicoHTML/c=cacheLevelPage/=/"

    try:
        response = requests.get(url)  # Objeto obtido do request

    except Exception as erro:
        print("\nHouve um problema para baixar os dados:\n", erro)

    else:

        return response
