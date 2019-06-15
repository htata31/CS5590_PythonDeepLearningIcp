import numpy as np


def randomize_replace():
    # Generates a random sample from a given 1-D array
    # Replace is used to avoid the duplicates
    random_num = np.random.choice(range(20), 15, replace=False)
    random_num.sort()
    print("Random numbers", random_num)
    # Changing the max value with 0
    random_num[random_num.argmax()] = 0
    print("Random numbers after replacing max with 0", random_num)


if __name__ == '__main__':
    randomize_replace()