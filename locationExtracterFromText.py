# For this code to work @ commands to be executed(Command to be executed from terminal)
# Command 1: import nltk
# Command 2: nltk.download('punkt')

from nltk.tag import StanfordNERTagger

from nltk.tokenize import word_tokenize

st = StanfordNERTagger('./stanford-ner-4.0.0/classifiers/english.all.3class.distsim.crf.ser.gz', '../stanford-ner-4.0.0/stanford-ner.jar', encoding='utf-8')

text_arr = []
text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'
text_arr.append(text)
text = "I'm from Mumbai."
text_arr.append(text)

location_arr = []

for text in text_arr:
    temp = [ i.capitalize() for i in text.split(' ')]
    text = ''
    for i in temp:
        text += (i + ' ')
    print(text)
    text = text[:-1]

    tokenized_text = word_tokenize(text)
    classified_text = st.tag(tokenized_text)
    print(classified_text)
    for i in classified_text:
        if i[1] == 'LOCATION':
            location_arr.append(i[0])
print(location_arr)