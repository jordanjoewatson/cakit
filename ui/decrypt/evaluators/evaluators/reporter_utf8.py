

name = "U1337 WebApp UTF8"

# Return score, any random string info required for replicating evaluation
def evaluator(bs):

    target = "U1337"
    
    encoded_string = target.encode("utf-8")   

    if encoded_string in bs:
        return (sum([ 
            1 for b in bs if b >= 0x20 and b <= 0x7E 
        ])/len(bs), "utf-8")

    # throw away decrypted data
    return None