from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

import requests as re
import os
import myClass as mc


def main(param: mc.Param):
    if not checkFolder(param.path):
        print('[CREANDO] {0}'.format(param.path))
        os.mkdir(param.path)
    else:
        print('[YA EXISTE] {0}'.format(param.path))
    print('====== Descargando archivos ======')
    download(param)
    print('============== DONE ==============')
    os.system('pause')


def checkFolder(path: mc.Param.path):
    return os.path.isdir(path)


def checkFile(file: str):
    return os.path.isfile(file)


def replace():
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


def download(param: mc.Param):
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
                print('[REMPLAZANDO] {0}'.format(name))
                req = re.get(str(i), allow_redirects=True)
                with open(fullName, 'wb') as file:
                    file.write(req.content)
            else:
                print('[NUEVO] {0}'.format(name))
                req = re.get(str(i), allow_redirects=True)
                with open(fullName, 'wb') as file:
                    file.write(req.content)
        else:
            if checkFile(fullName):
                print('[YA EXISTE] {0}'.format(name))
            else:
                print('[NUEVO] {0}'.format(name))
                req = re.get(str(i), allow_redirects=True)
                with open(fullName, 'wb') as file:
                    file.write(req.content)
