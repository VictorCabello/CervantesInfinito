"""
The intention of this module is
to create GPT implementation
using all the Quijote as dataset
"""
from quijotedownloader import get_quijote
from cervantesgpt import get_char_universe

def main():
    """
    This funciton has the main flow
    of te program
    """
    text = get_quijote()
    universe = get_char_universe(text)
    encoded = universe.encode('hi there')
    print(encoded)
    print(universe.decode(encoded))

if __name__ == '__main__':
    main()
