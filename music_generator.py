import string
from random import randint

training_data_file = 'music.txt'
store_notes = []
initial_word = {}
second_word = {}
transitions = {}
f = open("generated_music.txt", "w")


def remove_punctuation(sentence):
    return sentence.translate(str.maketrans('', '', string.punctuation))


def train_model():
    for line in open(training_data_file):
        tokens = remove_punctuation(line.rstrip().lower()).split()
        for i in range(len(tokens)):
            store_notes.append(tokens[i])
    i = 0
    for i in range(len(store_notes)):
        token = store_notes[i]
        if i == 0:
            initial_word[token] = initial_word.get(token, 0) + 1
        else:
            prev_token = store_notes[i - 1]
            if i == len(store_notes) - 1:
                add2dict(transitions, (prev_token, token), 'END')
            if i == 1:
                add2dict(second_word, prev_token, token)
            else:
                prev_prev_token = store_notes[i - 2]
                add2dict(transitions, (prev_prev_token, prev_token), token)

    # Normalize distributions:
    print(transitions)
    initial_chord_total = sum(initial_word.values())
    print(initial_chord_total)
    for key, value in initial_word.items():
        initial_word[key] = value / initial_chord_total
    for prev_word, next_word_list in second_word.items():
        second_word[prev_word] = list2probabilitydict(next_word_list)

    for word_pair, next_word_list in transitions.items():
        transitions[word_pair] = list2probabilitydict(next_word_list)


def add2dict(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = []
    dictionary[key].append(value)


def list2probabilitydict(given_list):
    probability_dict = {}
    given_list_length = len(given_list)
    for item in given_list:
        probability_dict[item] = probability_dict.get(item, 0) + 1
    for key, value in probability_dict.items():
        probability_dict[key] = value / given_list_length
    return probability_dict


def next_word_probab(dictionary):
    p = randint(0, 12) / 10
    cumalative = 0
    for key, value in dictionary.items():
        cumalative += value
        if p < cumalative:
            return key
    return key


def generate_poem():
    for i in range(10):
        sentence = []
        word0 = next_word_probab(initial_word)
        word1 = next_word_probab(second_word[word0])
        sentence.append(word0)
        sentence.append(word1)
        while True:
            word2 = next_word_probab(transitions[(word0, word1)])
            if word2 == 'END':
                break
            sentence.append(word2)
            word0 = word1
            word1 = word2
        f.write(' '.join(sentence))
        f.write('\n')
        print(' '.join(sentence))
    f.close()


train_model()
print(transitions)
generate_poem()

# print(store_notes)
