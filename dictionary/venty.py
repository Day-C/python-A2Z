

stuck = {"iphones": {"14-pro": 5, "12-pro_max": 4, "11-pro_max": 11},
         "samsung": {"s21-light": 12, "z-flip": 5, "s22-pro": 10},
         "tecno": {"altra-pro": 1, "cammon-X": 4, "texno-T2000": 2}
         }

def showstuck(phone, types):
    num_remaining = 0

    for k, v in phone.items():
        num_remaining += v.get(types, 0)
        return num_remaining
print('\n')
print("here is all iphones in  your inventy: ")
print(": - 14-pro    " + str(showstuck(stuck, "14-pro")))
print(": - 12-pro_max    " + str(showstuck(stuck, "12-pro_max")))
print(": - 11-pro_max    " + str(showstuck(stuck, "11-pro_max")))

