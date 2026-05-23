import argparse
def main():
    parser = argparse.ArgumentParser(description="CLI Tools for simulating the AI Model training paramters")

    # Positional args
    parser.add_argument(
        "model_name",
        type = str,
        help="The name of the architecture to use eg: ResNet50"
    )

    # Optional args(cuz of --)
    parser.add_argument(
        "--epochs",
        "-e", # alias for longer name --epochs
        type = int,
        default = 10,
        help = "Number of Training epochs"
    )
    parser.add_argument(
        "--learning_rate",
        "-lr",
        default = 0.001,
        help = "The learning rate for the optimizer"
    )
    parser.add_argument( 
        "--verbose", 
        action="store_true",
        help = "Enable verbose logging output"
        ''' By default --verbose False verbose means Talkative. In programming, this is a universal standard. If verbose is OFF, the program runs silently. If verbose is ON, the program prints every single detail of what it is doing.
        '''
    )
    args = parser.parse_args()
    print("--Initializtion--")
    print(f"Loading architecture:{args.model_name}")

    if args.verbose:
        print(f"[VERBOSE] system configured with {args.epochs} epochs.")
        print(f"[VERBOSE] optimizer set to learning Rate: {args.learning_rate}")
    
    print("--Training Started--")
    print(f"Training {args.model_name} for {args.epochs} epochs...")

    total_steps = args.epochs * 1000
    print(f"Total steps to execute: {total_steps}")

if __name__== "__main__":
    main()