class AocDay2:
    def __init__(self):
        self.part1 = 0
        self.part2 = 0
        self.puzzleInput = list()

        with open('input_files/day2.txt', 'r') as f:
            self.puzzleInput = f.readlines()

    def solvePart1(self):
        idRanges = self.puzzleInput[0].split(',')
        for idRange in idRanges:
            ids = idRange.split('-')
            firstID = int(ids[0])
            lastID = int(ids[1])

            for i in range(firstID, lastID+1, 1):
                idStr = str(i)
                idLength = len(idStr)
                if idLength % 2 == 0:
                    firstIDPart = idStr[0:int(idLength/2)]
                    lastIDPart = idStr[int(idLength/2):idLength]
                    if firstIDPart == lastIDPart:
                        self.part1 += i

    def solvePart2(self):
        idRanges = self.puzzleInput[0].split(',')
        for idRange in idRanges:
            ids = idRange.split('-')
            firstID = int(ids[0])
            lastID = int(ids[1])
            for i in range(firstID, lastID+1, 1):
                idStr = str(i)
                idLength = len(idStr)
                invalidIds = []
                for j in range(1, idLength):
                    if idLength % j == 0:
                        idParts = [int(idStr[i:i+j]) for i in range(0, idLength, j)]
                        if len(set(idParts)) == 1 and i not in invalidIds:
                            invalidIds.append(i)
                            self.part2 += int(idStr)


if __name__ == '__main__':
    aoc = AocDay2()
    aoc.solvePart1()
    aoc.solvePart2()
    print(f'Part 1: {aoc.part1}')
    print(f'Part 2: {aoc.part2}')
