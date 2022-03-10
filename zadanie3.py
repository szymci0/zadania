from decimal import Decimal
import numpy as np


# Function that generates a list of a decimal numbers in range [start, stop] with a specified step
def generate_list(start_point, end_point, step):
    g_list = np.arange(
        Decimal(start_point), Decimal(end_point) + Decimal(step), Decimal(step)
    ).tolist()
    return g_list


if __name__ == "__main__":
    print(generate_list(2, 5.5, 0.5))
