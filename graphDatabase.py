

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

	for concetp_obj in entry_obj.findall("Concept"):

		tokenizer = RegexpTokenizer(r'\w+')

		words = tokenizer.tokenize(concetp_obj)





newTerm = gdb.nodes.create(
	uuid = uuid_num,
	termName = 
)

uuid_num += 1

newTerm.relationships.create("", newDomain)

newConcept = gdb.nodes.create()

newConcept.relationships.create("",newTerm)

#Parse 

#Built term to term Relationships 
