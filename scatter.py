import matplotlib.pyplot as plt
import math

initial_x = [0.0101, 0.7919, 0.7445, 0.0374]
initial_y = [0.2140, 0.2527, 0.2609, 0.0020]
label_list = ['OSP', 'Gauss-Southwell', 'EvePPR-APP', 'EvePPR']
marker_list = ['o', '*', '+', 'd']


for i in range(len(initial_x)):
    initial_x[i] = 0.75 + math.log10(initial_x[i]) * 0.25

for i in range(len(initial_y)):
    initial_y[i] = 1 + math.log10(initial_y[i]) * 0.25

for i in range(len(initial_x)):
    plt.scatter(initial_x[i], initial_y[i], label = label_list[i], marker = marker_list[i], alpha = 0.7, s = 100)

plt.ylim(0, 1)
plt.xlim(0, 1)
plt.xticks([0.25, 0.5, 0.75], ['$10^{-2}$', '$10^{-1}$', '$10^0$'])
plt.yticks([0.25, 0.5, 0.75, 1], ['$10^{-3}$', '$10^{-2}$', '$10^{-1}$', '$10^0$'])
plt.xlabel('Running Time (second)')
plt.ylabel('2-Norm Error')
plt.legend(loc = 'lower right')
plt.show()