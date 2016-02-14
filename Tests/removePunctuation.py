from nltk.tokenize import RegexpTokenizer

concept = 'A firewall is a part of a computer system or network that is designed to block unauthorized access while permitting authorized communications. It is a device or set of devices which is configured to permit or deny computer based application upon a set of rules and other criteria.'

print len(concept)

tokenizer = RegexpTokenizer(r'\w+')
words = tokenizer.tokenize(concept)

newString = " ".join(words)

#for word in words:
    ##newString += word
    #newString += " "

print len(newString)

