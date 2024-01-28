from glob import glob
import os
from datetime import datetime

arquivos = glob(r'C:\Users\david\Downloads\*.*', recursive=True)

for arquivo in arquivos:
    epoch = os.path.getatime(arquivo)
    data = datetime.fromtimestamp(epoch)
    tempo_arquivado = datetime.now() - data
    if tempo_arquivado.days > 90:
        os.remove(arquivo)
    else:
        pass