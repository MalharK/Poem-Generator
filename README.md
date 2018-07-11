# Poem-Generator
Generate poems (or music or rap) using Markov Models.
Smartly handles line breaks and auto ending.

### Setup

    #create (python3) virtualenvironment and activate
    pip install -r requirements.txt
    python generator.py

> Generates a poem based on data from poems.txt in generated_poem.txt
> Can replace source file to music or rap.

Music can be played on [Virtual Piano](https://virtualpiano.net/)


### Working

1. Reads the dataset of poems i.e the training data and converts it into a bigram representation i.e. `(word1, word2) -> word3`
2. Adds entries for line-break and poem ending to support auto line break and poem endings.
3. Model as a second order Markov process: Create a probabilistic model.
4. Use the learned model to generate poems.
