import re , pprint
#buscar musicas

f = open( "goear.com" ,  "r+" )

a =  f.read()

b = re.findall( "(\d*)\Waudios</a>" , a )

pprint.pprint( b )