
def test_is_integer(test_item):
    """
        Function to test if an inputted item is an integer or not
        Args: test_item (any type from list)
        Output: (boolean) true if an integer or false if not 
    """
    try:
        int(test_item)
        return True
    except:
        return False

def square_of_odds(integers_input):
    # ensure that input is a List as expected
    if type(integers_input) is not list:
        return {"status": False, "error": "Input is not a list"}
    # create a new list of only integers in the provided list
    # and check if the length of the inout list matches this
    # if it does not match it means there were non integers in the list
    # and thus invalid input
    checked_list = [x for x in integers_input if test_is_integer(x)]
    if len(checked_list) != len(integers_input):
        return {"status": False, "error": "List does not contain only integers"}
    else:
        odds_list = [x for x in integers_input if x % 2 != 0]
        if len(odds_list) < 1:
            return {"status": False, "error": "List does not contain any odd numbers"}
        else:
            total = 0
            for item in odds_list:
                total = total + item**2
            return {"status": True, "data": total}
