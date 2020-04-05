from dahuffman import HuffmanCodec

def get_codec():
    """Generate the codec for encoding and decoding based on random sentence
       Args: None
       Returns: the codec
    """
    codec = HuffmanCodec.from_data("the quick brown fox jumps over the lazy dog")
    return codec

def encode(word):
    """return Huffman encoded binary for a given word
       Args: word (String)
       Returns: (binary string) encoded representation
    """
    return get_codec().encode(word)

def decode(compressed):
    """decodes a Huffman encoded binary string back into its original word
       Args: compressed (binary string) 
       Returns: (string) original word
    """
    return get_codec().decode(compressed)

def compress(list_input):
    """return a dict of original word as key and Huffman encoded equivalent for a given list
       Args: list_input (List): list of words to encode
       Returns: (dict) original word is key and encoded is value
    """
    # ensure that input is a List as expected
    if type(list_input) is not list:
        return {"status": False, "error": "Input is not a list"}
    # create a new list of only strings in the provided list
    # and check if the length of the input list matches this
    # if it does not match it means there were non strings in the list
    # and thus invalid input
    checked_list = [x for x in list_input if type(x) is str]
    if len(checked_list) != len(list_input):
        return {"status": False, "error": "List does not contain only strings"}
    else:
        dict_out = {}
        for word in list_input:
            dict_out[word] = encode(word)
        return {"status": True, "data": dict_out}
