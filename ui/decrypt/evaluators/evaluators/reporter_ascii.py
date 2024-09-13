

name = "Reporter WebApp ASCII"

# Return score, any random string info required for replicating evaluation
def evaluator(bs):

    target = "U1337"
    
    encoded_string = target.encode("ascii")   

    if encoded_string in bs:
        return (sum([ 
            1 for b in bs if b >= 0x20 and b <= 0x7E 
        ])/len(bs), "ascii")

    # throw away decrypted data
    return None