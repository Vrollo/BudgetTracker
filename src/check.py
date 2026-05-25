import argparse

# Use init_args to setup the arguments
def init_args(parser):
    # Add arguments
    parser.add_argument('-a', '--add', nargs=4)
    parser.add_argument('-d', '--delete', nargs=1)

    # parse = 
    return parser.parse_args('-d --add date amount category sub_category'.split())

def check():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command", required=True)

    # ---- add command ----
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("filename")
    add_parser.add_argument("--force", action="store_true")

    # ---- remove command ----
    remove_parser = subparsers.add_parser("remove")
    remove_parser.add_argument("id", type=int)

    # ---- search command ----
    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("query")
    search_parser.add_argument("category")
    search_parser.add_argument("--limit", type=int, default=10)

    args = parser.parse_args()

    print(args)

if __name__ == "__main__":
    check()  