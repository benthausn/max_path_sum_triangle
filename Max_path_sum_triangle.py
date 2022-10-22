#!/usr/bin/env python

""" Script to find the highest path sum in a triangle using a bottom up algorithm."""

__author__ = "Michaela Benthaus"
__version__ = "1.0"

import os

INPUT_FILE = r"C:\Users\micha\OneDrive\Dokumente\Lebenslauf\Werkstudent Bewerbung\Tebis\test.txt"

def maxSum(array):
    for value in range(len(array[-2])):   # second last row
        array[-2][value] = array[-2][value] + max(array[-1][value], array[-1][value + 1])  # value + bigger value of the both values below
    array.pop(-1)  # delete last row of triangle
    return array

def main():
    try:
        file = open(INPUT_FILE)
        array = []
        if os.stat(INPUT_FILE).st_size == 0:   # empty file
            print("*** WARNING: Empty input file! Max. path sum = 0")
        else:
            for line in file:
                array.append(list(map(int, line.split(" "))))   # write given txt-file in array
            while(len(array) != 1):
                maxSum(array)
            sum = array[0][0]
            print("Max. path sum:", sum)
        file.close()

    except FileNotFoundError:
        print("***ERROR: No such input file!")
        exit()

if __name__ == "__main__":
    main()