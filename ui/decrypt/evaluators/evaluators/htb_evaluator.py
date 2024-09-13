

name = "HTB ASCII"

# Return score, any random string info required for replicating evaluation
def evaluator(bs):
    
    htb_string = "HTB{"
    encoded_string = htb_string.encode("ascii")   
    if encoded_string in bs:
        return (1, "ascii")

    # throw away decrypted data
    return None