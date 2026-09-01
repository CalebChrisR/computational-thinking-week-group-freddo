
def solution_station_1(n: int):
    a = 0
    b = 1
    fib_numbers = []
    for _ in range(n+1):
        fib_numbers.append(a)
        a, b = b, a+b
        # returns the final fin number in the list of numbers
    return fib_numbers[-1]

if __name__ == "__main__":
    answers = solution_station_1(26)
    print(answers[-1])
# 54 , 49
# 88, 57
# 26, 9