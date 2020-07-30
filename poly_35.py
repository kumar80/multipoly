import itertools
import copy
import random
import time
import numpy as np

start_time = time.time()

x1 = []
x2 = []
x  = []
degree_1_term=10
for i in range(1,36):
	ch = 'x'+str(i)
	if(i>degree_1_term):
		x2.append(ch)
	else:
		x1.append(ch)
	x.append(ch)


def get_polynomial(vars, power):
	
	if "c" in vars:
		raise Exception("\"c\" cannot be a variable")
	
	vars.append("c") # add dummy variable
	
	# compute all combinations of variables
	terms = []
	for x in itertools.combinations_with_replacement(vars, power):
		terms.append(x)
	
	# get rid of "c" terms
	terms = map(list, terms)
	for i in xrange(len(terms)):
		while "c" in terms[i]:
			terms[i].remove("c")
 
	return terms
 

terms1 = get_polynomial(x1, 1)
terms1.pop(len(terms1) -1)

terms = get_polynomial(x2, 3)
terms.pop(len(terms) -1)

x1.pop(len(x1) -1)
x2.pop(len(x2) -1)

len1 = len(terms)
len2 = len(terms1)

for i in range(len1):
	if(len(terms[i])<3 and len(terms[i])>0):
		for j in range(len2):
			 temp = copy.deepcopy(terms[i])
			 temp.append(terms1[j][0])
			 terms.append(temp)
		terms.pop(i)			

for j in range(len2):
	terms.append(terms1[j])


len1=len(terms)
sum=0
expr=""

eq = []
c = []
for i in range(0,10):
	mydict ={}
	idx=0
	multiv_poly =[]
	mydict2 = {}
	for item in x2:
		mydict[item] = random.randint(0,1) 
		idx+=1 
	for item in x1:
		mydict2[item] = 0
	expr=""
	constant_term=[0]
	for j in range(len1):
		len2 = len(terms[j])
		r=random.randint(0,1)
		val=1
		temp_expr=""
		temp_list = []
		coeff = 0
		if(r==1):
			for k in range(len2):
				temp_expr+=terms[j][k]
			
				if terms[j][k] in mydict:
					val=val*mydict[terms[j][k]]
					coeff=1
				else:
					temp_list.append(terms[j][k])
			if len(temp_list)>0:
				mydict2[temp_list[0]]+=val;
				temp_list.append(val)
			if len(temp_list) > 0:
				multiv_poly.append(temp_list)
			else:
				constant_term[0] = constant_term[0] + val
			if len(expr)>0:
				expr=expr + '+' + temp_expr 
			else:
				expr=temp_expr
	li = []		
	for item in x1:
		li.append(mydict2[item]%2)
	eq.append(li)
	c.append((constant_term[0]%2))

	multiv_poly.append(constant_term)


a = np.array(eq)
b = np.array(c);

_det = np.linalg.det(a)
det =  int(round(_det))

print expr
print a
print b
if det%2!=0:
	x = np.linalg.solve(a,b)
	for i in range(len(x)):
		x[i]*=_det
		x[i]=int(round(x[i]))
		x[i]=((x[i]%2)+2)%2
	print x.astype(int)
else:
	print "Determinant is 0"
			

print("--- %s seconds ---" % (time.time() - start_time))
