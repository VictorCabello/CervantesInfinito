"""
The intention of this module is
to create GPT implementation
using all the Quijote as dataset
"""
from quijotedownloader import get_quijote
from cervantesgpt import get_char_universe, BiframLanguageModel
import torch 

def main():
    """
    This funciton has the main flow
    of te program
    """
    text = get_quijote()
    universe = get_char_universe(text)
    inputs, targets = universe.get_batch()
    model = BiframLanguageModel(universe.vocab_size)
    predictions, loss = model(inputs, targets)
    print(predictions.shape)
    print(loss)

    empty_inputs = torch.zeros((1, 1), dtype=torch.long)
    generated_outpt = model.generate(empty_inputs, max_new_tokens=100)
    decoded_sample = universe.decode(generated_outpt[0].tolist())
    print(decoded_sample)


if __name__ == '__main__':
    main()
