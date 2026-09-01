def solution_station_4(inp):
    if inp <= 1:
        return False
    for i in range(2, inp):
        if inp % i == 0:
            return False
    return True