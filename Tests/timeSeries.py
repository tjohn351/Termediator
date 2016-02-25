from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from lxml import etree

stopset = set(stopwords.words('english'))

# concept = 'A firewall is a part of a computer system or network that is designed to block unauthorized access while permitting authorized communications. It is a device or set of devices which is configured to permit or deny computer based application upon a set of rules and other criteria.'

tokenizer = RegexpTokenizer(r'\w+')

glossary = etree.parse("glossary.xml")

for entry_obj in glossary.findall("Entry"):

	term_name = entry_obj.find("Term").text.lower()

	words = tokenizer.tokenize(term_name)

	pattern = ""

	for w in words:
		# print w
		if w in stopset:
			pattern += "0"
		else:
			pattern += "1"

	print pattern


#http://stackoverflow.com/questions/20912364/remove-stopwords-and-tokenize-for-collocationbigramfinder-nltk
	