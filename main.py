from parse import parse
from db import connection

def main():
    turple_of_lists = parse()
    connection(turple_of_lists)

if __name__ == '__main__':
    main()
