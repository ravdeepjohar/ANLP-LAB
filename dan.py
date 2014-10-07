import string

def num_letters_per_word(transcript):
    """Total number of sentences
    """
    return sum(len(w.strip(string.punctuation)) for line in transcript for w in line.split()) / sum(len(line.split()) for line in transcript)
def num_sentences(transcript):
    """Number of words in each sentence
    """
    return len(transcript)

def num_nonword_sounds(transcript):
    """Number of tokens preceded with a =, implying an action like =laughs
    """
    return sum(w[0] == '=' for line in transcript for w in line.split())

FEATURES_DAN = [
        num_letters_per_word,
        num_sentences,
        num_nonword_sounds,
    ]


################################################################################


if __name__ == "__main__":
    from sys import argv, exit
    
    if len(argv) < 2:
        print('usage: python2 %s [*.cha]+' % argv[0])
        exit()

    csv = [ '#' + ','.join(f.__name__ for f in FEATURES_DAN) + ',Label' ]

    for cha in argv[1:]:
        lines      = open(cha, 'r').readlines()
        label      = lines[0].split()[-1]
        transcript = lines[1:]
        features   = [ f(transcript) for f in FEATURES_DAN ]
        csv.append( ','.join([ str(f) for f in features ] + [label]) )

    with open('features_dan.csv', 'w') as fout:
        fout.write( '\n'.join(csv) + '\n' )
