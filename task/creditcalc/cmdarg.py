import argparse

if __name__ == '__main__':
    #  Initialize the parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--echo", help="echo the string you use here")
    parser.add_argument("-s", "--square", help="display a square of a give number",
                        type=int)
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    args = parser.parse_args()
    if args.echo:
        print(args.echo)
    if args.square:
        print(args.square**2)
    if args.verbose:
        print("verbosity turned on")
