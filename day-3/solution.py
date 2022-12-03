input_lines = open('input.txt').read().splitlines()
# input_lines = open('test_input.txt').read().splitlines()

def get_priority_for_char(character):
    if character.isupper():
        return ord(character) - 38
    return ord(character) - 96


def get_priority(line):
    first_compartment = set(line[:len(line) // 2])
    second_compartment = set(line[len(line) // 2:])
    common = first_compartment.intersection(second_compartment)
    return get_priority_for_char(common.pop())


def get_priority_for_group(group):
    elf1 = set(group[0])
    elf2 = set(group[1])
    elf3 = set(group[2])
    common = elf1.intersection(elf2).intersection(elf3)
    return get_priority_for_char(common.pop())

sum_priorities = 0
group = []
for i, line in enumerate(input_lines):
    if i % 3 == 2: #new group
        group.append(line)
        sum_priorities += get_priority_for_group(group)
        group = []
    else:
        group.append(line)

print(sum_priorities)
