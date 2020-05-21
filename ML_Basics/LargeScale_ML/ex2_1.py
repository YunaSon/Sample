import requests, io, os
import numpy as np
import tarfile, zipfile, gzip

def unzip_from(UCI_url, dest=''):
    """
    UCI의 데이터셋을 zip포맷으로 다운로드 한 뒤 압축을 푼다. 
    """
    response = requests.get(UCI_url)
    compressed_file = io.BytesIO(response.content)
    z = zipfile.ZipFile(compressed_file)
    print("Extracting in {}".format(os.getcwd())+ '\'+ dest)
    for name in z.namelist():
        if '.csv' in name:
            print('\tunzipping {}'.format(name))
            z.extract(name, path=os.getcwd()+'\'+dest)