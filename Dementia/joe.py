FILLED = 'um uh uhhuh mm hmm hmhmm'.split()

def num_filled_pauses(transcript):
    """Number of filled pauses (e.g. um, uh, er, hmm, etc.)
    """
    return sum( w in FILLED for line in transcript for w in line.split() )
