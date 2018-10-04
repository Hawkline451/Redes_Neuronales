import clase_1
import numpy as np
import matplotlib.pyplot as plt


#input
n_points = 80

#red points are 1
x = np.random.uniform(low=0, high=25, size=(n_points,))
y = np.random.uniform(low=0, high=35, size=(n_points,))
values = np.zeros(n_points)

#blue points are 0
x_2 = np.random.uniform(low=30, high=50, size=(n_points,))
y_2 = np.random.uniform(low=0, high=50, size=(n_points,))
values_2 = np.ones(n_points)

coord = np.array( list(zip(np.append(x, x_2),np.append(y, y_2))) )
labels = np.append(values, values_2)
print(coord)


#random weight and bias during first iteration
old_w = [np.random.randint(-2,2), np.random.randint(-2,2)]
bias_ini = np.random.randint(-2,2)

#Number of iterations
n_iter = 50
# Learning rate
lr = .1

for n in range(n_iter):
    random_point = np.random.randint(n_points*2)
    train_row = coord[random_point]

    perceptron = clase_1.FirstPerceptron(old_w, bias_ini)
    out = perceptron.feed_perceptron(train_row)

    
    expected = labels[random_point]
    diff = expected - out
    print("-----")
    print(coord[random_point])
    print(labels[random_point])

    
    for i in range(len(old_w)):
        old_w[i] += (lr * train_row[i] * diff)
    print(old_w + (lr*coord[i]*diff))    
    print(old_w)

    bias = bias_ini + (lr * diff)
count = 0
 
for j in range(len(coord)):
    perceptron = clase_1.FirstPerceptron(old_w, bias)
    out = perceptron.feed_perceptron((coord[j][0], coord[j][i]))
    count = (count + 1) if out ==  labels[j] else count

print(count)




#plt.scatter(x, y, c = "red")
#plt.scatter(x_2, y_2, c = "blue")
#plt.show()
