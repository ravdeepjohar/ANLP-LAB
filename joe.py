FILLED     = 'um uh uhhuh mm hmm hmhmm'.split()
DICTIONARY = [ w.strip() for w in open('dictionary.txt', 'r') ]

def num_tokens(transcript):
    """Total number of word tokens
    """
    return sum(len(line.split()) for line in transcript)

def num_filled_pauses(transcript):
    """Number of filled pauses (e.g. um, uh, er, hmm, etc.)
    """
    return sum(w in FILLED for line in transcript for w in line.split())

def num_nondict_tokens(transcript):
    """Number of word tokens not found in CMU dictionary
    """
    return sum(w not in DICTIONARY for line in transcript for w in line.split())

FEATURES_JOE = [
        num_tokens,
        num_filled_pauses,
        num_nondict_tokens,
    ]


################################################################################


if __name__ == "__main__":
    from sys import argv, exit
    
    if len(argv) < 2:
        print 'usage: python2 %s [*.cha]+' % argv[0]
        exit()

    csv = [ '#' + ','.join(f.__name__ for f in FEATURES_JOE) + ',Label' ]

    for cha in argv[1:]:
        lines      = open(cha, 'r').readlines()
        label      = lines[0].split()[-1]
        transcript = lines[1:]
        features   = [ f(transcript) for f in FEATURES_JOE ]
        csv.append( ','.join([ str(f) for f in features ] + [label]) )

    with open('features_joe.csv', 'w') as fout:
        fout.write( '\n'.join(csv) + '\n' )
