import re

pierwszy = "79-900"
drugi = "80-155"

# Function for generating list of codes in a format XX-XXX, where X is a number [0-9]
# It generates possible codes between two given codes in the same format
def postal_code_gen(first, second):
    generated_post_codes = []

    x1 = re.split("-", first)
    x2 = re.split("-", second)

    number1 = int(x1[0]) * 1000 + int(x1[1])
    number2 = int(x2[0]) * 1000 + int(x2[1])

    for i in range(number1 + 1, number2):
        generated_post_codes.append(f"{str(i)[0:2]}-{str(i)[2:5]}")

    return generated_post_codes


lista = postal_code_gen(pierwszy, drugi)

for j in range(len(lista)):
    print(lista[j])
