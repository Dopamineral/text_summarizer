from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tokenize import RegexpTokenizer

f = open("text.txt","r")
text = f.read()


stop_words = set(stopwords.words("english"))
tokenizer = RegexpTokenizer(r'\w+')
words = tokenizer.tokenize(text)

freq_table = dict()
for word in words:
    word = word.lower()
    if word in stop_words:
        continue
    try:
        if int(word):
            continue
    except ValueError:
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1
        
sentences = sent_tokenize(text)
sentence_value = dict()

for sentence in sentences:
    for word_value in freq_table:
        if word_value in sentence.lower():
            if sentence[:12] in sentence_value:
                sentence_value[sentence[:12]] += freq_table[word_value]
            else:
                sentence_value[sentence[:12]] = freq_table[word_value]
    space_count = sentence.count(" ")
    sentence_value[sentence[:12]] = sentence_value[sentence[:12]] / space_count
            
sum_values = 0
for sentence in sentence_value:
    sum_values += sentence_value[sentence]
average = sum_values/len(sentence_value)     
        
summary = ''
for sentence in sentences:
    if sentence[:12] in sentence_value and sentence_value[sentence[:12]] > (1.45*average):
        summary += " " + sentence
    
f2 = open("output.txt",'w')
f2.write(summary)
f2.close()
