import argparse

def init_argparse():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command", required=True)

    # add transactions
    add_parser = subparsers.add_parser("add", help="add a transaction")
    add_parser.add_argument("date", type=str, help="date format (str) yyyymmdd: 20260525")
    add_parser.add_argument("amount", type=float, help="transaction amount")
    add_parser.add_argument("category", type=str, help="category")
    add_parser.add_argument("sub_category", type=str, help="sub-category")

    # delete transactions
    delete_parser = subparsers.add_parser("delete", help="delete a transaction")
    delete_parser.add_argument("id", type=int, help="transaction ID")

    # update transactions
    update_parser = subparsers.add_parser("update", help="update/modify an existing transaction")
    update_parser.add_argument("id", type=int, help="transaction ID")
    update_parser.add_argument("date", type=str, help="date format (str) yyyymmdd: 20260525")
    update_parser.add_argument("amount", type=float, help="transaction amount")
    update_parser.add_argument("category", type=str, help="category")
    update_parser.add_argument("sub_category", type=str, help="sub-category")   

    # view balance
    balance_parser = subparsers.add_parser("balance", help="View your current balance")


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

if __name__ == "__main__":
    main()
