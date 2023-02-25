import spacy

""" spaCy recognises the links between monkey and banana, and between cat and monkey. """

nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

""" spaCy again recognises the similarities between monkey/cat and apple/banana."""

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

""" spaCy again links comparable types by identifying cat/dog as well as the car; so a sentence containing
 both a vehicle and an animal rates higher."""

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

""" Using 'en_core_web_sm' instead of 'en_core_web_md' produces similarities but with a smaller confidence ratio."""
