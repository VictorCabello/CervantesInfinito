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

    inputs, targets = universe.get_batch()

    print('Inputs:')
    print(inputs.shape)
    print(inputs)
    print('Targets:')
    print(targets.shape)
    print(targets)

    for b in range(universe.batch_size):
        for t in range(universe.block_size):
            myInput = inputs[b,:t+1]
            target = targets[b, t]
            print(f"When the input is {myInput} the target: {target}")

if __name__ == '__main__':
    main()
