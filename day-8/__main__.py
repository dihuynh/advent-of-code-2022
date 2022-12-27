from solution import Solver

if __name__ == '__main__':
    # input = open('test_input.txt').read()
    input = open('input.txt').read()
    solver = Solver(input.splitlines())
    solver.solve()

    print(f'Part 1: {solver.part1}')
    print(f'Part 2: {solver.part2}')


