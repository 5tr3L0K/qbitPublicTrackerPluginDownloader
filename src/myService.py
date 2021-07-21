from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

import requests as re
import os
import myClass as mc


# proceso principal
def main(param: mc.Param):
    proc = 'P001'
    try:
        if not checkFolder(param.path):
            print('[CREANDO] {0}'.format(param.path))
            os.mkdir(param.path)
        else:
            print('[YA EXISTE] {0}'.format(param.path))
        print('====== Descargando archivos ======')
        download(param)
        print('============== DONE ==============')
        os.system('pause')
    except Exception as e:
        print('Error en: {0}'.format(proc))
        print(e)


# checkea si existe la carpeta de descarga
def checkFolder(path: mc.Param.path):
    proc = 'P002'
    try:    
        return os.path.isdir(path)
    except Exception as e:
        print('Error en: {0}'.format(proc))
        raise e


# checkea si el archivo existe o no
def checkFile(file: str):
    proc = 'P003'
    try:
        return os.path.isfile(file)
    except Exception as e:
        print('Error en: {0}'.format(proc))
        raise e


# consulta si se desea remplazar arhivos o no
def replace():
    proc = 'P004'
    try:
        rta = ''
        while rta not in ('s', 'n'):
            print('¿Desea remplazar los archivos en caso de que ya existan? [s/n]')
            rta = input('=> ').lower()
            if rta not in ('s', 'n'):
                print('Por favor ingrese [s] o [n]...')
        if rta == 's':
            return True
        else:
            return False
    except Exception as e:
        print('Error en: {0}'.format(proc))
        raise e


# descarga un plugin y muestra el estado por pantalla
def downloadSub(message, link, name, fullName: str):
    proc = 'P006'
    try:
        print('[{1}] {0}'.format(name, message))
        req = re.get(str(link), allow_redirects=True)
        with open(fullName, 'wb') as file:
            file.write(req.content)
    except Exception as e:
        print('Error en: {0}'.format(proc))
        raise e


# proceso principal de descarga los plugins
def download(param: mc.Param):
    proc = 'P005'
    try:
        request = param.url
        html = urlopen(request)
        soup = BeautifulSoup(html, 'lxml')
        firstTable = soup.select_one("table:nth-of-type(1)")
        links = []
        rep = False

        for link in firstTable.findAll('a'):
            if str(link.get('href')[-3:]) == '.py':
                links.append(link.get('href'))
        
        rep = replace()

        for i in links:
            preName = str(i).split('/')
            name = preName[-1]
            fullName = '{0}/{1}'.format(param.path, name)

            if rep:
                if checkFile(fullName):
                    downloadSub('REMPLAZANDO', str(i), name, fullName)
                else:
                    downloadSub('NUEVO', str(i), name, fullName)
            else:
                if checkFile(fullName):
                    print('[YA EXISTE] {0}'.format(name))
                else:
                    downloadSub('NUEVO', str(i), name, fullName)
    except Exception as e:
        print('Error en: {0}'.format(proc))
        raise e
