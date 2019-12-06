import sys
import math

def parseInstruction(instruction):
    direction = instruction[0]
    distance = int(instruction[1:])
    return (direction, distance)


def printGrid(grid):
    for row in grid:
        for col in row:
            # if col:
            #     print('*', end='')
            # else:
            #     print('.', end='')
            print(col, end='')
        print()


def calcPath(instructions, size, start):
    instructions = list(map(parseInstruction, instructions))
    grid = [0] * size
    for i in range(size):
        grid[i] = [0] * size

    currentRow = start
    currentCol = start

    steps = 0

    for (direction, distance) in instructions:
        rowInc = 0
        colInc = 0
        if (direction == 'D'):
            rowInc = -1
        elif (direction == 'U'):
            rowInc = 1
        elif (direction == 'L'):
            colInc = -1
        elif (direction == 'R'):
            colInc = 1

        for i in range(distance):
            steps += 1
            currentRow += rowInc
            currentCol += colInc
            grid[currentRow][currentCol] += steps

        # printGrid(grid)

    return grid


def calcIntersectionDistance(path1, path2):
    size = 20000
    start = 10000
    grid1 = calcPath(path1, size, start)
    grid2 = calcPath(path2, size, start)

    bestDistance = 100000
    bestSteps = 100000

    for i in range(len(grid1)):
        for j in range(len(grid1[0])):
            if grid1[i][j] and grid2[i][j] and not (i == start and j == start):
                distance = abs(i - start) + abs(j - start)
                if distance < bestDistance:
                    bestDistance = distance

                steps = grid1[i][j] + grid2[i][j]
                if steps < bestSteps:
                    bestSteps = steps

    print(bestDistance, bestSteps)
    return (bestDistance, bestSteps)


def main():
    if len(sys.argv) != 2:
        print("Please provide a single input file.")
        exit(1)

    assert(calcIntersectionDistance(
        ['R8', 'U5', 'L5', 'D3'],
        ['U7', 'R6', 'D4', 'L4']
    ) == (6,30))
    assert(calcIntersectionDistance(
        ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
        ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
    ) == (159, 610))
    assert(calcIntersectionDistance(
        ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
        ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
    ) == (135,410))

    f = open(sys.argv[1], "r")
    path1 = f.readline().split(',')
    path2 = f.readline().split(',')
    f.close()

    print(calcIntersectionDistance(path1, path2))

if __name__ == "__main__":
    main()
