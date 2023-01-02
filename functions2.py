def temp_check(temp_local):
    if temp_local < 0:
        temp_res = "Solid"
    elif 0 < temp_local < 100:
        temp_res = "Liquid"
    else:
        temp_res = "Gas"
    return temp_res
