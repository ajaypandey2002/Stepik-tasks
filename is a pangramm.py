def is_pangram(text):
	text =  text.lower()
	count = 0
	s = []
	abc = 'qwertyuiopasdfghjklzxcvbnm'
	text = text.split(' ')
	
	for i in range(len(text)):
		for j in range(len(text[i])):
			if text[i][j] in abc and text[i][j] not in s:
				count += 1
				s.append(text[i][j])

	if count == len(abc):
		return True
	else:
		return False
text = 'ajay is great'
print(is_pangram(text))


