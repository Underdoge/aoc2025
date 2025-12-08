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
    
    def turn_right(self) -> int:
        if self.position == 99:
            self.password += 1
            self.position = 0
            return self.position
        self.position += 1
        return self.position


    def turn_left(self) -> int:
        if self.position == 1:
            self.password += 1
            self.position = 0
            return self.position
        if self.position == 0:
            self.position = 99
            return self.position
        self.position -= 1
        return self.position
        

    def turn(self, instruction: str) -> None:
        number = int(instruction[1::])
        print(f"initial pos {self.position} instruction {instruction} turn {number} pass {self.password}")
        if instruction[0] == 'R':
            for i in range(number):
                pos = self.turn_right()
        else:
            for i in range(number):
                pos = self.turn_left()
        print(f"final pos {pos} pass {self.password}")

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
