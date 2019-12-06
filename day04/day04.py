import sys


def getNumberOfPasswords(start, end):
    password = start
    valid_passwords = 0

    while password < end:
        digits = list(map(int, str(password)))
        for i in range(len(digits) - 1):
            if digits[i+1] < digits[i]:
                for j in range(i+1, len(digits)):
                    digits[j] = digits[i]

        password = sum(d * 10**i for i, d in enumerate(digits[::-1]))
        if password > end:
            break

        i = 0
        while i < len(digits) - 1:
            if digits[i+1] == digits[i]:
                if i < len(digits) - 2 and digits[i+2] == digits[i]:
                    # increment i so we don't check again from the second digit
                    while i < len(digits) - 1 and digits[i+1] == digits[i]:
                        i += 1
                else:
                    # double digit, not triple, so we're valid
                    valid_passwords += 1
                    break
            else:
                i += 1

        password = sum(d * 10**i for i, d in enumerate(digits[::-1]))
        password += 1

    return valid_passwords


def main():
    if len(sys.argv) != 2:
        print("Please provide a single input file.")
        exit(1)

    f = open(sys.argv[1], "r")
    (start, end) = f.readline().split('-')
    f.close()

    start = int(start)
    end = int(end)
    print(getNumberOfPasswords(start, end))

if __name__ == "__main__":
    main()
