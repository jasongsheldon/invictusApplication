import argparse
from nameko.standalone.rpc import ClusterRpcProxy

config = {
    'AMQP_URI': "pyamqp://guest:guest@rabbitmq"
}

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument command
parser.add_argument("--cmd", help="choose a service command: 'squares', 'compress' or 'decode' are valid values", required=True)
parser.add_argument("--data", help="data for the command selected: for squares list of integers eg 1,2,3, for compress list of words eg 'cat','dog','hamster', for decode the compressed word to decode", required=True)

# Read arguments from the command line
args = parser.parse_args()

# Check for --cmd
if not args.cmd:
    print("--cmd is required")
else:
    print("command: %s" % args.cmd)
    if args.cmd == "squares" or args.cmd == "compress" or args.cmd == "decode":
        if not args.data:
            print("--data is required")
        else:
            with ClusterRpcProxy(config) as cluster_rpc:
                print("data: %s" % args.data)
                if args.cmd == "squares":
                    try:
                        input_data = [int(x) for x in args.data.split(',')]
                    except ValueError:
                        input_data = [x for x in args.data.split(',')]
                    result = cluster_rpc.squares_service.square_of_odds(input_data)
                    if result.get('status'):
                        print("output: %d" % result.get('data'))
                    else:
                        print("error: %s" % result.get('error'))
                elif args.cmd == "compress":
                    input_data = [x for x in args.data.split(',')]
                    result = cluster_rpc.compress_service.compress(input_data)
                    if result.get('status'):
                        print("output: %s" % result.get('data'))
                    else:
                        print("error: %s" % result.get('error'))
                elif args.cmd == "decode":
                    input_data = args.data
                    result = cluster_rpc.compress_service.decode(input_data)
                    if result.get('status'):
                        print("output: %s" % result.get('data'))
                    else:
                        print("error: %s" % result.get('error'))
                else:
                    print('unknown command but should never get here')
    else:
        print("%s invalid command: valid commands are 'squares', 'compress' or 'decode'" % args.cmd)
