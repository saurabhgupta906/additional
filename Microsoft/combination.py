def combination(prefix,suffix):
	if len(suffix) == 0:
		print (prefix)
	else:
		for i in range(0,len(suffix)):
			combination(prefix +suffix[i], suffix[0:i]+suffix[i+1:len(suffix)])



combination("","acd")