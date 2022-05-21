import matplotlib.pyplot as plt
import numpy as np

# 获取待拟合数据
year = np.array([1975, 1978, 1981, 1984, 1987, 1990, 1993, 1996, 1999, 2002, 2005, 2008, 2011, 2014])
plastic = np.array([46, 64, 72, 86, 104, 120, 137, 168, 202, 231, 263, 281, 325, 367])
calculateFunction = np.polyfit(year, plastic, 3)
print(calculateFunction)

p = np.poly1d(calculateFunction)

inputType = input('please input your type 1-all 2-part\n')
if inputType == '1':
    plt.scatter(year, plastic)
    plt.plot(year, p(year))

    plt.show()
elif inputType == '2':
    inputYear = input('please input your favorite year\n')
    plt.scatter(year, plastic)
    intInputYear = int(inputYear)
    inputArrange = np.arange(1975, intInputYear, 1)
    plt.plot(inputArrange, p(inputArrange))
    plt.plot(intInputYear, p(intInputYear), "or")
    plt.show()
