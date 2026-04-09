''' 
20th Feb

Assignment Name : NumPy Speed Test
Description : Compare Python lists vs NumPy arrays with 1M numbers, measure execution time, write 3 observations
'''

import numpy as np
import time

# Create 1 million numbers
size = 1000000

# Python List
python_list = list(range(size))

start = time.time()
result_list = [x * 2 for x in python_list]
end = time.time()

print("Python List Time:", end - start)

# NumPy Array
numpy_array = np.array(range(size))

start = time.time()
result_array = numpy_array * 2
end = time.time()

print("NumPy Array Time:", end - start)

