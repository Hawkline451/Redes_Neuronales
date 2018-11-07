
from __future__ import division

import clase_1

import numpy as np
import matplotlib.pyplot as plt 


training_set = [((0, 0), 0), 
                ((0, 1), 1), 
                ((1, 0), 1), 
                ((1, 1), 0)]

x = [training_set[i][0][0] for i in range(len(training_set))]
y = [training_set[i][0][1] for i in range(len(training_set))]

for x, value in training_set:  
    if value == 0:  
        plt.scatter(x[0], x[1], color='red')
    else:
        plt.scatter(x[0], x[1], color='blue')


# parameter initialization
w = np.random.rand(2)
errors = [] 
w_list = []
b_list = []

eta = .1
epoch = 100
b = 0


# Learning
for i in range(epoch):
    for x, y in training_set:
        
        train_row = x
        perceptron = clase_1.FirstPerceptron(w, b)
        out = perceptron.feed_sigmoid(train_row)
        error = y - out 
      
        errors.append(error) 
        for index in x:
            #print(w[index])
            w[index] += eta * error * y
            b += eta*error
        w_list.append(w)
        b_list.append(b)



for x, y in training_set:        
    train_row = x
    print(train_row)
    perceptron = clase_1.FirstPerceptron(w, b)
    out = perceptron.feed_sigmoid(train_row)

    print(out)


