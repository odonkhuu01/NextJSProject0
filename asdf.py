
# import re
# m = re.match(r"(\w+)@(\w+)\.(\w+)", 'odonkhuu4@gmail.com')
# # print(m.group())
# # print(m.group(1))
# # print(m.group(2))
# # print(m.group(3))
# # print(m.group(1, 2, 3))
# # print(m.groups())
# # print(m.start())
# # print(m.end())
# # print(m.span())

import re

def square(match):
    number = int(match.group(0))
    return str(number**2)

print(re.sub(r"\d+", square, "11 2 3 4 5 6 7 8 9"))