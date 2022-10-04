```python
import nltk
```


```python
text = 'the cat is sitting with the bats on the striped mat\
       under many badly flying geese. I am still '

word_list = nltk.word_tokenize(text)
print(word_list)
```

    ['the', 'cat', 'is', 'sitting', 'with', 'the', 'bats', 'on', 'the', 'striped', 'mat', 'under', 'many', 'badly', 'flying', 'geese', '.', 'I', 'am', 'still']
    


```python
text = 'My name is Robinson. \
        I am from England.\
        I am eighteen years old.\
        My father is German.\
        My mother is English.\
        I have two brothers. \
        I have one sister.\
        We are a good family.'
word_list = nltk.word_tokenize(text)
print(word_list)
```

    ['My', 'name', 'is', 'Robinson', '.', 'I', 'am', 'from', 'England', '.', 'I', 'am', 'eighteen', 'years', 'old', '.', 'My', 'father', 'is', 'German', '.', 'My', 'mother', 'is', 'English', '.', 'I', 'have', 'two', 'brothers', '.', 'I', 'have', 'one', 'sister', '.', 'We', 'are', 'a', 'good', 'family', '.']
    
