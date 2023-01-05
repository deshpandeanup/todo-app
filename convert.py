def convert_into_metres(feet, inches):
    feet = float(feet)
    inches = float(inches)
    meters = feet * 0.3048 + inches * 0.0254
    return meters


if __name__ == "__main__":
    test_output = convert_into_metres(3, 4)
    print(test_output)
