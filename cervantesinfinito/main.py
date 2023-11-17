"""
The intention of this module is
to create GPT implementation
using all the Quijote as dataset
"""
from quijotedownloader import get_quijote
from cervantesgpt import get_char_universe, BiframLanguageModel

def main():
    """
    This funciton has the main flow
    of te program
    """
    text = get_quijote()
    universe = get_char_universe(text)
    inputs, targets = universe.get_batch()
    model = BiframLanguageModel(universe.vocab_size)
    out = model(inputs, targets)
    print(out.shape)


if __name__ == '__main__':
    main()
