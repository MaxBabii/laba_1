while True:
    alf_UA = "абвгґдуєжзиіїйкльмншщпрстуфхцчшщьюяабвгґдуєжзиіїйкльмншщпрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯabsdefghijklmnopqrstuvwxyzabsdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWABCDEFGHIJKLMNOPQRSTUVW1234567890"
    step = 1
    message = input("Message deshif: ")
    result = ""
    for i in message:
        cell = alf_UA.find(i)
        new_cell = cell + step
        if i in alf_UA:
            result += alf_UA[new_cell]
        else:
            result += i

    print(result)