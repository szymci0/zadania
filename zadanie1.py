import re


# Function for generating list of codes in a format XX-XXX, where X is a number [0-9]
# It generates possible codes between two given codes in the same format
def postal_code_gen(first_code, second_code):
    generated_post_codes = []

    x1 = re.split("-", first_code)
    x2 = re.split("-", second_code)

    number1 = int(x1[0]) * 1000 + int(x1[1])
    number2 = int(x2[0]) * 1000 + int(x2[1])

    for i in range(number1 + 1, number2):
        generated_post_codes.append(f"{str(i)[0:2]}-{str(i)[2:5]}")

    return generated_post_codes


# Test of the function on some input
if __name__ == "__main__":
    first = "79-900"
    second = "80-155"
    finished = postal_code_gen(first, second)

    for j in range(len(finished)):
        print(finished[j])
