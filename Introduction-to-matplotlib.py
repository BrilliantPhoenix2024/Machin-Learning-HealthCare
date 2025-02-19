import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4))
plt.plot()
plt.show()

plt.plot([1, 2, 3, 4])
plt.show()

x = [1, 2, 3, 4]
y = [11, 22, 33, 44]
plt.plot(x, y)
plt.show()

# 1st Method:
# Creates a figure
fig1 = plt.figure()
# Adds some axes
ax = fig1.add_subplot()
plt.show()

# 2end Method:
# Create a figure
fig2 = plt.figure()
axes1 = fig2.add_axes([0.1, 0.1, 0.8, 0.8])
axes1.plot(x, y)
plt.show()

# 3rd Method:
fig3, axes2 = plt.subplots()
axes2.plot(x, [20, 50, 100, 250])
plt.show()








