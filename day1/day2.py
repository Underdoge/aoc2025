class Dial:
    def __init__(self, **kwargs):
        self._number = 50
        self._password = 0

    @property
    def password(self) -> int:
        return self._password

    @password.setter
    def password(self, password: int) -> None:
        self._password = password

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, number: int) -> None:
        self._number = number

    def turn(self, instruction: str) -> int:
        print(f"initial pos {self.number} instruction {instruction}")
        number = int(instruction[1::])
        if instruction[0] == 'R':
            turns = (number+self.number) / 100
            pos = (number+self.number) % 100
        else:
            turns = (self.number-number) / 100
            print(f"turns {turns}")
            if turns < 0:
                self.password += 1
            if number == self.number:
                pos = 0
            else:
                pos = (self.number-number) % 100
        print(f"pos {pos} turns {turns} password {self.password}")
        # if pos == 0:
        #    self.password += 1
        print(f"password after zero {self.password}")
        self.password += int(turns)
        print(f"password after {int(turns)} turns {self.password}")
        self.number = pos
        return turns

if __name__ == '__main__':
    dial = Dial()
    password = 0
    with open("input_1.txt", 'r') as file:
        for line in file:
            if dial.turn(line.strip()) == 0:
                password += 1

    print(f"password {dial.password}")
