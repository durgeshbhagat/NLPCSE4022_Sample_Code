import nltk

text = 'the cat is sitting with the bats on the striped mat\
       under many badly flying geese. I am still '

word_list = nltk.word_tokenize(text)
print(word_list)

['the', 'cat', 'is', 'sitting', 'with', 'the', 'bats',\
 'on', 'the', 'striped', 'mat', 'under', 'many', 'badly',\
 'flying', 'geese', '.', 'I', 'am', 'still']