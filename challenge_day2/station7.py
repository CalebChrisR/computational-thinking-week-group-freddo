def solution_station_7(sequence):
    split_apart = list(sequence)
    for i in range(len(split_apart)):
        if split_apart[i] == "a":
            split_apart[i] = "3"
        if split_apart[i] == "b":
            split_apart[i] = "-1"
        if split_apart[i] == "c":
            split_apart[i] = "4"
        if split_apart[i] == "d":
            split_apart[i] = "7"
        if split_apart[i] == "e":
            split_apart[i] = "0.5"
    string_final = "".join(split_apart)        
    answer = eval(string_final)
    return float(answer)

'''
a = 3
b = -1
c = 4
d = 7
e = 0.5

make all characters separate in the string
if abcde replace with number
make math symbols work as math
do math
''' 