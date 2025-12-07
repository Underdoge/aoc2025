import sys

class Dial:
    def __init__(self, **kwargs):
        self._number = 50

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, number: int) -> None:
        self._number = number

    def turn(self, instruction: str) -> int:
        print(f"instruction {instruction}")
        number = int(instruction[1::])
        if instruction[0] == 'R':
            turns = (number+self.number) / 100
            pos = (number+self.number) % 100
        else:
            turns = (number-self.number) / 100
            if number == self.number:
                pos = 0
            else:
                pos = (self.number-number) % 100
        print(f"{pos}")
        self.number = pos
        return pos

if __name__ == '__main__':
    dial = Dial()
    password = 0
    with open(sys.argv[1], 'r') as file:
        for line in file:
            if dial.turn(line.strip()) == 0:
                password += 1

    print(f"password {password}")
