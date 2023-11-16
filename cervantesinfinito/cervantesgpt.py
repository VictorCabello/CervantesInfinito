'''
Analize tex to genereate a GPT
able to generate text similar 
to want Cervantes wrote
'''

import torch

class CharacterUniverse:
    '''
    A class used to reperesents all 
    the characters prenests on a text

    Attributes
    ----------
    chars : list
        a list of all the unique characters that occurs on the text
    vocab_size : int
        total number of the unique characters that occurs on the text
    str_to_int : Map
        used to encode str to int
    int_to_str : Map
        used to decode str to int
    text : The Cervantes full text
        used to decode str to int
    '''
    def __init__(self, text) -> None:
        self.text = text
        chars = sorted(list(set(text)))
        self.chars = chars
        self.vocab_size = len(chars)
        self.str_to_int = {}
        self.int_to_str = {}
        self.initTranformatinUtils()

    def initTranformatinUtils(self) -> None:
        '''
        Initilizez maps used to enumerate/decode
        '''
        for i, ch in enumerate(self.chars):
            self.str_to_int[ch] = i
            self.int_to_str[i] = ch

    def encode(self, text) -> list[int]:
        '''
        Transform text into an array of int_to_str

        Returns
        -------
        list[int]
            A representation of the text as int array
        '''
        return [self.str_to_int[ch] for ch in text]

    def decode(self, array) -> str:
        '''
        Transform an arry of int to str
        '''
        return ''.join([self.int_to_str[i] for i in array])

    @property
    def tensor(self):
        '''
        Create a tensor with the characeters of the 
        universe.
        '''
        return torch.tensor(self.encode(self.text), dtype=torch.long)

    def __str__(self) -> str:
        '''
        Get an string representation of this object

        Returns
        -------
        str
            a human readable representation of this object
        '''
        template = f"""
        CharacterUniverse (
            chars: {''.join(self.chars)},
            vocab_size: {self.vocab_size}
        )
        """

        return template

def get_char_universe(text) -> CharacterUniverse:
    '''
    Get the unique characters on the text and the amount of them

    Parameters
    ----------
    text : str
        All the text that we want to analize

    Returns
    -------
    CharacterUniverse
        an object that contiains in its properties
        the list of all unique characters and the total of them
    '''
    return CharacterUniverse(text)
