

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

#List of each similarity nucleous 
nucleous_list = []
#List of each conept 
concept_list = []

#Build Database Elements

'''
Parses the glossary to get all of the domains
Adds a Glossaries id, origin, url, and domain to Neo4j
'''

for domain_obj in glossary.findall("GlossaryRef"):
	domain_id = domain_obj.find("").text
	origin = domain_obj.find("OriginName").text
	url    = domain_obj.find("originURL").text
	domain = domain_obj.find("origionDomain").text

	newDomain = gdb.nodes.create(
		id = ,
		originName = origin,
		originURL = url,
		origionDomain = domain
	)

'''
Parses the glossary to get each term and its associated concepts 
'''

for entry_obj in glossary.findall("GlossaryRef"):
	

	term_name = entry_obj.find("Term").text.lower()
	
	newTerm = gdb.nodes.create(
		termName = term_name
	)


	#Creats the relationship between a term and its accosiated glossary

	newTerm.relationships.create("", newDomain)


	#For each concept of term

	for concetp_obj in entry_obj.findall("Concept"):

		concept_text = concetp_obj.text

		#RegEx for removing puncutation 
		tokenizer = RegexpTokenizer(r'\w+')

		#Split the concet into individual words
		words = tokenizer.tokenize(concetp_text)

		#Creat a list of concepts 
		concept_list.append(concetp_text)

		#Creats a list of the subsets of the concept
		#Starts with the whole concept so that each subsets is compaired against the origional  
		docs = [concetp_text]

		#Empty string that each word of the concept is joind to
		concept_breakdown = ""

		for w in words:
			concept_break_down = " ".join(w)
			#Remove the first space from the subset 
			docs.append(concept_breakdown[-1:])



		tfidf_vectorizer = TfidfVectorizer()
	    tfidf_matrix = tfidf_vectorizer.fit_transform(docs)
	   
	    #The matrix of the subsets 
	    matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)

	    #The mean 
		mean = statistics.mean()

		#The 95% confidence interval
		conf = stats.norm.interval(0.95, loc=mean, scale=statistics.pstdev())

		#Calculates the nucleous for a given conept 
		threshold = 1 - (1*statistics.pstdev()) - conf[0]


		#Add the calculated nucleous to the list
		nucleous_list.append(threshold)

		#Add the concept into Neo4j 
		newConcept = gdb.nodes.create(
			uuid = uuid_num,
			threshold = 
		)

		#Update the uuid
		uuid_num += 1


#Parse 

#Built term to term Relationships 
matrix = cosine_similarity()

index = 0

for row in matrix:
	
	matrix_index = 0

	for element in matrix:
		#Skip compairing a concept to itself 
		if index == matrix_index:
			continue
		else:
			#Add concept to conept relationships 
			newConcept.relationships.create("",newTerm)
			#Incrament indexs 
			index ++
			matrix_index ++

print "Done"
