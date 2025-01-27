import matplotlib.pyplot as plt
import numpy as np
np.random.seed(44)
data=np.random.randint(22,88,1000)
plt.hist(data,bins=12,edgecolor='black',color='Green')
plt.title('Histogram of Cancer Patients Age Distributions')
plt.xlabel('Age')
plt.ylabel('Number of Patients')
plt.show()
