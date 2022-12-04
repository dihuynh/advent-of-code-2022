input_lines = open('input.txt').read().splitlines()
# input_lines = open('test_input.txt').read().splitlines()


def get_range(assignment):
    return set(range(int(assignment.split('-')[0]), int(assignment.split('-')[1]) + 1))

def check_overlap(line):
    elf1 = get_range(line.split(',')[0])
    elf2 = get_range(line.split(',')[1])
    if elf1.intersection(elf2):
        return 1
    return 0


total_overlaps = 0
for line in input_lines:
    total_overlaps += check_overlap(line)
print(total_overlaps)

