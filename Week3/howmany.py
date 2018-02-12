def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    length =0
    for entry in aDict.values():
        length += len(entry)
    return length
