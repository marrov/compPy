#!/usr/bin/python3

# First one is correct but gives linter error warning
#from . import table_mult
# Second one is correct if run with -m from its directory
import table_mult

from pprint import pprint


def print_all_tables():
    d = table_mult.get_all_tables()
    pprint(d)


if __name__ == "__main__":
    print_all_tables()
