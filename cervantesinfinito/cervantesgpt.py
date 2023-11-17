'''
Analize tex to genereate a GPT
able to generate text similar 
to want Cervantes wrote
'''

from typing import Tuple
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
    tensor : torch.Tensor
        all the tokens generated by the text
    train_data : torch.Tensor
        Tokens used to train the model
    validation_data : torch.Tensor
        Tokens used to validate the model
    batch_size : int
        number of indepentent sequences will we process in parallel
    block_size : int
        Max context length for predictions
    '''
    def __init__(self, text) -> None:
        self.text = text
        chars = sorted(list(set(text)))
        self.chars = chars
        self.vocab_size = len(chars)
        self.str_to_int = {}
        self.int_to_str = {}
        self.initTranformatinUtils()
        self.tensor = torch.tensor(self.encode(self.text), dtype=torch.long)
        tranning_data_percentage = int( 0.9 * len(self.tensor) )
        self.train_data = self.tensor[:tranning_data_percentage]
        self.validation_data =  self.tensor[tranning_data_percentage:]
        self.batch_size = 4
        self.block_size = 32

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

    def get_batch(self, isTrainData=True) -> Tuple[torch.Tensor, torch.Tensor]:
        '''
        Generarte a small batch of data of inputs x and targets y

        Returns
        -------
        Tuple[Tensor, Tensor]
            A tuple wich first elment is a Tensor that repersents the inputs and
            the second element is a Tensor that reperesnts the targets
        '''
        data = self.train_data if isTrainData else self.validation_data
        ix = torch.randint(len(data) - self.block_size, (self.batch_size,))
        inputs = torch.stack([data[i:i + self.block_size] for i in ix])
        targets = torch.stack([data[i + 1:i + self.block_size + 1] for i in ix])
        return inputs, targets


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


class BiframLanguageModel(torch.nn.Module):
    '''
    Represents a nerral network to predict characters

    Attributes
    ----------
    token_embedding_table : torch.nn.Embedding
        Matrix with all the tokens used by the model
    '''

    def __init__(self, vocab_size) -> None:
        '''
        Initialize this Model creating a matrix for all
        its tokens
        '''
        super().__init__()
        self.token_embedding_table = torch.nn.Embedding(vocab_size, vocab_size)

    def forward(self, inputs, targets):
        '''
        This funciton is called every time the model is called and
        it returns the predictions and its loss.

        Parameters
        ----------
        input : Tensor (batch_size, block_size, vocab_size)
            used to generate the predictions
        targets : Tensor (batch_size, block_size, vocab_size)
            used to validate the loss of the predictions

        Returns
        -------
        '''
        predictions = self.token_embedding_table(inputs)

        return predictions
