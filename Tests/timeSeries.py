from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

stopset = set(stopwords.words('english'))

concept = 'A firewall is a part of a computer system or network that is designed to block unauthorized access while permitting authorized communications. It is a device or set of devices which is configured to permit or deny computer based application upon a set of rules and other criteria.'

tokenizer = RegexpTokenizer(r'\w+')
words = tokenizer.tokenize(concept.lower())

pattern = ""

for w in words:
	# print w
	if w in stopset:
		pattern += "B"
	else:
		pattern += "A"

print pattern


#http://stackoverflow.com/questions/20912364/remove-stopwords-and-tokenize-for-collocationbigramfinder-nltk
	