from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import statistics
from lxml import etree
import scipy as sp
from scipy import stats
from scipy.stats import norm
import csv
from nltk.corpus import stopwords

#This defines a number of different paramaters to be set to control the threshold level 

outFile = open('Breakdown.csv', 'wb')
wr = csv.writer(outFile, quoting=csv.QUOTE_ALL)

count = dict()

Num_Deviations = 1 
Confidence_Level = 0.95

glossary = etree.parse("glossary.xml")

tfidf_vectorizer = TfidfVectorizer()

conList = []




def mean_confidence_interval(mean,sdev):
	return stats.norm.interval(Confidence_Level ,loc=mean,scale=sdev)[0]    #statistics.pstdev(conList))
	 

def term_to_term_threshold():
	

	return threshold

def concept_to_concept_threshold_word(concept):
	#print "Concept_to_Concept ", name
	
	conList = []
	docs = [concept]
	splitgroup = concept.split(' ')
	filtered1 = [w for w in splitgroup if w in stopwords.words('english')]
	filtered = [w for w in splitgroup if w not in stopwords.words('english')]
	instr = ""

	for word in splitgroup:
	    instr += (' ' + word)
	    docs.append(instr)
	 

        tfidf_matrix = tfidf_vectorizer.fit_transform(docs)
        
        matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
        #print matrix
	   
	for row in matrix:
            for x in row[1:]:
		conList.append(x)

	
	mean = statistics.mean(conList)
	stdev = statistics.pstdev(conList)

	thld = round(1 - (Num_Deviations * stdev),2)

	#print thld

	#if thld in count:
            #c = count[thld] + 1
            #count[thld] = c
        #else:
	a = float(len(filtered))
        b = float(len(splitgroup)) 
        #print a/b
	count[(a/b)] = thld
	out = [thld,len(splitgroup),len(filtered),len(filtered1)]
	wr.writerow(out)

	#thld1 = thld - abs(mean_confidence_interval(mean,stdev)) 

	#if thld == 1:
	    #return
	#print statistics.pstdev(conList)

	#print thld
	#out = [thld,thld1]
	#wr.writerow(out)
	return thld

def concept_to_concept_threshold_char(concept,name):
	#print "Concept_to_Concept ", name
	
	conList = []
	docs = [(name + concept)]
	
        for x in range(0,len(concept)):
  	    docs.append((name+concept[0:x]))

        tfidf_matrix = tfidf_vectorizer.fit_transform(docs)
        
        matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
        #print matrix
	   
	for row in matrix:
            for x in row[1:]:
		conList.append(x)

	
	mean = statistics.mean(conList)
	stdev = statistics.pstdev(conList)

	thld = 1 - (Num_Deviations * stdev)
	#print abs(mean_confidence_interval(mean,stdev))
	#thld1 = thld - abs(mean_confidence_interval(mean,stdev)) 

	#if thld == 1:
	    #return
	#print statistics.pstdev(conList)

	#print thld
	#out = [thld,thld1]
	#wr.writerow(out)
	return thld

def all_concept_list():
    
    for entry_obj in glossary.findall("Entry"): 
        for concept_obj in entry_obj.findall("Concept"):
        	all_concepts.append(concept_obj.text)

if __name__ == '__main__':
    #out = ["SoW","SoC"]
    #wr.writerow(out)
    for entry_obj in glossary.findall("Entry"): 
        term_name = entry_obj.find("Term").text.lower()
	print term_name
	#if len(entry_obj) == 2:
	    #continue
	#if term_name == '0 ary function':
	for concept_obj in entry_obj.findall("Concept"):
	    if len(concept_obj.text) < 4:
            	continue
	    else:
		w = concept_to_concept_threshold_word(concept_obj.text)
		#c = concept_to_concept_threshold_char(concept_obj.text,term_name)
	        #out = [w]
		#wr.writerow(out)
		#print count
		#print concept_obj.text
        	


	#all_concept_list()
        #tfidf_vectorizer = TfidfVectorizer()
	# tfidf_matrix = tfidf_vectorizer.fit_transform(all_concepts)
	# print tfidf_matrix.shape

	# matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
	# print matrix
    #for keys,values in count.items():
	#print keys, "-", values
	#out = [keys,values]
	#wr.writerow(out)
    print "Done!"
    outFile.close()





# from lxml import etree
# glossary = etree.parse("glossary.xml")

# detval = []
# num = 1
# for entry_obj in glossary.findall("Entry"):
#     concepts = []
#     conList = []
#     term_name = entry_obj.find("Term").text.lower()
#     #print term_name
#     #connum = 0
#     if term_name == "firewall":
# 	print term_name
#         length = 1
# 	for concept_obj in entry_obj.findall("Concept"):
# 	    #print concept_obj.text
# 	    #connum += 1
# 	    #if len(concept_obj) < 6:
#                 #continue

# 	    length += 1
# 	    #print concept_obj.text
# 	    splitgroup = concept_obj.text.split(' ')

# 	    #if len(splitgroup) < 6:
#                 #continue

# 	    concepts.append(concept_obj.text)
	    
	    
# 	    docs = [concept_obj.text]

# 	    # get each word 
# 	    instr = ""

# 	    for word in splitgroup:
# 		instr += (' ' + word)
# 		docs.append(instr)
	
# 	    tfidf_vectorizer = TfidfVectorizer()
# 	    tfidf_matrix = tfidf_vectorizer.fit_transform(docs)
# 	    #print tfidf_matrix.shape

# 	    matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
# 	    #print matrix
	   
# 	    for row in matrix:
# 		for x in row[1:]:
# 		    conList.append(x)
	    
# 	    #print (statistics.median(conList) /statistics.pstdev(conList))
# 	    #thld = statistics.median(conList) + statistics.pstdev(conList)
# 	    thld1 = 1 - (1*statistics.pstdev(conList))
# 	    thld2 = 1 - (2*statistics.pstdev(conList))
# 	    if thld1 > 1:
# 		thld = (statistics.median(conList))

# 	    detval.append(thld1)
#             #print thld1
# 	    #print thld2
# 	    num += 1

#             #break
#         #tfidf_vectorizer = TfidfVectorizer()
#         tfidf_matrix = tfidf_vectorizer.fit_transform(concepts)
# 	#print tfidf_matrix.shape

# 	matrix = cosine_similarity(tfidf_matrix[0:len(concepts)], tfidf_matrix)
# 	#print matrix
#         index = 0
#         #print 2*"\n"
# 	rnum = 1	
# 	for row in matrix: 
#             xindex = 0
# 	    for x in row:
                
# 		if x >= detval[index]:
# 		    #print index , xindex
# 		    if xindex == index:
#                         continue
# 		    else:
			
# 			#print "same"
#                         #print "Match - Row: ", row, "Value: " , x
# 			print concepts[index]
# 			print concepts[xindex]
# 		        print rnum, " Row - ", index, "Column - ", xindex, "Value needed - ",detval[index],  " Matched on - ", x
# 			rnum += 1
#                 xindex += 1       
# 	    index += 1
	    

  
# print "Done"


