import re
from lxml import etree

# def clean_concept(con):
	



glossary = etree.parse("glossary.xml")

wordList = []

for entry_obj in glossary.findall("Entry"):

	for concept_obj in entry_obj.findall("Concept"):

		
		# concept_text = re.sub('[.,();"\']','',concept_obj.text.lower())
		concept_text = concept_obj.text.lower()

		words = concept_text.split(' ')

		for w in words: 
			
			wordList.append(w)

# print len(wordList)
# print len(set(wordList))

for x in wordList:
	print x


