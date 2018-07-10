# Poem-Generator
Poem generator using Markov Models.
1. Read a text file which is the dataset of poems i.e the training data and convert it into a bigram representation.
2. Model as a second order Markov process: Create a probabilistic model.
3. Use the learned model to generate poem.

# Typical Paradigms of Operations
1. Reading the poems and forming a dictionary where key is the (word1,word2) and value is word3.
2. Calculating scores for the word3 i.e. (word1,word2) -> word3
3. Prediciting words from the model generated.

# Input
1. Text File of poems

# Output
1. Text File of generated Poem
