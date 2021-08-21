import re

from collections import deque
  
def getIndex(s, i):
  
	if s[i] != '(':
		return -1
  
	d = deque()
  
	for k in range(i, len(s)):
  
		if s[k] == ')':
			d.popleft()
  
		elif s[k] == '(':
			d.append(s[i])
  
		if not d:
			return k
  
	return -1

def bracket(s,pos,n,opn,close):
	if close == n :
		string = ""
		for i in s:
			string = string + i
		lst.append(string)
		return
	else :
		if opn > close : 
			s[pos]=')'
			bracket(s, pos + 1, n, opn, close + 1)

		if(opn < n):
			s[pos] = '('
			bracket(s, pos + 1, n, opn + 1, close)

def remove_bracket(s):
	s = s.replace('(','')
	s = s.replace(')','')
	return s

source_code = open("sample.c").read().split('\n')
number_of_lines_of_code = len(source_code)

z = 1

for i in range(number_of_lines_of_code) :
	if "if" in source_code[i] :
		text = source_code[i][(source_code[i].find("if")+2):]
		first_open_bracket = text.find("(")
		last_close_bracket = getIndex(text,first_open_bracket)
		text1 = text[first_open_bracket+1:last_close_bracket]
		text1 = remove_bracket(text1)
		temp = text1
		delimiters = "&&" , "||"
		regexPattern = '|'.join(map(re.escape, delimiters))
		conditions = re.split(regexPattern, text1)
		print conditions
		for sub in conditions:
			temp = temp.replace(sub, ' ')
		operators = temp.split()
		print operators
		for c in range(len(conditions)):
			if '!' in conditions[c] :
				last_index_of_not_operator = conditions[c].rindex('!')
				conditions[c] = conditions[c][:last_index_of_not_operator+1] + "(" + conditions[c][last_index_of_not_operator+1:] + ")"
			else :
				conditions[c] = "(" + conditions[c][:] + ")"
		print conditions
		n = len(conditions)
		s = [""] * 2 * n
		lst=[]
		lst2=[]
		bracket(s, 0, n, 0, 0)
		print lst
		for strg in lst :
			str1 = "("
			str1 = str1 + conditions[0]
			j = 1
			k = 0
			for c in strg[1:] :
				if c == '(' :
					str1 = str1 + operators[k]
					k = k + 1
					str1 = str1 + "("
					str1 = str1 + conditions[j]
					j = j + 1
				else :
					str1 = str1 + ")"

			lst2.append(str1)
			print str1

		for strg in lst :
			str2 = "("
			j = 0
			k = 0
			p = 1
			for c in strg[1:] :
				if c == ')' and p < len(strg)-1 :
					str2 = str2 + conditions[j]
					j = j + 1
					str2 = str2 + ")"
					str2 = str2 + operators[k]
					k = k + 1
				elif c == ')' and p == len(strg)-1 :
					str2 = str2 + conditions[j]
					j = j + 1
					str2 = str2 + ")"
				else :
					str2 = str2 + "("
				p = p + 1
	
			lst2.append(str2)
			print str2

		final_lst = []
		for elm in lst2:
			if elm not in final_lst:
				final_lst.append(elm)

		print len(final_lst)

		for l in final_lst :

			output_file = open("sample_m"+str(z)+".c","w")
					
			for p in range(0,len(source_code)) :
				if p == i : 
					timmed_length = source_code[i].find("if")+2
					line = source_code[i][:first_open_bracket+timmed_length+1]+l+source_code[i][last_close_bracket+timmed_length:]
					output_file.write(line+"\n")
				else :
					output_file.write(source_code[p]+"\n")

			output_file.close()
			z = z + 1		
		
		 
