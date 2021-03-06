'''
'''
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import statistics
# import scipy as sp
# from scipy import stats
# from scipy.stats import norm
from lxml import etree
# from nltk.tokenize import RegexpTokenizer
from neo4jrestclient.client import GraphDatabase

#Resources 

#Locations of the Neo4j Database 
gdb = GraphDatabase("http://localhost:7474/db/data/")
#location of the glossary 
glossary = etree.parse("glossary.xml")

#RegEx for punctuation removal 
punct = r'\w+'
#uuid for terms
uuid_num = 0

#List of each similarity nucleous 
nucleous_list = []
#List of each conept 
concept_list = []

#defines a unique term to term relationship, key value pairs
unique_termtoterm = {}

#Build Database Elements

#Parses the glossary to get all of the domains
#Adds a Glossaries id, origin, url, and domain to Neo4j

for domain_obj in glossary.findall("GlossaryRef"):

	domain_id = domain_obj.get("id")
	origin = domain_obj.find("OriginName").text
	url    = domain_obj.find("OriginURL").text
	domain = domain_obj.find("OriginDomain").text

	newDomain = gdb.nodes.create(
		originId = domain_id,
		originName = origin,
		originURL = url,
		originDomain = domain
	)

	newDomain.labels.add("Domain")

# #Parses the glossary to get each term and its associated concepts 
for entry_obj in glossary.findall("Entry"):
	
	term_name = entry_obj.find("Term").text.lower()
	
	newTerm = gdb.nodes.create(
		termName = term_name,
		termLength = len(term_name.split(' '))
	)

	newTerm.labels.add("Term")

	#Creats the relationship between a term and its accosiated glossary
	newTerm.relationships.create("", )  #coneptannotation 

	#For each concept of term
	for concept_obj in entry_obj.findall("Concept"):

		concept_text = concept_obj.text

		#RegEx for removing puncutation 
		tokenizer = RegexpTokenizer(punct)

		#Split the concet into individual words
		words = tokenizer.tokenize(concept_text)

		#Creat a list of concepts 
		concept_list.append(concept_text)

		#Creats a list of the subsets of the concept
		#Starts with the whole concept so that each subsets is compaired against the origional  
		docs = [concept_text]

		#Empty string that each word of the concept is joind to
		concept_breakdown = ""

		for w in words:
			concept_break_down = " ".join(w)
			#Remove the first space from the subset 
			docs.append(concept_breakdown[-1:])

		#transform the subsets into a vectorized matrix
		tfidf_vectorizer = TfidfVectorizer()
	    tfidf_matrix = tfidf_vectorizer.fit_transform(docs)
	   
	    #The matrix of the subsets just look at the elements after the first
	    matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)

	    #Parse the first row of the matrix
	    for row in matrix:
	    	for x in row[1:]:
	    		conList.append(x)

	    #The mean 
		mean = statistics.mean(conList)

		#The 95% confidence interval
		conf = stats.norm.interval(0.95, loc=mean, scale=statistics.pstdev(conList))

		#Calculates the nucleous for a given conept 
		threshold = 1 - (1*statistics.pstdev()) - conf[0]

		#Add the calculated nucleous to the list
		nucleous_list.append(threshold)

		#Add the concept into Neo4j 
		newConcept = gdb.nodes.create(
			uuid = uuid_num,
			threshold = threshold,
			conceptLength = len(words)
		)

		#Update the uuid
		uuid_num += 1

#Parse 

#Built term to term Relationships 
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform()
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
			newConcept.relationships.create("",)

			if in unique_termtoterm:
				continue
			else:
				.relationships.create()
				unique_termtoterm.append()

			#Incrament colum index 
			matrix_index ++

	#Increment row index
	index ++

print "Done"