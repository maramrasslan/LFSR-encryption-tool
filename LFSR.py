# Souhila Sherif Zamzam 20205025
# Maram Alaa Eldein Rasslan 20205022

import re
import pyinputplus


plain_text = input("Binary plain text X = ")
initial_vector = []
key = []
cipher_text = []
coe_zero = False
coefficients = []
polynomial_LFSR = input("Enter your polynomial LFSR: ")

# Extracting the numbers out of the polynomial
digits = re.findall(r'\d+', polynomial_LFSR)
res = list(map(int, digits))

# assign the no. of FlipFlops
max_power = res[0]

# intializng the coefficients
for length in range(max_power):
    coefficients.append(int(0))

# check if polynomial have x^0
for i in reversed(range(len(polynomial_LFSR))):
    if (polynomial_LFSR[i] == '1') and (polynomial_LFSR[i-1] == '+'):
        coe_zero = True
        break

# changing the value at the result no. list
if coe_zero == True:
    for i in range(len(res)):
        if (res[i] == 1) and (len(res) == i+1):
            res[i] = '0'
        else:
            continue

# assigning the existing coe to 1
for x in range(1, len(res)):
    coefficients[int(res[x])] = 1

# assigning values to the initialize vector
print("The initial vector is: ")
for value in range(max_power):
    initial_vector.append(pyinputplus.inputNum(prompt=f"v{value}: ", min=0, max=1))

# applying LFSR number of rounds = plain text no. of bits
for key_loop in range(len(plain_text)):
    key.append(initial_vector[max_power-1])
    print(initial_vector)
    temp = 0

    # shifting and applying LFSR
    for coefficient in range(max_power):
        vector_coefficient = max_power-coefficient-1
        # storing feedback values before shifting
        temp = (temp + coefficients[coefficient]*int(initial_vector[vector_coefficient])) % 2

        if coefficient == max_power - 1:
            initial_vector[vector_coefficient] = temp

        else:
            new_value = initial_vector[vector_coefficient-1]
            initial_vector[vector_coefficient] = new_value

print(f"The key is : {key}")

# XOR the key and plain text
for cipher_loop in range(len(plain_text)):
    cipher_text.append((int(plain_text[cipher_loop]) + key[cipher_loop]) % 2)

print(f"The cipher text is : {cipher_text}")