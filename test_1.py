import clase_1
import unittest

class Test1(unittest.TestCase):

    def test_and(self):
        w_list = (1,1)
        bias = -1.5
        and_perceptron = clase_1.FirstPerceptron(w_list, bias)
        
        result_1_1 = and_perceptron.feed_perceptron((1,1))
        result_1_0 = and_perceptron.feed_perceptron((1,0))
        result_0_1 = and_perceptron.feed_perceptron((0,1))
        result_0_0 = and_perceptron.feed_perceptron((0,0))

        result = (result_1_1, result_1_0, result_0_1, result_0_0)
        self.assertEqual(result, (1, 0, 0, 0))
    
    def test_or(self):
        w_list = (1,1)
        bias = -.5
        or_perceptron = clase_1.FirstPerceptron(w_list, bias)
        
        result_1_1 = or_perceptron.feed_perceptron((1,1))
        result_1_0 = or_perceptron.feed_perceptron((1,0))
        result_0_1 = or_perceptron.feed_perceptron((0,1))
        result_0_0 = or_perceptron.feed_perceptron((0,0))

        result = (result_1_1, result_1_0, result_0_1, result_0_0)
        self.assertEqual(result, (1, 1, 1, 0))

    def test_nand(self):
        w_list = (-2,-2)
        bias = 3
        nand_perceptron = clase_1.FirstPerceptron(w_list, bias)
        
        result_1_1 = nand_perceptron.feed_perceptron((1,1))
        result_1_0 = nand_perceptron.feed_perceptron((1,0))
        result_0_1 = nand_perceptron.feed_perceptron((0,1))
        result_0_0 = nand_perceptron.feed_perceptron((0,0))

        result = (result_1_1, result_1_0, result_0_1, result_0_0)
        self.assertEqual(result, (0, 1, 1, 1))

    def test_sum_gate(self):
        sum_gate = clase_1.SumGate()

        result = sum_gate.sum((1,1))
        # result = (sum, carry)
        self.assertEqual(result, (0,1))
 
        result = sum_gate.sum((1,0))
        self.assertEqual(result, (1,0))
         
        result = sum_gate.sum((0,1))
        self.assertEqual(result, (1,0))
         
        result = sum_gate.sum((0,0))
        self.assertEqual(result, (0,0))


if __name__ == '__main__':
    unittest.main()
