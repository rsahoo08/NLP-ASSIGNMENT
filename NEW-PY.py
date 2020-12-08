Python 3.8.6rc1 (tags/v3.8.6rc1:08bd63d, Sep  7 2020, 22:55:24) [MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> from nltk.tokenize import sent_tokenize
>>> nltk.download('popular')
[nltk_data] Downloading collection 'popular'
[nltk_data]    | 
[nltk_data]    | Downloading package cmudict to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package cmudict is already up-to-date!
[nltk_data]    | Downloading package gazetteers to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package gazetteers is already up-to-date!
[nltk_data]    | Downloading package genesis to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package genesis is already up-to-date!
[nltk_data]    | Downloading package gutenberg to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package gutenberg is already up-to-date!
[nltk_data]    | Downloading package inaugural to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package inaugural is already up-to-date!
[nltk_data]    | Downloading package movie_reviews to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package movie_reviews is already up-to-date!
[nltk_data]    | Downloading package names to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package names is already up-to-date!
[nltk_data]    | Downloading package shakespeare to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package shakespeare is already up-to-date!
[nltk_data]    | Downloading package stopwords to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package stopwords is already up-to-date!
[nltk_data]    | Downloading package treebank to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package treebank is already up-to-date!
[nltk_data]    | Downloading package twitter_samples to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package twitter_samples is already up-to-date!
[nltk_data]    | Downloading package omw to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package omw is already up-to-date!
[nltk_data]    | Downloading package wordnet to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package wordnet is already up-to-date!
[nltk_data]    | Downloading package wordnet_ic to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package wordnet_ic is already up-to-date!
[nltk_data]    | Downloading package words to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package words is already up-to-date!
[nltk_data]    | Downloading package maxent_ne_chunker to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package maxent_ne_chunker is already up-to-date!
[nltk_data]    | Downloading package punkt to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package punkt is already up-to-date!
[nltk_data]    | Downloading package snowball_data to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package snowball_data is already up-to-date!
[nltk_data]    | Downloading package averaged_perceptron_tagger to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package averaged_perceptron_tagger is already up-
[nltk_data]    |       to-date!
[nltk_data]    | 
[nltk_data]  Done downloading collection popular
True
>>> odia_text="""ସବୁ ମନୁଷ୍ୟ ଜନ୍ମକାଳରୁ ସ୍ୱାଧୀନ. ସେମାନଙ୍କର ମର୍ଯ୍ୟାଦା ଓ ଅଧିକାର ସମାନ."""
>>> from nltk.tokenize import sent_tokenize
>>> tokenized_text=sent_tokenize(odia_text)
>>> print(tokenized_text)
['ସବୁ ମନୁଷ୍ୟ ଜନ୍ମକାଳରୁ ସ୍ୱାଧୀନ.', 'ସେମାନଙ୍କର ମର୍ଯ୍ୟାଦା ଓ ଅଧିକାର ସମାନ.']
>>> from nltk.probability import FreqDist
>>> fdist = FreqDist(odia_text)
>>> from nltk.tokenize import word_tokenize
>>> tokenized_word=word_tokenize(odia_text)
>>> print(tokenized_word)
['ସବୁ', 'ମନୁଷ୍ୟ', 'ଜନ୍ମକାଳରୁ', 'ସ୍ୱାଧୀନ', '.', 'ସେମାନଙ୍କର', 'ମର୍ଯ୍ୟାଦା', 'ଓ', 'ଅଧିକାର', 'ସମାନ', '.']
>>>  from nltk.probability import FreqDist
 
SyntaxError: unexpected indent
>>> fdist = FreqDist(tokenized_word)
>>> print(fdist)
<FreqDist with 10 samples and 11 outcomes>
>>> import matplotlib.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
>>> fdist.most_common(2)
[('.', 2), ('ସବୁ', 1)]
>>> from nltk.corpus import stopwords
>>> stop_words=set(stopwords.words("english"))
>>> stop_words=set(stopwords.words(tokenized_word))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    stop_words=set(stopwords.words(tokenized_word))
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordlist.py", line 23, in words
    for line in line_tokenize(self.raw(fileids))
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordlist.py", line 32, in raw
    return concat([self.open(f).read() for f in fileids])
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordlist.py", line 32, in <listcomp>
    return concat([self.open(f).read() for f in fileids])
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\api.py", line 208, in open
    stream = self._root.join(file).open(encoding)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\data.py", line 337, in join
    return FileSystemPathPointer(_path)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\compat.py", line 41, in _decorator
    return init_func(*args, **kwargs)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\data.py", line 315, in __init__
    raise IOError("No such file or directory: %r" % _path)
OSError: No such file or directory: 'C:\\Users\\Rahul1\\AppData\\Roaming\\nltk_data\\corpora\\stopwords\\ସବୁ'
>>> stop_words=set(stopwords.words("ଜନ୍ମକାଳରୁ"))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    stop_words=set(stopwords.words("ଜନ୍ମକାଳରୁ"))
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordlist.py", line 23, in words
    for line in line_tokenize(self.raw(fileids))
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordlist.py", line 32, in raw
    return concat([self.open(f).read() for f in fileids])
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordlist.py", line 32, in <listcomp>
    return concat([self.open(f).read() for f in fileids])
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\api.py", line 208, in open
    stream = self._root.join(file).open(encoding)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\data.py", line 337, in join
    return FileSystemPathPointer(_path)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\compat.py", line 41, in _decorator
    return init_func(*args, **kwargs)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\data.py", line 315, in __init__
    raise IOError("No such file or directory: %r" % _path)
OSError: No such file or directory: 'C:\\Users\\Rahul1\\AppData\\Roaming\\nltk_data\\corpora\\stopwords\\ଜନ୍ମକାଳରୁ'
>>> stop_words=set(stopwords.words('ଜନ୍ମକାଳରୁ'))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    stop_words=set(stopwords.words('ଜନ୍ମକାଳରୁ'))
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordlist.py", line 23, in words
    for line in line_tokenize(self.raw(fileids))
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordlist.py", line 32, in raw
    return concat([self.open(f).read() for f in fileids])
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordlist.py", line 32, in <listcomp>
    return concat([self.open(f).read() for f in fileids])
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\api.py", line 208, in open
    stream = self._root.join(file).open(encoding)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\data.py", line 337, in join
    return FileSystemPathPointer(_path)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\compat.py", line 41, in _decorator
    return init_func(*args, **kwargs)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\data.py", line 315, in __init__
    raise IOError("No such file or directory: %r" % _path)
OSError: No such file or directory: 'C:\\Users\\Rahul1\\AppData\\Roaming\\nltk_data\\corpora\\stopwords\\ଜନ୍ମକାଳରୁ'
>>> from nltk.corpus import stopwords
>>> stop_words=set(stopwords.words("odia"))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    stop_words=set(stopwords.words("odia"))
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordlist.py", line 23, in words
    for line in line_tokenize(self.raw(fileids))
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordlist.py", line 32, in raw
    return concat([self.open(f).read() for f in fileids])
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordlist.py", line 32, in <listcomp>
    return concat([self.open(f).read() for f in fileids])
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\api.py", line 208, in open
    stream = self._root.join(file).open(encoding)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\data.py", line 337, in join
    return FileSystemPathPointer(_path)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\compat.py", line 41, in _decorator
    return init_func(*args, **kwargs)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\data.py", line 315, in __init__
    raise IOError("No such file or directory: %r" % _path)
OSError: No such file or directory: 'C:\\Users\\Rahul1\\AppData\\Roaming\\nltk_data\\corpora\\stopwords\\odia'
>>> stop_words=set(stopwords.words("english"))
>>> stop_words=set(stopwords.words("or"))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    stop_words=set(stopwords.words("or"))
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordlist.py", line 23, in words
    for line in line_tokenize(self.raw(fileids))
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordlist.py", line 32, in raw
    return concat([self.open(f).read() for f in fileids])
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordlist.py", line 32, in <listcomp>
    return concat([self.open(f).read() for f in fileids])
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\api.py", line 208, in open
    stream = self._root.join(file).open(encoding)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\data.py", line 337, in join
    return FileSystemPathPointer(_path)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\compat.py", line 41, in _decorator
    return init_func(*args, **kwargs)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\data.py", line 315, in __init__
    raise IOError("No such file or directory: %r" % _path)
OSError: No such file or directory: 'C:\\Users\\Rahul1\\AppData\\Roaming\\nltk_data\\corpora\\stopwords\\or'
>>> stop_words=set(stopwords.words("english"))
>>> print(stop_words)
{'do', 'does', "mightn't", 'my', 'but', 'mightn', 'only', 'after', 'those', 'y', 'own', 'any', 've', "you've", 'that', 'are', 'above', 'this', 'under', "shouldn't", "don't", 'them', 'is', 'to', 'where', 'shouldn', "shan't", 'each', 'haven', 'too', 'more', 'yours', 'himself', 'because', 'same', 'couldn', 'won', 'her', 'most', 'down', 'mustn', "weren't", 'what', "didn't", "doesn't", 'until', "wouldn't", 'no', 'into', 'being', 'while', 'should', 'm', 're', 'didn', 'hers', 'she', 'such', 'how', 'which', "should've", "it's", 'needn', 'your', "that'll", 'against', 'theirs', "you'd", 'a', 'nor', 'there', 'wasn', 'these', 't', "isn't", 'up', "she's", 'at', "hasn't", "won't", 'had', 'who', 'with', 'our', 'been', 'he', 'themselves', 'his', 'further', 'below', 's', 'hasn', 'both', 'it', 'we', 'herself', 'in', "wasn't", 'from', 'were', 'aren', 'just', "you'll", 'their', 'ourselves', 'yourselves', 'as', 'the', 'him', 'will', 'weren', 'yourself', 'i', 'an', 'before', 'ain', 'its', 'be', 'was', "needn't", 'off', 'between', 'during', 'll', 'having', 'over', 'on', 'me', 'about', "couldn't", 'doing', 'whom', 'not', 'am', 'through', 'or', 'other', 'of', 'doesn', 'has', 'then', 'don', "you're", "haven't", 'myself', "mustn't", 'once', 'when', 'isn', 'have', 'by', 'hadn', 'here', 'all', 'now', 'can', 'shan', 'ours', 'some', 'than', 'wouldn', 'out', 'for', "hadn't", 'o', 'again', 'very', 'did', 'so', "aren't", 'why', 'they', 'itself', 'if', 'd', 'few', 'and', 'ma', 'you'}
>>> stop_words=set(stopwords.words("odiaroman"))
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    stop_words=set(stopwords.words("odiaroman"))
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordlist.py", line 23, in words
    for line in line_tokenize(self.raw(fileids))
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordlist.py", line 32, in raw
    return concat([self.open(f).read() for f in fileids])
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordlist.py", line 32, in <listcomp>
    return concat([self.open(f).read() for f in fileids])
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\api.py", line 208, in open
    stream = self._root.join(file).open(encoding)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\data.py", line 337, in join
    return FileSystemPathPointer(_path)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\compat.py", line 41, in _decorator
    return init_func(*args, **kwargs)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\data.py", line 315, in __init__
    raise IOError("No such file or directory: %r" % _path)
OSError: No such file or directory: 'C:\\Users\\Rahul1\\AppData\\Roaming\\nltk_data\\corpora\\stopwords\\odiaroman'
>>> filtered_sent=[]
>>> for ସବୁ in tokenized_sent:
	if ସବୁ  not in stop_words:
        filtered_sent.append(ସବୁ)
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> filtered_sent=[]
>>> for ସବୁ in tokenized_sent:
	if ସବୁ  not in stop_words:
        filtered_sent.append(ସବୁ):
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> print("Tokenized Sentence:",tokenized_sent)
print("Filterd Sentence:",filtered_sent)
SyntaxError: multiple statements found while compiling a single statement
>>> from nltk.stem import PorterStemmer
>>> from nltk.tokenize import sent_tokenize, word_tokenize

>>> ps = PorterStemmer()
>>> stemmed_words=[]
>>> for ସବୁ in filtered_sent:
	stemmed_words.append(ps.stem(w))
	print("Filtered Sentence:",filtered_sent)
print("Stemmed Sentence:",stemmed_words)
SyntaxError: invalid syntax
>>> from nltk.stem.wordnet import WordNetLemmatizer
>>> lem = WordNetLemmatizer()
>>> from nltk.stem.porter import PorterStemmer
>>> stem = PorterStemmer()
>>> word = "ସେମାନଙ୍କର"
>>> print("Lemmatized Word:",lem.lemmatize(word,"ମାନ"))
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print("Lemmatized Word:",lem.lemmatize(word,"ମାନ"))
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\stem\wordnet.py", line 38, in lemmatize
    lemmas = wordnet._morphy(word, pos)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordnet.py", line 1873, in _morphy
    exceptions = self._exception_map[pos]
KeyError: 'ମାନ'
>>> print("Stemmed Word:",stem.stem(word))
Stemmed Word: ସେମାନଙ୍କର
>>> print("Lemmatized Word:",lem.lemmatize(word,"ତା"))
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print("Lemmatized Word:",lem.lemmatize(word,"ତା"))
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\stem\wordnet.py", line 38, in lemmatize
    lemmas = wordnet._morphy(word, pos)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordnet.py", line 1873, in _morphy
    exceptions = self._exception_map[pos]
KeyError: 'ତା'
>>> print("Lemmatized Word:",lem.lemmatize(word,"ସେମାନଙ୍କର"))
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print("Lemmatized Word:",lem.lemmatize(word,"ସେମାନଙ୍କର"))
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\stem\wordnet.py", line 38, in lemmatize
    lemmas = wordnet._morphy(word, pos)
  File "C:\Users\Rahul1\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\corpus\reader\wordnet.py", line 1873, in _morphy
    exceptions = self._exception_map[pos]
KeyError: 'ସେମାନଙ୍କର'
>>> 