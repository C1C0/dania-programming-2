from operator import index
from pandas import DataFrame, Series

# 1 Create a Pandas Series from a list, b = [1,7,2]
b = [1,7,2]

# 3 Custom labels
labels = ['first', 'second', 'third']
s = Series(b, index=labels)

# 2 Return first value of above series

first = s.head(1)

# 4 Create series from dict

dic = {"day1": 420, "day2": 380, "day3": 390}
s1 = Series(dic)
print(s1)

# 5 Create dataFram from 2 series

s11 = Series([420, 380, 390])
s12 = Series([50, 40, 45])

labels = ["calories", "duration"]

df = DataFrame([s11, s12], index=labels)

print(df)