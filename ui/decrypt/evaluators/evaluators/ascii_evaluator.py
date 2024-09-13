

name = "ASCII"

# Return score, any random string info required for replicating evaluation
def evaluator(bs):

    ascii_bs = [ 
        b for b in bs if b >= 0x20 and b <= 0x7E 
    ]

    # 0x20 to 0x7E
    return len(ascii_bs)/len(bs), ''.join([ chr(b) for b in ascii_bs ])