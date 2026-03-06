# Computer Architecture - University of York - 06/03/2026

# This is an implementaion of a simple python program, which will be copied by a x86-64 assembly program, and then executed by the assembly program. The purpose of this is to demonstrate how to write a simple assembly program, which can execute a python program.

#python will do simple numeric workloads

def sum_to_n(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def count_positive(numbers: list) -> int:
    count = 0
    for n in numbers:
        if n > 0:
            count += 1
    return count

def max(numbers: list) -> int:
    if not numbers:
        return None
    maximum = numbers[0]
    for n in numbers:
        if n > maximum:
            maximum = n
    return maximum



