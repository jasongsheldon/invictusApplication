from nameko.standalone.rpc import ClusterRpcProxy

config = {
    'AMQP_URI': "pyamqp://guest:guest@localhost"
}

with ClusterRpcProxy(config) as cluster_rpc:
    print(cluster_rpc.squares_service.square_of_odds([0,1,3,6,5]))
