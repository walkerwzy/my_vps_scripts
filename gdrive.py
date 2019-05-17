#!/usr/bin/env python3
import requests
from tqdm import tqdm
import re
import os

def download_file_from_google_drive(id, destination):
    URL = 'https://docs.google.com/uc?export=download'
    destination = '/site/'+destination
    session = requests.Session()
    response = session.get(URL, params = { 'id' : id }, stream = True)

    token = None
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            token = value
            break

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    CHUNK_SIZE = 32*1024
    # TODO: this doesn't seem to work; there's no Content-Length value in header?
    total_size = int(response.headers.get('content-length', 0))

    with tqdm(desc=destination, total=total_size, unit='B', unit_scale=True) as pbar:
        with open(destination, 'wb') as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk:
                    pbar.update(CHUNK_SIZE)
                    f.write(chunk)


if __name__ == '__main__':
    import sys
    if len(sys.argv) is not 3:
        executable = os.path.basename(sys.argv[0])
        print('Usage: [python] %s {DRIVE_FILE_ID_OR_URL} {DESTINATION_FILE_PATH}' % executable)
    else:
        # TAKE ID FROM SHAREABLE LINK
        if sys.argv[1].startswith('https://'):
            file_id = re.search(r'[?&]id=([a-zA-Z0-9_-]+)', sys.argv[1]).group(1)
        else:
            file_id = sys.argv[1]

        # DESTINATION FILE ON YOUR DISK
        destination = sys.argv[2]
        download_file_from_google_drive(file_id, destination) 
