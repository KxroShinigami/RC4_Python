from rc4 import RC4
import random
import matplotlib.pyplot as plt
import collections

# Define the number of times to call rc4
num_calls = 10000000

# Define the list to store the output of rc4
rc4_output = []

# Call rc4 multiple times and store the output in the list
for i in range(num_calls):
    # random 16 byte key
    key = bytes([random.randint(0, 255) for i in range(16)])
    message = b'\x00' * 32
    # get 2nd byte of output
    rc4_output.append(RC4(key=key, message=message)[1])


# Print the count of bytes, sort by most frequent
print("Count of bytes: ", collections.Counter(rc4_output).most_common())


# Create a histogram of the output
plt.hist(rc4_output, bins=256)
plt.xlabel("Byte Value")
plt.ylabel("Frequency")
plt.title("Histogram of RC4 Output")
plt.show()