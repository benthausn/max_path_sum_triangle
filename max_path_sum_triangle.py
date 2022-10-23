#!/usr/bin/env python

""" Script to find the highest path sum in a triangle using a bottom up algorithm."""

__author__ = "Michaela Benthaus"
__version__ = "1.0"

import os

INPUT_FILE = r"C:\Users\micha\OneDrive\Dokumente\Lebenslauf\Werkstudent Bewerbung\Tebis\test.txt"


def max_sum(triangle_array):
    for value in range(len(triangle_array[-2])):   # second last row
        triangle_array[-2][value] = triangle_array[-2][value] + max(triangle_array[-1][value], triangle_array[-1][value + 1])  # value + bigger value of the both values below
    triangle_array.pop(-1)  # delete last row of triangle
    return triangle_array


def main():
    try:
        file = open(INPUT_FILE)
        triangle_array = []
        if os.stat(INPUT_FILE).st_size == 0:   # empty file
            print("*** WARNING: Empty input file! Max. path sum = 0")
        else:
            for line in file:
                triangle_array.append(list(map(int, line.split(" "))))   # write given txt-file in triangle_array
            while(len(triangle_array) != 1):
                max_sum(triangle_array)
            max_path_sum = triangle_array[0][0]
            print("Max. path sum:", max_path_sum)
        file.close()

    except FileNotFoundError:
        print("***ERROR: No such input file!")
        exit()


if __name__ == "__main__":
    main()