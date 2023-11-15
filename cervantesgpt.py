'''
Analize tex to genereate a GPT
able to generate text similar 
to want Cervantes wrote
'''


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
    '''
    def __init__(self, text) -> None:
        chars = sorted(list(set(text)))
        self.chars = chars
        self.vocab_size = len(chars)

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
