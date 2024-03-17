import rdflib

# create a Graph
g = rdflib.Graph()

# parse in an RDF file hosted on the Internet
result = g.parse("./IATA-1R-DM-Ontology.ttl", format='ttl')

for stmt in g:
    print(stmt)
