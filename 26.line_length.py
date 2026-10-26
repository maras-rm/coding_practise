# Challenge: write a function to calculate the length of line segments joining 2 given points
# challenge can be found here: https://app.programiz.pro/community-challenges/preview/length-of-line/info

import math

def calculate_line_length(point1, point2):
    # get the distance of both x points
    # (x2 - x1) to the power of 2
    p1 = (point1[0] - point2[0])**2
    # get the distance of both y points
    # (y2 - y1) to the power of 2
    p2 = (point1[1] - point2[1])**2
    # square root of p1 + p2 = length of line
    overall = math.sqrt(p1+p2)

    return(round(overall, 2))


if __name__ == "__main__":
    print(calculate_line_length((15,7), (22,11)))