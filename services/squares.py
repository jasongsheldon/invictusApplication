from nameko.rpc import rpc

class SquaresService:
    name = "squares_service"

    def test_is_integer(self, test_item):
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

    @rpc
    def square_of_odds(self, integers_input):
        """
           Function to receive a List of integers and output the sum of the squares of the
           odd numbers
           Args: integers_input (List)
           Output: (dict) status: True or False and data: the sum of square of odds
           if successful or error if False with error reason
        """

        # ensure that input is a List as expected
        if type(integers_input) is not list:
            return {"status": False, "error": "Input is not a list"}

        # create a new list of only integers in the provided list
        # and check if the length of the inout list matches this
        # if it does not match it means there were non integers in the list
        # and thus invalid input
        checked_list = [x for x in integers_input if self.test_is_integer(x)]
        if len(checked_list) != len(integers_input):
            return {"status": False, "error": "List does not contain only integers"}
        else:
            # generate new list of only odds
            odds_list = [x for x in integers_input if x % 2 != 0]
            if len(odds_list) < 1:
                # if there are no odds in list its bad data ie no odds to sum
                return {"status": False, "error": "List does not contain any odd numbers"}
            else:
                total = 0
                for item in odds_list:
                    total = total + item**2
                return {"status": True, "data": total}
