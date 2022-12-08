import re


def build_stacks(stacks_lines, number_of_stacks):
    stacks = [[] for x in range(number_of_stacks + 1)]
    for line in stacks_lines[:-1]:
        for stack_index, stack in enumerate(stacks[1:]):
            item_index = 1 + stack_index * 4
            # print(line, item_index)
            if line[item_index] != ' ':
                stack.append(line[item_index])
    return stacks


def find_message(stacks):
    message = ''
    for stack in stacks:
        if stack:
            message += str(stack.pop())
    return message


def apply_instructions(stacks, instructions_lines):
    regex = re.compile(r'move (\d*) from (\d*) to (\d*)')

    for line in instructions_lines:
        result = regex.match(line)
        number_of_items = int(result.group(1))
        from_stack = int(result.group(2))
        to_stack = int(result.group(3))
        stacks[to_stack].extend(stacks[from_stack][0:number_of_items])
        stacks[from_stack] = stacks[from_stack][number_of_items:]
        print(f'{stacks}\n')
    return stacks


def main():
    input_lines = open('input.txt').read().splitlines()
    number_of_stacks = 9
    index_of_break = input_lines.index('')
    stacks_lines = input_lines[:index_of_break]
    # stacks_lines.reverse()
    instructions_lines = input_lines[index_of_break + 1:]
    stacks = build_stacks(stacks_lines, number_of_stacks)
    print(f'{stacks}\n')
    new_stacks = apply_instructions(stacks, instructions_lines)
    message = find_message(new_stacks)
    print(message)


main()
