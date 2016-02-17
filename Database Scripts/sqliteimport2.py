import sqlite3
from lxml import etree

#connect to db
conn = sqlite3.connect('/home/term/termediator/termediator/db.sqlite3')
c = conn.cursor()

glossary = etree.parse("glossary.xml")

#domain
#Found in the OriginDomain
#get all of the domains

domainList = []

for glos in glossary.findall("GlossaryRef"):
	domain = glos.find("OriginDomain").text
	if domain in domainList:
		continue
	else:
		domainList.append(domain)

x = 1
for dom in domainList:
	#insert =  'INSERT INTO dbview_domain VALUES (' + str(x) + ', \'' + dom + '\')'
	c.execute("INSERT INTO dbview_domain VALUES (?, ?);",(x,dom))
	x += 1

#print domainList.index("Graphic Designer") + 1 
#term
term_list = []
x = 1
for entry_obj in glossary.findall("Entry"):
    term_name = entry_obj.find("Term").text
    term_list.append(term_name)
    #insert = 'INSERT INTO dbview_term VALUES (' + str(x) + ', \'' + term_name + '\')'
    c.execute("INSERT INTO dbview_term VALUES (?, ?);",(x,term_name))
    x += 1

#glossary

x = 0
gls = dict()
glslist = []
for glos in glossary.findall("GlossaryRef"):
    x += 1
    glosref = glos.find("OriginName").text.replace(" ","")
    glosref = glosref.replace("'","")
    value = glos.find("OriginName").text
    #print x, value
    gls[glosref] = value
    glslist.append(value)
    #print glosref
    orinam = glos.find("OriginName").text 
    url = glos.find("OriginURL").text
    domain = glos.find("OriginDomain").text
    c.execute("INSERT INTO dbview_glossary VALUES (?, ?, ?, ?);",(x, glosref, orinam, url))
    domindex = (domainList.index(domain) + 1)
    c.execute("INSERT INTO dbview_glossary_OriginDomain VALUES (?, ?, ?);",(x, x, domindex))
    
  
#print x, len(gls) 

#print gls	
#textConcept 
x = 1
for glos in glossary.findall("Entry"):
	concept_term = glos.find("Term").text
	ct_index = (term_list.index(concept_term))+1
	for concept_obj in glos.findall("Concept"):
            concept = concept_obj.text
	    concept_glossary = gls[concept_obj.find("ConceptAnnotation").text]
	    cg_index = (glslist.index(concept_glossary))+1
	    #concept_glossary = concept_obj.find("ConceptAnnotation").text
	    c.execute("INSERT INTO dbview_textConcept VALUES (?, ?, ?, ?);",(x, concept, cg_index, ct_index))
	    x += 1
	#print concept_term, concept, concept_glossary

conn.commit()
conn.close()
