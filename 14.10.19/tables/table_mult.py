#!/usr/bin/python3

# Generate multiplication table from 1 to 10


def generate_table(n):
    # Initialize empty list
    l = []

    for i in range(1, 11):
        l.append(i*n)  # Note the indentation is 4 spaces for code inside for!

    return l

# Store multiplication table based on the number of the table


def get_all_tables():
    d = {}
    for i in range(1, 11):
        d[i] = generate_table(i)

    return d


# d = get_all_tables()
# print(d)
