import sys


def compute(opcodes):
    currentIndex = 0

    while currentIndex < len(opcodes):
        op = opcodes[currentIndex]

        if op == 99:
            break
        else:
            try:
                x = opcodes[opcodes[currentIndex + 1]]
                y = opcodes[opcodes[currentIndex + 2]]

                if op == 1:
                    z = x + y
                elif op == 2:
                    z = x * y
                else:
                    print("Invalid opcode " + str(op))
                    exit(2)

                result_index = opcodes[currentIndex + 3]
                opcodes[result_index] = z

            except:
                print("Invalid index. Returning.")
                return opcodes

        currentIndex += 4

    return opcodes


def search(original_opcodes):
    search_size = len(original_opcodes)
    for noun in range(search_size):
        for verb in range(search_size):
            opcodes = original_opcodes.copy()
            opcodes[1] = noun
            opcodes[2] = verb

            opcodes = compute(opcodes)
            output = opcodes[0]
            if output == 19690720:
                return (noun, verb)

    return (0, 0)


def main():
    if len(sys.argv) != 2:
        print("Please provide a single input file.")
        exit(1)

    assert(compute([1,0,0,0,99]) == [2,0,0,0,99])
    assert(compute([2,3,0,3,99]) == [2,3,0,6,99])
    assert(compute([2,4,4,5,99,0]) == [2,4,4,5,99,9801])
    assert(compute([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99])

    f = open(sys.argv[1], "r")
    opcodes_string = f.read()
    f.close()

    original_opcodes = list(map(int, opcodes_string.split(',')))

    (noun, verb) = search(original_opcodes)
    print("Noun: ", noun, ", verb: ", verb, ", answer: ", noun * 100 + verb)


if __name__ == "__main__":
    main()
