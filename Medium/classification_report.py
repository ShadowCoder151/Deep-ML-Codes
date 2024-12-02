
def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
	TP, TN, FP, FN = 0, 0, 0, 0
	for i in range(len(actual)):
		if actual[i] == 1 and predicted[i] == 1:
			TP += 1
		elif actual[i] == 1 and predicted[i] == 0:
			FN += 1
		elif actual[i] == 0 and predicted[i] == 1:
			FP += 1
		else:
			TN += 1

		confusion_matrix = [[TP, FN], [FP, TN]]

		accuracy = (TP + TN) / len(actual)
		precision = TP / (TP + FP) if (TP + FP) != 0 else 0
		recall = TP / (TP + FN) if (TP + FN) != 0 else 0

		f1 = 2 * precision * recall / (precision + recall) if (precision + recall) != 0 else 0

		specificity = TN / (TN + FP) if (TN + FP) != 0 else 0
		negativePredictive = TN / (FN + TN) if (FN + TN) != 0 else 0

	
	return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)


actual = [1, 0, 1, 0, 1]
predicted = [1, 0, 0, 1, 1]
print(performance_metrics(actual, predicted))