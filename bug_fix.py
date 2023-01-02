# def speed(distance, time):
#     return distance / time
#
#
# print(speed(200, 4))
#
#
# def speed(distance, time):
#     return distance / time
#
#
# print(speed(time=5, distance=300))


def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t



time = calculate_time(100)
print(time)