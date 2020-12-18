#!/usr/bin/python3

import functools

with open('day10_test.txt') as f:
    data = frozenset(int(x) for x in f.read().splitlines())

@functools.lru_cache(maxsize=None)
def count_paths(available_adaptors, current_joltage, target_joltage):
    if current_joltage == target_joltage:
        return 1
    return sum(
        count_paths(available_adaptors.difference([next_joltage]), current_joltage, target_joltage)
        for next_joltage in range(
            current_joltage+1,
            min(current_joltage+4, target_joltage+1),
        )
        if next_joltage in available_adaptors
    )

print(count_paths(data, 0, max(data) + 3))
