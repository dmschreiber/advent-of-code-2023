import re
import scrib
import os
from collections import namedtuple
from timeit import default_timer as timer


def solve(input):
    with open(input) as f:
        lines = f.read().splitlines()

    # grid = scrib.parsegrid(lines)

    g = []
    # max_r = len(lines)
    # max_c = len(lines[0])

    # g = [k for k in grid if grid[k] == "#"]
    # ex_r = [r for r in range(max_r) if all([scrib.get(grid,r,c)=='.' for c in range(max_c+1)])]
    # ex_c = [c for c in range(max_c) if all([scrib.get(grid,r,c)=='.' for r in range(max_r+1)])]

    g = [(r,c) for r,line in enumerate(lines) for c,item in enumerate(line) if item == "#"]
    ex_r = [r for r,item in enumerate(lines) if all(i == "." for i in item)]
    ex_c = [c for c,item in enumerate(zip(*lines)) if all(i == "." for i in item)]

    d_p1 = {}
    d_p2 = {}
    for k, g1 in enumerate(g):
        for j, g2 in enumerate(g[:k+1]):
            exp_r = (sum([1 for r in ex_r if r in range(*sorted([g1[0],g2[0]]))]))
            exp_c = (sum([1 for c in ex_c if c in range(*sorted([g1[1],g2[1]]))]))
            d_p2[(g1,g2)] = abs(g1[0]-g2[0]) + abs(g1[1]-g2[1]) + exp_r*999999 + exp_c*999999
            d_p1[(g1,g2)] = abs(g1[0]-g2[0]) + abs(g1[1]-g2[1]) + exp_r + exp_c

    return sum(d_p1.values()), sum(d_p2.values())


if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"
    start = timer()
    p1, p2 = solve(input_file)
    assert(p1==9370588)
    assert(p2==746207878188)
    print("{} part 1: {}".format(d,p1))
    print("{} part 2: {}".format(d,p2))
    print("elapsed time {}".format(timer()-start))
    # print("day 8 part 1: {}".format(part1("./data/day10_test.txt")))

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))