

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import statistics
import scipy as sp
from scipy import stats
from scipy.stats import norm
from lxml import etree
from nltk.tokenize import RegexpTokenizer
from neo4jrestclient.client import GraphDatabase

#Resources 

#Locations of the Neo4j Database 
gdb = GraphDatabase("http://localhost:747/db/data/")
glossary = etree.parse("glossary.xml")

#RegEx for punctuation removal 

uuid_num = 0


#Build Database Elements

#Domains 

for domain_obj in glossary.findall("GlossaryRef"):
	origin = domain_obj.find("OriginName").text
	url    = domain_obj.find("originURL").text
	domain = domain_obj.find("origionDomain").text

	newDomain = gdb.nodes.create(
		id = ,
		originName = origin,
		originURL = url,
		origionDomain = domain
	)

for entry_obj in glossary.findall("GlossaryRef"):
	term_name = entry_obj.find("Term").text.lower()
	
	newTerm = gdb.nodes.create(
		termName = term_name
	)

	newTerm.relationships.create("", newDomain)

	for concetp_obj in entry_obj.findall("Concept"):

		tokenizer = RegexpTokenizer(r'\w+')

		words = tokenizer.tokenize(concetp_obj.text)

		#newString = " ".join(words)

		concepts.append(concetp_obj.text)

		for w in words:


		newConcept = gdb.nodes.create(
			uuid = uuid_num,

		)

		uuid_num += 1


#Parse 

#Built term to term Relationships 
matrix = cosine_similarity(tfidf_matrix[], tfidf_matrix)

for row in matrix:

	if :
		continue
	else:

		newConcept.relationships.create("",newTerm)

print "Done"
