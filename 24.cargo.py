# Challenge: Does Cargo fit?
# Write a function to determine if a cargo fits into a box

# A function takes dimension of box as a list [len, width, height] and volume of the cargo as inputs.
# in side the function calculate volume of box and compare it with volume of cargo
# return True if cargo fits into the box otherwise return False
# vol = l x w x h
# Challenge can be found here: https://app.programiz.pro/community-challenges/preview/does-cargo-fit/info

def cargo_fit(box_dimensions, cargo_volume):
    # If three var are not given for box dimension return error message
    if (len(box_dimensions) < 3):
        return 'Error: Three variables for box dimension is required. '

    # as we know len, width, height assign vars
    box_l, box_w, box_h = box_dimensions[0], box_dimensions[1], box_dimensions[2]

    # vol = l x w x h
    vol_of_box = box_l * box_w * box_h

    # if volume of box is less than or equal to cargo volume it will fit: hence return true
    if (vol_of_box <= cargo_volume):
        return True
    # else: vol of box will not fit in cargo so return false
    else:
        return False

if __name__ == "__main__":
    print(cargo_fit([1,2], 6)) # outcome: Error: Three variables for box dimension is required.
    print(cargo_fit([1,2,3], 6)) # outcome: True
    print(cargo_fit([1,2,4], 6)) # outcome: False