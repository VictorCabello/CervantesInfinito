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

    block_size = 8

    tranformer_input = universe.train_data[:block_size]
    next_tarnformer_input = universe.train_data[1:block_size + 1]

    for t in range(block_size):
        input = tranformer_input[:t+1]
        target = next_tarnformer_input[t]
        print(f"When the input is {input} the target: {target}")

if __name__ == '__main__':
    main()
