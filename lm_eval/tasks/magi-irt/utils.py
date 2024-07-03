import numpy as np
# use a custom process_results() function, because AGIEval can have multiple valid answers
def process_results_mcqa(doc, results):
	results = [result[0] for result in results]

	gold = doc["gold"]

	acc = 1.0 if int(np.argmax(results)) in gold else 0.0
	completion_len = np.array([float(len(i)) for i in doc["choices"]])
	acc_norm = 1.0 if int(np.argmax(results / completion_len)) in gold else 0.0

	return {
		"acc": acc,
	}
