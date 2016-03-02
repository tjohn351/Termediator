from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from lxml import etree
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import statistics
from scipy import stats

patterns = []

stopset = set(stopwords.words('english'))

tokenizer = RegexpTokenizer(r'\w+')

glossary = etree.parse("glossary.xml")

tags = {}

tfidf_vectorizer = TfidfVectorizer()

# outFile = open("timeseries.csv", "wb")
# wr = csv.writer(outFile, quoting=csv.QUOTE_ALL)

outFile = open("timeseries.txt", "wb")

def nucleous(s):
	docs = [s]
	instr = ""
	conList = []

	words = tokenizer.tokenize(s)

	for w in words:
		instr += (' ' + w)
		docs.append(instr)

	tfidf_matrix = tfidf_vectorizer.fit_transform(docs)
	matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
	
 	for row in matrix:	
 		for x in row[1:]:
			conList.append(x)

	mean = statistics.mean(conList)
  	conf = stats.norm.interval(0.95 ,loc=mean,scale=statistics.pstdev(conList))

  	thld = 1 - statistics.pstdev(conList)

  	return thld



for entry_obj in glossary.findall("Entry"):

	for concept_obj in entry_obj.findall("Concept"):

		concept_text = concept_obj.text.lower()

		words = tokenizer.tokenize(concept_text)

		pattern = ""


		for w in words:
			if w in stopset:
				pattern += "0"
			else:
				pattern += "1"

		if pattern == "11011":
			outFile.write(concept_text + "\n")
			outFile.write(pattern + "\n")
			outFile.write('%.7f' % nucleous(concept_text))
			outFile.write("\n")
			

		# print pattern , " - ", nucleous(concept_text), "\n"
		# if pattern == "11011":
		# if pattern not in tags:
		# 	tags[pattern] = 1
		# else:
		# 	newvalue = tags[pattern]
		# 	tags[pattern] = (newvalue + 1)
			

# for keys, values in tags.items():
# 	print keys, " - ", values



		# 	print concept_text, "\n"
		# patterns.append(pattern)


outFile.close()
# print len(set(patterns))