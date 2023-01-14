import random


class Nums:
    def __init__(self):
        self.nums = []

    def generate(self):
        counter = 0
        while counter < 12:
            random_num = random.randint(1, 120)

            if random_num in self.nums:
                continue

            self.nums.append(random_num)
            counter += 1

        return self.nums
