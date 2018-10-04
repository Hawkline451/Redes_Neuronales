
class FirstPerceptron(): 

  def __init__(self, w_list, bias):
    self.w_list = w_list
    self.bias = bias

  def feed_perceptron(self, in_list):
    out = sum([(x * y) for (x, y) in zip(in_list, self.w_list)]) + self.bias
    return (1 if out > 0 else 0)  

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
    out1 = self.nand_perceptron.feed_perceptron(in_list)

    in_list2 = (x1, out1)
    out2 = self.nand_perceptron.feed_perceptron(in_list2)

    in_list3 = (out1, x2)
    out3 = self.nand_perceptron.feed_perceptron(in_list3)

    in_list4 = (out2,out3)
    sum = self.nand_perceptron.feed_perceptron(in_list4)

    in_list5 = (out1,out1)
    carry = self.nand_perceptron.feed_perceptron(in_list5)

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

#print(nand_perceptron.feed_perceptron(in_list))

sum_gate = SumGate()
print(sum_gate.sum(in_list))
'''
