def doc_to_text(doc):
	if doc['source'] == 'winogrande_xl':
		idx = doc["query"].index("_")
		return doc["query"][:idx].strip()
	elif doc['source'].startswith('mmlu'):
		choices = doc['choices']
		category = doc['source'][5:].replace('-', ' ')
		prepend_str = 'The following are multiple choice questions (with answers) about '+category+'\n\n'
		return prepend_str + doc['query'].strip() + '\nA. ' + choices[0] + '\nB. ' + choices[1] + '\nC. ' + choices[2] + '\nD. ' + choices[3] + '\nAnswer:'
	elif doc['source'].startswith('agieval'):
		return doc['query']


def doc_to_target(doc):
	if doc['source'] == 'winogrande_xl':
		return doc['gold']
	elif doc['source'].startswith('mmlu'):
		return doc['gold']
	elif doc['source'].startswith('agieval'):
		return doc['gold']


def doc_to_choice(doc):
	if doc['source'] == 'winogrande_xl':
		idx = doc["query"].index("_") + 1
		options = [doc["choices"][0][4:], doc["choices"][1][4:]]
		return [opt + doc["query"][idx:] for opt in options]
	elif doc['source'].startswith('mmlu'):
		return ["A", "B", "C", "D"]
	elif doc['source'].startswith('agieval'):
		return doc['choices']
