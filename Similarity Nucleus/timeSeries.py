from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from lxml import etree

patterns = []

stopset = set(stopwords.words('english'))

tokenizer = RegexpTokenizer(r'\w+')

glossary = etree.parse("glossary.xml")

for entry_obj in glossary.findall("Entry"):

	for concept_obj in entry_obj.findall("Concept"):

		concept_text = concept_obj.text.lower()

		words = tokenizer.tokenize(concept_text)

		pattern = ""

		for w in words:
			# print w
			if w in stopset:
				pattern += "0"
			else:
				pattern += "1"

		if pattern == "11011":
			print concept_text, "\n"
		# patterns.append(pattern)


# print len(set(patterns))