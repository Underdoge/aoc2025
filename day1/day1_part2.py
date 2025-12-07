import sys
import math

class Dial:
    def __init__(self, **kwargs):
        self._position = 50
        self._password = 0

    @property
    def password(self) -> int:
        return self._password

    @password.setter
    def password(self, password: int) -> None:
        self._password = password

    @property
    def position(self) -> int:
        return self._position

    @position.setter
    def position(self, position: int) -> None:
        self._position = position

    def turn(self, instruction: str) -> int:
        number = int(instruction[1::])
        print(f"initial pos {self.position} instruction {instruction} turn {number} pass {self.password}")
        if instruction[0] == 'R':
            turns = (number+self.position) / 100
            pos = (number+self.position) % 100
        else:
            turns = (self.position-number) / 100
            print(f"turns {turns}")
            pos = int(math.modf(turns)[0]*100)
            print(f"new pos {pos}")
            if self.position == number:
                pos = 0
                self.password += 1
                print(f"password after zero {self.password}")
            if turns < 0 and abs(int(turns)) < 1 and self.position != 0:
                self.password += 1
            if turns < 0 and self.position != 0:
                pos = 100 + int(math.modf(turns)[0]*100)
            elif turns < 0:
                pos = 100 + int(math.modf(turns)[0]*100)
        print(f"pos {pos} turns {abs(int(turns))} password {self.password}")
        if abs(int(turns)) > 0:
            self.password += abs(int(turns))
            print(f"password after {int(turns)} pass {self.password}")
        self.position = pos
        print(f"final pos {pos} pass {self.password}")
        return turns

if __name__ == '__main__':
    dial = Dial()
    instructions = 0
    with open(sys.argv[1], 'r') as file:
        for line in file:
            dial.turn(line.strip())
            print("")
            instructions += 1
            # if instructions % 10 == 0:
            #    input()

    print(f"final pos {dial.position} password {dial.password}")
