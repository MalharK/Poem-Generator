import string
from random import randint

training_data_file = 'poems.txt'
store_words = []
transitions = {}
LINE_END_WORD = "line_end_word$%^"
POEM_START_WORD = "poem_start_word$%^"
POEM_END_WORD = "poem_end_word$%^"


def remove_punctuation(sentence):
    return sentence.translate(str.maketrans('', '', string.punctuation))


def train_model():
    p_p_word = POEM_START_WORD
    p_word = LINE_END_WORD
    for line in open(training_data_file):
        tokens = remove_punctuation(line.rstrip().lower()).split()
        if len(tokens) == 0:
            add_to_transitions((p_p_word, p_word), POEM_END_WORD)
            p_p_word = POEM_START_WORD
            p_word = LINE_END_WORD
        else:
            tokens.append(LINE_END_WORD)
            for token in tokens:
                add_to_transitions((p_p_word, p_word), token)
                p_p_word = p_word
                p_word = token


def add_to_transitions(bigram_tuple, token):
    if bigram_tuple in transitions:
        if token in transitions[bigram_tuple]:
            transitions[bigram_tuple][token] = transitions[bigram_tuple][token] + 1
        else:
            transitions[bigram_tuple][token] = 1
    else:
        transitions[bigram_tuple] = {}
        transitions[bigram_tuple][token] = 1


def next_word_by_probab(dictionary):
    cumulative = 0
    for key, value in dictionary.items():
        cumulative += value
    p = randint(0, cumulative)
    cumulative = 0
    for key, value in dictionary.items():
        cumulative += value
        if p <= cumulative:
            return key


def generate_poem():
    f = open("generated_poem.txt", "w")

    word0 = POEM_START_WORD
    word1 = LINE_END_WORD

    while True:
        word2 = next_word_by_probab(transitions[(word0, word1)])
        if word2 == POEM_END_WORD:
            f.close()
            break
        if word2 == LINE_END_WORD:
            f.write("\n")
        else:
            f.write(word2 + " ")
        word0 = word1
        word1 = word2


train_model()
generate_poem()

# print(store_notes)
