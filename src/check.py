import argparse

# Use init_args to setup the arguments
def init_args(parser):
    # Add arguments
    parser.add_argument('-n', nargs='+')
    parser.add_argument('args', nargs='*')

    # parse = 
    return parser.parse_args(['-f'])

def main():
    # Parser setup
    parser = argparse.ArgumentParser(prog='PROG')

    # Parsing the arguments in the parser object
    args = init_args(parser)

    # Selection of argument action used, to call the right function
    answer = args.x**args.y
    if args.verbose >= 2:
        print(f"Running '{__file__}'")
    if args.verbose >= 1:
        print(f"{args.x}^{args.y} == ", end="")
    print(answer)