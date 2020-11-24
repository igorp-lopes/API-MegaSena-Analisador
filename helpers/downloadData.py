from zipfile import ZipFile
import requests
import pathlib
import os


def obtainData():

    # We obtain the main directory of the program
    rootDir = pathlib.Path.cwd()

    # We obtain the directory where the data will be downloaded
    resourcesDir = rootDir.joinpath('resources')

    databasePath = resourcesDir.joinpath('DadosMegasena.html')

    # Website of the archive with the data
    url = "http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbwMPI0sDBxNXAOMwrzCjA0sjIEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wNnUwNHfxcnSwBgIDUyhCvA5EawAjxsKckMjDDI9FQE-F4ca/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0K8DBC0QPVN93KQ10G1/res/id=historicoHTML/c=cacheLevelPage/=/"

    try:
        # Object given by the request
        response = requests.get(url)

    except Exception as error:
        print("\n The following exception occurred when downloading the data:\n", error)

    else:

        return response
