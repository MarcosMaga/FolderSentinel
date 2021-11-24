from time import sleep
from datetime import datetime
import os

local = './'

def EscreverLog(file, text):
    f = open(file, 'a')
    f.writelines(text+ '\n')
    f.close()
    
def Convert(val):
    acm = ['B', 'KB', 'MB', 'GB', 'TB']
    count = 0
    while val > 1024:
        val /= 1024
        count += 1
    return '{:.1f}{}'.format(val, acm[count])


class Arch:
    def __init__(self, name, size, dir):
        self.name = name
        self.size = size
        self.dir = dir

atualArch = []

for diretorio, subpastas, arquivos in os.walk(local):
        for arquivo in arquivos:
            atualArch.append(Arch(arquivo, os.path.getsize(os.path.join(diretorio,arquivo)), diretorio))

while True:
    for diretorio, subpastas, arquivos in os.walk(local):
        for arquivo in arquivos:
            error = 0
            for j in range(len(atualArch)):
                if arquivo == atualArch[j].name:
                    error += 1
            if error == 0:
                if os.path.exists(os.path.join(diretorio,arquivo)) and arquivo != 'log.txt':
                    atualArch.append(Arch(arquivo, os.path.getsize(os.path.join(diretorio,arquivo)), diretorio))
    
    for i in range(len(atualArch)):
        try:
            if not os.path.exists(os.path.join(atualArch[i].dir, atualArch[i].name)):
                EscreverLog(local + 'log.txt', '{} - O arquivo \'{}\' foi removido. Peso: {}'.format(datetime.today().strftime('%d/%m/%Y %H:%M'),atualArch[i].name, Convert(atualArch[i].size)))
                print('O arquivo {} foi removido.'.format(atualArch[i].name))
                del atualArch[i]
        except:
            pass
    sleep(1)
    newArch = []

    for diretorio, subpastas, arquivos in os.walk(local):
        for arquivo in arquivos:
            if arquivo != 'log.txt':
                newArch.append(Arch(arquivo, os.path.getsize(os.path.join(diretorio,arquivo)), diretorio))

    for i in range(len(newArch)):
        error = 0
        for j in range(len(atualArch)):
            if newArch[i].name == atualArch[j].name:
                if newArch[i].size != atualArch[j].size:
                    EscreverLog(local + 'log.txt', '{} - O arquivo \'{}\' foi modificado. {} >>> {}'.format(datetime.today().strftime('%d/%m/%Y %H:%M'),newArch[i].name, Convert(atualArch[j].size), Convert(newArch[i].size)))
                    print('O arquivo {} foi modificado.'.format(newArch[i].name))
                    atualArch[j].size = newArch[i].size
                error += 1
        if error == 0:
            atualArch.append(Arch(newArch[i].name, newArch[i].size, newArch[i].dir))
            EscreverLog(local + 'log.txt', '{} - O arquivo \'{}\' foi adicionado. Peso: {}'.format(datetime.today().strftime('%d/%m/%Y %H:%M'),newArch[i].name, Convert(newArch[i].size)))
            print('O arquivo {} foi adicionado.'.format(newArch[i].name))




            
   


                
    
            

