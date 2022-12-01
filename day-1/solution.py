
input_lines = open('input.txt').read().splitlines()

current_sum = 0
all_sums = []
for line in input_lines:
    if line != '':
        current_sum += int(line)
    else:
        all_sums.append(current_sum)
        current_sum = 0

all_sums.sort()
print(all_sums[-1] + all_sums[-2] + all_sums[-3])
