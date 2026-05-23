import argparse as a

parser=a.ArgumentParser(description="Simple calculation");
parser.add_argument("n1",type=float, help='1st num') # here n1,n2 and oper will become the atttribute of the class later and accepts the value as the inputs given in the cmd line arguments
parser.add_argument("n2",type=float, help='2nd num')
parser.add_argument('oper',choices=['add','sub','mul','div'],help='Operation to perform')
args=parser.parse_args()

if(args.oper=='add'):
    print(f"Result is {args.n1+args.n2}")
elif(args.oper=='sub'):
    print(f"Result is {args.n1-args.n2}")
elif(args.oper=='div'):
    print(f"Result is {args.n1/args.n2}")
elif(args.oper=='mul'):
    print(f"Result is {args.n1*args.n2}")
else:
    print("Invalid operation entered!")