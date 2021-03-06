from nameko.standalone.rpc import ClusterRpcProxy

config = {
    'AMQP_URI': "pyamqp://guest:guest@rabbitmq"
}


def test_islist():
    """Test that will not break if it is not a list"""
    with ClusterRpcProxy(config) as cluster_rpc:
        assert cluster_rpc.squares_service.square_of_odds({'a': 3}).get('status') == False


def test_invalid_data():
    """Test to see if there is invalid (non integer) data in the list
    """
    with ClusterRpcProxy(config) as cluster_rpc:
        assert cluster_rpc.squares_service.square_of_odds([1,2,3,'a']).get('status') == False


def test_none_odd():
    """Test to see if there are any odd numbers in the list as we are summing odd numbers
       so if are none its bad data
    """
    with ClusterRpcProxy(config) as cluster_rpc:
        assert cluster_rpc.squares_service.square_of_odds([2,4,6,8]).get('status') == False


def test_as_expected():
    """Positive test to see that the correct sum of squares for valid data is returned"""
    with ClusterRpcProxy(config) as cluster_rpc:
        assert cluster_rpc.squares_service.square_of_odds([1, 3, 12, 13, 14, 19, 20]).get('data') == 540
