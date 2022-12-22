# input_lines = open('input.txt').read().splitlines()
input_lines = open('input.txt').read().splitlines()


def contains_dup(code: str):
    return len(set(code)) != len(code)


def find_signal_start(code: str):
    # for each character in string
    for i in range(len(code)-13):
        next_four = code[i:i + 14]
        if not contains_dup(next_four):
            return i + 14


for line in input_lines:
    print(find_signal_start(line))
