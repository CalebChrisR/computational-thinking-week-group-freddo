def solution_station_5(name: str):
    lt1 = ["Ainas", "Ben", "Christopher", "Ebony", "Iuliia", "Klementyna", "Tiara", "Tobit", "Yasmin", "Yurui", "Yuvraj", "Zoë", "Lula", "Markus", "Mateo", "Mufang", "Muni", "Nandini", "Nathan", "Oumaima"]
    lt2 = ["Alex", "Arwen", "Christina", "David", "Helen", "Huy Bao", "Iris", "Katharina", "Lora", "Mark", "Mats", "Minseo", "Quinn", "Rajko", "Sade", "Sylwia", "Tarling", "Vadim", "Zeno"]
    lt4 = ["An", "Yujie", "Douwe", "Jeremy", "Krishiv", "Lara", "Heer", "Illya", "Lucas", "Maria", "Michelle", "Neel", "Oliwia", "Paige", "Rakin", "Rapolas", "Samir", "Tom", "Yutong", "Amalia"]

    result = 0
    if name in lt1:
        result = 1
    elif name in lt2:
        result = 2
    elif name in lt4:
        result = 4
    else:
        result = 3
    return result

if __name__ == "__main__":
    lt = solution_station_5("Amalia")
    print(lt)
