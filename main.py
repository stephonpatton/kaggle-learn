import numpy
import pandas as pd
rolls = numpy.random.randint(low=1, high=225, size=10)
print(rolls)
print(rolls <= 2)

melbourne_data = pd.read_csv('datasheets/melb_data.csv')
melbourne_data.describe()

