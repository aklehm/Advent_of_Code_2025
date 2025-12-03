class AocDay1:
    def __init__(self):
        self.part1 = 0
        self.part2 = 0
        self.puzzleInput = list()
        self.dailMin = 0
        self.dailPos = 50
        self.dailMax = 99

        with open('input_files/day1.txt', 'r') as f:
            self.puzzleInput = f.readlines()

    def solvePart1(self):
        for turn in self.puzzleInput:
            direction = turn[0]
            distance = int(turn[1::].replace('\r', '').replace('\n', ''))

            if direction == 'L':
                self.dailPos = self.dailPos - distance
                while self.dailPos < self.dailMin:
                    self.dailPos = self.dailPos + 100
                    if self.dailPos >= self.dailMin:
                        break

            if direction == 'R':
                self.dailPos = self.dailPos + distance
                while self.dailPos > self.dailMax:
                    self.dailPos = self.dailPos - 100
                    if self.dailPos <= self.dailMax:
                        break

            if self.dailPos == 0:
                self.part1 += 1

    def solvePart2(self):
        self.dailPos = 50
        for turn in self.puzzleInput:
            direction = turn[0]
            distance = int(turn[1::].replace('\r', '').replace('\n', ''))
            for i in range(distance):
                if direction == 'R':
                    self.dailPos += 1
                    if self.dailPos == 100:
                        self.dailPos = 0
                elif direction == 'L':
                    self.dailPos -= 1
                    if self.dailPos == -1:
                        self.dailPos = 99
                if self.dailPos == 0:
                    self.part2 += 1


if __name__ == '__main__':
    aoc = AocDay1()
    aoc.solvePart1()
    aoc.solvePart2()
    print(f'Part 1: {aoc.part1}')
    print(f'Part 2: {aoc.part2}')
