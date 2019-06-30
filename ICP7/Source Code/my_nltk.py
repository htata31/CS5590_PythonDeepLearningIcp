import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk import ne_chunk
from collections import Counter
ps = PorterStemmer()

lemmatizer = WordNetLemmatizer()
text = open('data.txt', encoding="utf8").read()

# tokenization
w_tokens =word_tokenize(text)
s_tokens = sent_tokenize(text)
print("----------Word tokens")
print(w_tokens)
print("\n")
print("---------Sentence tokens")
print(s_tokens)
print("\n")

# trigram
trigrams = ngrams(w_tokens,3)
print("---------- trigrams")
print(list(trigrams))
print("\n")

# Lemmatization
lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in w_tokens])
print("----------Lemmatization")
print(lemmatized_output)
print("\n")

# Stemming
stemmed_output = ' '.join([ps.stem(w) for w in w_tokens])
print("-------Stemming")
print(stemmed_output)
print("\n")

# POS
n_pos = nltk.pos_tag(w_tokens)
print("Parts of Speech :", n_pos)

# NOR
print("\n")
noe = ne_chunk(n_pos)
# print("Named Entity Recognition :", noe)