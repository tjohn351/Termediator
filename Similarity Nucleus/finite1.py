from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import statistics
#from scipy.stats import norm

import scipy as sp
from scipy import stats
from scipy.stats import norm

from lxml import etree
glossary = etree.parse("glossary.xml")

detval = []
num = 1
for entry_obj in glossary.findall("Entry"):
        concepts = []
        conList = []
        term_name = entry_obj.find("Term").text.lower()
    #print term_name
    #connum = 0
    #if term_name == "firewall":
	print term_name
        length = 1
	for concept_obj in entry_obj.findall("Concept"):
	    #print concept_obj.text
	    #connum += 1
	    #if len(concept_obj) < 6:
                #continue

	    length += 1
	    #print concept_obj.text
	    splitgroup = concept_obj.text.split(' ')

	    #if len(splitgroup) < 6:
                #continue

	    concepts.append(concept_obj.text)
	    
	    
	    docs = [concept_obj.text]

	    # get each word 
	    instr = ""

	    for word in splitgroup:
		instr += (' ' + word)
		docs.append(instr)
	
	    tfidf_vectorizer = TfidfVectorizer()
	    tfidf_matrix = tfidf_vectorizer.fit_transform(docs)
	    #print tfidf_matrix.shape

	    matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
	    #print matrix
	   
	    for row in matrix:
		for x in row[1:]:
		    conList.append(x)
	    
	    #print (statistics.median(conList) /statistics.pstdev(conList))
	    #thld = statistics.median(conList) + statistics.pstdev(conList)
	    mean = statistics.mean(conList)
	    conf = stats.norm.interval(0.95 ,loc=mean,scale=statistics.pstdev(conList))
	    
	    thld1 = 1 - (1*statistics.pstdev(conList)) - conf[0]
	    thld2 = 1 - (2*statistics.pstdev(conList))
	    
	    
	
	    #print thld1 - conf[0] 

	    

	    if thld1 > 1:
		thld = (statistics.median(conList))

	    detval.append(thld1)
            #print thld1
	    #print thld2
	    num += 1

            #break
        #tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform(concepts)
	#print tfidf_matrix.shape

	matrix = cosine_similarity(tfidf_matrix[0:len(concepts)], tfidf_matrix)
	#print matrix
        index = 0
        #print 2*"\n"
	rnum = 1	
	for row in matrix: 
            xindex = 0
	    for x in row:
                
		if x >= detval[index]:
		    #print index , xindex
		    if xindex == index:
                        continue
		    else:
			#x
			#print "same"
                        #print "Match - Row: ", row, "Value: " , x
			#print concepts[index]
			#print concepts[xindex]
		        print rnum, " Row - ", index, "Column - ", xindex, "Value needed - ",detval[index],  " Matched on - ", x
			rnum += 1
                xindex += 1       
	    index += 1
	    

  
print "Done"
