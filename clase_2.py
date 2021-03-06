import clase_1

import numpy as np
import matplotlib.pyplot as plt

training_set = [((0, 0), 0), 
                ((0, 1), 1), 
                ((1, 0), 1), 
                ((1, 1), 1)]

plt.figure(0)

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

eta = .5
epoch = 30
b = 0


# Learning
for i in range(epoch):
    for x, y in training_set:
        
        train_row = x
        perceptron = clase_1.FirstPerceptron(w, b)
        out = perceptron.feed(train_row)
        error = y - out 
      
        errors.append(error) 
        for index in x:
            #print(w[index])
            w[index] += eta * error * y
            b += eta*error
        w_list.append(w)
        b_list.append(b)


count_list = []
for w, b in zip(w_list, b_list):
    count = 0
    for x, y in training_set:        
        train_row = x
        perceptron = clase_1.FirstPerceptron(w, b)
        out = perceptron.feed(train_row)
        count = (count + 1) if out ==  y else count
    count_list.append(count/len(training_set))

print(count_list)
            
# final decision boundary
a = [0,-b/w[1]]
c = [-b/w[0],0]
plt.plot(a,c)
   
# ploting errors   
plt.figure(2)
plt.ylim([-1,1]) 
plt.plot(errors)

# ploting precision   
plt.figure(3)
plt.ylim([0,1.1]) 
plt.plot(count_list)

plt.show()