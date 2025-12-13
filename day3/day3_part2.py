import sys

def sum_banks(input: str, battery_number: int) -> int:
    sum = 0
    with open(input, 'r') as file:
        for line in file:
            bank = [int(x) for x in list(line.strip()).copy()]
            num = ""
            while len(num) < battery_number:
                sorted_bank = bank.copy()
                sorted_bank.sort(reverse=True)
                for val in sorted_bank:
                    if len(bank[bank.index(val):]) >= battery_number - len(num):
                        picked = val
                        break
                num += str(picked)
                bank = bank[bank.index(picked)+1:]
            sum += int(num)
    return sum

if __name__ == '__main__':

    print("final sum", sum_banks(sys.argv[1], 12))
