#!/usr/bin/env python3
# Created by: Enoch O
# Created on: Feb 27, 2025
# This program calculates the circumference and area of a circle.
import math


def main():
    # Input
    radius = 8
    # Calculations
    circumference = math.pi * 2 * radius
    area = math.pi * radius**2
    sqrt_100 = math.sqrt(100)
    sqrt_25 = math.sqrt(25)

    # Output
    print(circumference)
    print(area)
    print(sqrt_100)
    print(sqrt_25)


if __name__ == "__main__":
    main()
