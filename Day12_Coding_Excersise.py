litres = input("Enter the number of litres: ")
litres = float(litres)


def convert_milliltrs(litres_local):
    millilitres = litres_local / 1000
    return millilitres

mil_output = convert_milliltrs(litres)

message =  f'{litres} in millilters is: {mil_output}'
print(message)