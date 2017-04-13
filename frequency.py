""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    remover = str.maketrans('','',string.punctuation)
    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('THE RAVEN.') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]
    lines = [e for e in [rem_punc.translate(remover) for rem_punc in [line[:-1] for line in lines]] if e != "Illustration"]
    words = ' '.join(str(l) for l in lines)
    return words.split()

def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    word_number_dict = {}
    for word in word_list:
        try:
            word_number_dict[word] += 1
        except KeyError:
            word_number_dict[word] = 1
    return list(reversed(([w[0] for w in sorted(word_number_dict.items(), key=lambda item: item[1])])))[:n]

if __name__ == "__main__":
    print(get_top_n_words(get_word_list('book.txt'), 100))
