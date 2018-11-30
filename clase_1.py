from __future__ import division

import numpy as np

class FirstPerceptron(): 

  def __init__(self, w_list, bias):
    self.w_list = w_list
    self.bias = bias

  def feed(self, in_list):
    #out = sum([(x * y) for (x, y) in zip(in_list, self.w_list)]) + self.bias
    out = np.dot(in_list, self.w_list) + self.bias
    return self.step_fun(out)
  

  def feed_sigmoid(self, in_list):
    out = sum([(x * y) for (x, y) in zip(in_list, self.w_list)]) + self.bias
    return self.sigmoid(out)

  def step_fun(self, x):
    return (0 if x < 0 else 1) 

  def sigmoid(self, x):
    return (1 / (1 + np.exp(-x)))

class SumGate():

  def __init__(self):
    w_list = (1,1)
    bias = -1.5
    self.and_perceptron = FirstPerceptron(w_list, bias)

    w_list = (1,1)
    bias = -.5
    self.or_perceptron = FirstPerceptron(w_list, bias)

    w_list = (-2,-2)
    bias = 3
    self.nand_perceptron = FirstPerceptron(w_list, bias)

  # in_list = (x1,x2)
  # return (sum of two bits, carry)
  def sum(self, in_list):
    (x1,x2) = in_list
    out1 = self.nand_perceptron.feed(in_list)

    in_list2 = (x1, out1)
    out2 = self.nand_perceptron.feed(in_list2)

    in_list3 = (out1, x2)
    out3 = self.nand_perceptron.feed(in_list3)

    in_list4 = (out2,out3)
    sum = self.nand_perceptron.feed(in_list4)

    in_list5 = (out1,out1)
    carry = self.nand_perceptron.feed(in_list5)

    return (sum, carry)

'''
w_list = (1,1)
bias = -1.5
and_perceptron = FirstPerceptron(w_list, bias)

w_list = (1,1)
bias = -.5
or_perceptron = FirstPerceptron(w_list, bias)

w_list = (-2,-2)
bias = 3
nand_perceptron = FirstPerceptron(w_list, bias)

in_list = (1,0)

#print(nand_perceptron.feed(in_list))

sum_gate = SumGate()
print(sum_gate.sum(in_list))
'''
