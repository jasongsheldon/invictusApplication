from nameko.standalone.rpc import ClusterRpcProxy

config = {
    'AMQP_URI': "pyamqp://guest:guest@localhost"
}


def test_islist():
    """Test that will not break if it is not a list"""
    with ClusterRpcProxy(config) as cluster_rpc:
        assert cluster_rpc.compress_service.compress({'a': 3}).get('status') == False


def test_invalid_data():
    """Test to see if there is invalid (non string) data in the list
    """
    with ClusterRpcProxy(config) as cluster_rpc:
        assert cluster_rpc.compress_service.compress([1,'dog','cat','hamster']).get('status') == False


def test_compress_as_expected():
    """Positive test to see that the correct dict data is output from compress"""
    with ClusterRpcProxy(config) as cluster_rpc:
        assert cluster_rpc.compress_service.compress(['dog', 'cat', 'hamster']).get('data') == {'dog': '¸ñ', 'cat': '¶µ', 'hamster': 'í\x7f\x8de*'}


def test_decode():
    """Positive test to see that it decodes as expected"""
    with ClusterRpcProxy(config) as cluster_rpc:
        assert cluster_rpc.compress_service.decode('¸ñ') == 'dog'
