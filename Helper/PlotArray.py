import numpy as np
import matplotlib.pyplot as plt

image = np.array([
                    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
                    [0, 0, 1, 1, 1, 1, 1, 0, 0,],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0,],
                    [0, 0, 1, 1, 1, 1, 0, 0, 0,],
                    [0, 0, 0, 0, 0, 0, 1, 0, 0,],
                    [0, 0, 0, 0, 0, 0, 1, 0, 0,],
                    [0, 0, 1, 0, 0, 0, 1, 0, 0,],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0,],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
                ])
plt.imshow(image, cmap='gray')
plt.show()
print(image.shape)