from compression import compress, decode

def test_islist():
    """Test that will not break if it is not a list"""
    assert compress({'a': 3}).get('status') == False

def test_invalid_data():
    """Test to see if there is invalid (non string) data in the list
    """
    assert compress([1,'dog','cat','hamster']).get('status') == False

def test_compress_as_expected():
    """Positive test to see that the correct dict data is output from compress"""
    assert compress(['dog','cat','hamster']).get('data') == {'dog': b'\xb8\xf1', 'cat': b'\xb6\xb5', 'hamster': b'\xed\x7f\x8de*'}

def test_decode():
    """Positive test to see that it decodes as expected"""
    assert decode(b'\xb8\xf1') == 'dog'
