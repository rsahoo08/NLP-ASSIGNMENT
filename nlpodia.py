Python 3.8.6rc1 (tags/v3.8.6rc1:08bd63d, Sep  7 2020, 22:55:24) [MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> nltk.download('popular')
[nltk_data] Downloading collection 'popular'
[nltk_data]    | 
[nltk_data]    | Downloading package cmudict to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package cmudict is already up-to-date!
[nltk_data]    | Downloading package gazetteers to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Unzipping corpora\gazetteers.zip.
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
[nltk_data]    |   Unzipping corpora\shakespeare.zip.
[nltk_data]    | Downloading package stopwords to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package stopwords is already up-to-date!
[nltk_data]    | Downloading package treebank to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Unzipping corpora\treebank.zip.
[nltk_data]    | Downloading package twitter_samples to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Unzipping corpora\twitter_samples.zip.
[nltk_data]    | Downloading package omw to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Unzipping corpora\omw.zip.
[nltk_data]    | Downloading package wordnet to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Unzipping corpora\wordnet.zip.
[nltk_data]    | Downloading package wordnet_ic to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Unzipping corpora\wordnet_ic.zip.
[nltk_data]    | Downloading package words to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Unzipping corpora\words.zip.
[nltk_data]    | Downloading package maxent_ne_chunker to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Unzipping chunkers\maxent_ne_chunker.zip.
[nltk_data]    | Downloading package punkt to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Package punkt is already up-to-date!
[nltk_data]    | Downloading package snowball_data to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    | Downloading package averaged_perceptron_tagger to
[nltk_data]    |     C:\Users\Rahul1\AppData\Roaming\nltk_data...
[nltk_data]    |   Unzipping taggers\averaged_perceptron_tagger.zip.
[nltk_data]    | 
[nltk_data]  Done downloading collection popular
True
>>> import nltk
>>> odia_text="""ସବୁ ମନୁଷ୍ୟ ଜନ୍ମକାଳରୁ ସ୍ୱାଧୀନ. ସେମାନଙ୍କର ମର୍ଯ୍ୟାଦା ଓ ଅଧିକାର ସମାନ."""
>>> tokens=nltk.word_tokenize(odia_text)
>>> print(tokens)
['ସବୁ', 'ମନୁଷ୍ୟ', 'ଜନ୍ମକାଳରୁ', 'ସ୍ୱାଧୀନ', '.', 'ସେମାନଙ୍କର', 'ମର୍ଯ୍ୟାଦା', 'ଓ', 'ଅଧିକାର', 'ସମାନ', '.']
>>> nltk.pos_tag(tokens)
[('ସବୁ', 'JJ'), ('ମନୁଷ୍ୟ', 'NNP'), ('ଜନ୍ମକାଳରୁ', 'NNP'), ('ସ୍ୱାଧୀନ', 'NNP'), ('.', '.'), ('ସେମାନଙ୍କର', 'VB'), ('ମର୍ଯ୍ୟାଦା', 'JJ'), ('ଓ', 'NNP'), ('ଅଧିକାର', 'NNP'), ('ସମାନ', 'NNP'), ('.', '.')]






