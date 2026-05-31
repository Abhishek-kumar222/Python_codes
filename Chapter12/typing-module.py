# from typing import List, Tuple, Union

# number : list[int] = [2,3,2,3,4,2,1]
# print(number)

# numbers: list[int] = [1, 2, 3, 4]
# names: list[str] = ["Ram", "Shyam"]

# print(names)


from typing import Tuple

point: Tuple[int, int] = (10, 20)


 # Union -Ek se zyada type allow karne ke liye:

from typing import Union

data: Union[int, str] = 10
data = "Hello"

# and so on 
# Function Example
from typing import List

def average(nums: List[int]) -> float:
    return sum(nums) / len(nums)

print(average([10, 20, 30]))