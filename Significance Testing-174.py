## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt
mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)
print(mean_group_a)
print(mean_group_b)
plt.hist(weight_lost_a)
plt.show()
plt.hist(weight_lost_b)
plt.show()

## 4. Test statistic ##

mean_difference = mean_group_b - mean_group_a
print(mean_difference)

## 5. Permutation test ##

mean_difference = 2.52
print(all_values)
mean_differences = []
for i in range(1000):
    group_a = []
    group_b = []
    for value in all_values:
        assignment_chance = np.random.rand()
        if assignment_chance >= 0.5:
            group_a.append(value)
        else:
            group_b.append(value)
    iteration_mean_difference = np.mean(group_b) - np.mean(group_a)
    mean_differences.append(iteration_mean_difference)
    
plt.hist(mean_differences)
plt.show()
    

## 7. Dictionary representation of a distribution ##

sampling_distribution={}
for key in mean_differences:
    if sampling_distribution.get(key,False):
        sampling_distribution[key]=sampling_distribution[key]+1
    else:
        sampling_distribution[key]=1
   

## 8. P value ##

frequencies=[]
for key in sampling_distribution:
    if key >= 2.52:
        frequencies.append(key)
import numpy
sum_freq=numpy.sum(frequencies)
p_value=sum_freq/1000