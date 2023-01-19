# (T) use enumerator() and zip()-(combine multiple iterators into one) to print a list from two lists


def Filter1(x):
    if x > 50:
        return True
    else:
        return False


def Map1(x):
    return x * x


# Example input

grades = [
    34,
    99,
    56,
    87,
]


# Transformers
# filter functions
print(list(filter(Filter1, grades)))
# map function
print(sorted(list(map(Map1, grades))))

# itertools
import itertools

seq = ["jan", "thomas", "patryk"]
cycle1 = itertools.cycle(seq)
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))
# accumulate, chain, takewhile, dropwhile
# predicate function -
