import fileinput

from thinq_parser import parser

def main():
    with fileinput.input() as fin:
        for line in fin:
            print(parser.parse(line.rstrip()))
            
if __name__ == "__main__":
    main()