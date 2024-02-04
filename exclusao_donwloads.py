from glob import glob
import os
from datetime import datetime

arquivos = glob(r'C:\Users\david\Downloads\*.*', recursive=True)
data_inicio = datetime.now()
for arquivo in arquivos:
    epoch = os.path.getatime(arquivo)
    data = datetime.fromtimestamp(epoch)
    tempo_arquivado = datetime.now() - data
    if tempo_arquivado.days > 90:
        os.remove(arquivo)
    else:
        pass

data_fim = datetime.now()

with open('hist.txt', 'a', encoding='UTF-8') as arquivo:
    arquivo.write(f'{data_inicio}|{data_fim}\n')