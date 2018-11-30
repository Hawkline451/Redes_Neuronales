import random

def fitness (input_word, test_word):
	score = 0
	i = 0
	for i in range(len(input_word)):
		score = score + 1 if (password[i] == test_word[i]) else score

	return score / len(input_word)


def generateIndividual(length):
	i = 0
	result = ""
	input_array = ["1", "0"]
	for i in range(length):
		letter = random.choice (input_array)
		result += letter
		i += 1
	return result

def generateFirstPopulation(sizePopulation, input_word):
	population = []
	i = 0
	for i in range(len(sizePopulation))
		population.append(generateIndividual(len(input_word)))
		i+=1
return population
