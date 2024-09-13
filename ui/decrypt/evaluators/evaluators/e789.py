

name = "e789"

# Return score, any random string info required for replicating evaluation
def evaluator(bs):

    target = "7899"
    for encode in ['utf-8', 'ascii']:
    	encoded_string = target.encode(encode)   
	
    	if encoded_string in bs:
        	return (1, encoded_string)

    return None
