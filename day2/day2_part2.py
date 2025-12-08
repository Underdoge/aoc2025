import sys
import re

if __name__ == '__main__':
    invalid = 0
    with open(sys.argv[1], 'r') as file:
        for line in file:
           ranges = line.strip().split(",")
    for curr_range in ranges:
        start, finish = curr_range.split("-")
        start = int(start)
        finish = int(finish)
        print(curr_range)
        for number in range(start, finish+1):
            if re.search(r'^(.{1,})\1+$',str(number)):
                print(number,"<- invalid")
                invalid += number
    print(invalid)

