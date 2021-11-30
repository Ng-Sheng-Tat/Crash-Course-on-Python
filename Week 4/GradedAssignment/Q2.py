def highlight_word(sentence, word):
	sentence = sentence.replace(word, word.upper()) 
	return sentence

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
