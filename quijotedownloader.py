'''
This module is created to download the
entire series of books from Cervantes
calle "El Quijote de La Mancha"
'''

from os import getcwd
from os.path import join
from os.path import exists
from urllib import request

target_folder = getcwd()
'''
This string represents the
target directory where the
book is downloaded
'''

QUIJOTE_FILE = 'el_quijote.txt'
'''
String that represents
the file's name where the
entire quijote books is
stored
'''

QUIJOTE_URL = 'https://gist.githubusercontent.com/jsdario/6d6c69398cb0c73111e49f1218960f79/raw/8d4fc4548d437e2a7203a5aeeace5477f598827d/el_quijote.txt'
'''
URL to get the quijote
'''

quijote_path = join(target_folder, QUIJOTE_FILE)
'''
The file system path
where the books are stored
'''

def is_there_quijote():
    '''
    True is there a file
    on the quijote_path
    '''
    return exists(quijote_path)

def downloaded_quijote():
    '''
    Download the quijote
    as plain text
    '''
    if is_there_quijote():
        return
    request.urlretrieve(QUIJOTE_URL, quijote_path)


def get_quijote():
    """
    Returns an string that represents
    all the words on the quijote books

    :param int numCharacters: The number of chararcters
    to be readed
    """
    downloaded_quijote();

    with open(quijote_path, 'r', encoding='utf-8') as f:
        text = f.read()
        return text
