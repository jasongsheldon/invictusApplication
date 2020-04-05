from nameko.standalone.rpc import ClusterRpcProxy

config = {
    'AMQP_URI': "pyamqp://guest:guest@localhost"
}

with ClusterRpcProxy(config) as cluster_rpc:
    response = cluster_rpc.compress_service.compress(['dog','cat','hamster'])
    print(response)
    if response.get('status') == True:
        for key in response.get('data').keys():
            compressed = response.get('data')[key]
            decoded = cluster_rpc.compress_service.decode(compressed)
            print('for key {}: compressed: {} and decoded:{}\n'.format(key,compressed,decoded))
