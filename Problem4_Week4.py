def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this functio
    i=0
    a = hand.values()
    for val in a:
    	if val != 0:
    		i+=val
    return i
