def number_to_words(num):
	s = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать',
	 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать',
	 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
	
	n = num%10
	if num in range(1, 21):
		print(s[num])
	if num in range(21, 30):
		print(s[20]+' '+s[n])
	if num == 30:
		print(s[21])
	if num in range(31, 40):
		print(s[21]+' '+s[n])
	if num == 40:
		print(s[22])
	if num in range(41,50):
		print(s[22]+' '+s[n])
	if num == 50:
		print(s[23])
	if num in range(51,60):
		print(s[23]+' '+s[n])
	if num == 60:
		print(s[24])
	if num in range(61,70):
		print(s[24]+' '+s[n])
	if num == 70:
		print(s[25])
	if num in range(71,80):
		print(s[25]+' '+s[n])
	if num == 80:
		print(s[26])
	if num in range(81,90):
		print(s[26]+' '+s[n])
	if num == 90:
		print(s[27])
	if num in range(91, 100):
		print(s[27]+' '+s[n])



	


number_to_words(16)
		

	
