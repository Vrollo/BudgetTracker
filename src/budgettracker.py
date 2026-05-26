# SBT = Simple Budget Tracker
# Current project filename for lack of a better name
# This will be the main project
import argparse

def init_argparse():
    parser = argparse.ArgumentParser(
        prog="budgettracker", 
        formatter_class=argparse.RawTextHelpFormatter,
        description="""This is a small CLI budget tracker to keep track of your current balance.
You will be able to create new transactions, update/delete existing transactions.\n"""
    )

    # To allow the --version option without the need to combine it with a command
    # you will need to use the action="version", which will display the version
    parser.add_argument(
        "--version", 
        action="version", 
        version="Budget Tracker v0.1",
        help="Shows the current version of the budget tracker CLI tool."
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # add transactions
    add_parser = subparsers.add_parser("add", help="add a transaction")
    add_parser.add_argument("date", type=str, help="date format (str) yyyymmdd: 20260525")
    add_parser.add_argument("amount", type=float, help="transaction amount")
    add_parser.add_argument("category", type=str, help="category")

    # delete transactions
    delete_parser = subparsers.add_parser("delete", help="delete a transaction")
    delete_parser.add_argument("id", type=int, help="transaction ID")

    # update transactions
    update_parser = subparsers.add_parser("update", help="update/modify an existing transaction")
    update_parser.add_argument("id", type=int, help="transaction ID")
    update_parser.add_argument("date", type=str, help="date format yyyymmdd: 20260525")
    update_parser.add_argument("amount", type=float, help="transaction amount")
    update_parser.add_argument("category", type=str, help="category")

    # view balance
    subparsers.add_parser("balance", help="View your current balance")

    return parser.parse_args()

def main():

    args = init_argparse()

    match args.command:
        case 'add':
            print("Adding transaction:")
            print(f"Date: {args.date}")
            print(f"Amount: € {args.amount}")
            print(f"Category: {args.category} / {args.sub_category}")
        case 'delete':
            print(f"Deleting transactions: {args.id}")
        case 'update':
            print(f"Updating transaction {args.id}")
        case 'balance':
            print("Your current balance is ......")

    if args.version:
        print("Budget Tracker v0.1")

if __name__ == "__main__":
    main()
