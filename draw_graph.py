import matplotlib.pyplot as plt
import numpy as np
x = np.array([2021,2022,2023,2024])
y = np.array([36,54,76,84])
plt.plot(x,y,marker = ".",
         ms = 10,mfc="purple",
         mec = "black",
         ls = "dotted")
plt.show()