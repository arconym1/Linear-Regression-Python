import sys

import matplotlib.pyplot as plt
import math


def get_mean(arr: list):
    counter, output = 0, 0
    for value in arr:
        counter += 1
        output += value
    return output / counter


def get_standard_deviation(arr: list, squared_value):
    len_ = len(arr) - 1
    sqrt_ = squared_value / len_
    return math.sqrt(sqrt_)


x = [9054.914, 9437.372, 12239.894, 12495.334, 15991.736, 17288.083, 18064.288, 19121.592, 20732.482, 25864.721,
     27195.197, 29866.581, 32485.545, 35343.336, 37044.891, 37675.006, 40106.632, 40996.511, 41973.988, 43331.961,
     43603.115, 43724.031, 43770.688, 49866.266, 50854.583, 50961.865, 51350.744, 52114.165, 55805.20]
y = [6., 5.6, 4.9, 5.8, 6.1, 5.6, 4.8, 5.1, 5.7, 6.5, 5.8, 6., 5.9, 7.4, 7.3, 6.5, 6.9, 7., 7.4, 7.3, 7.3, 6.9,
     6.8, 7.2, 7.5, 7.3, 7., 7.5, 7.2]
# x and y have to be the same length

# Function -> y = a + bx
# Slope (b) of regression line -> b = r * s(y) / s(x)
# Y-intercept (a) of regression line -> mean(y) - b*mean(x)

# 1. Calculate Pearson Correlation Coefficient ( r )
mean_x = get_mean(x)
mean_y = get_mean(y)
x_xmean_times_y_ymean, x_xsquared, y_ysquared = [], [], []

for n in range(len(x)):
    assert len(x) == len(y)
x_xmean_times_y_ymean.append((x[n] - mean_x) * (y[n] - mean_y))
x_xsquared.append((x[n] - mean_x) ** 2)
y_ysquared.append((y[n] - mean_y) ** 2)

sum_over = round(sum(x_xmean_times_y_ymean), 2)
sum_x_xsquared = round(sum(x_xsquared), 2)
sum_y_ysquared = round(sum(y_ysquared), 2)

r = sum_over / math.sqrt(sum_x_xsquared * sum_y_ysquared)

x_std = get_standard_deviation(x, sum_x_xsquared)
y_std = get_standard_deviation(y, sum_y_ysquared)

b = r * (y_std / x_std)
a = mean_y - b * mean_x

_x = int(input("Enter value : "))
print("Y = ", a + b * _x)
