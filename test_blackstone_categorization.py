import spacy

# Load the model
nlp = spacy.load("en_blackstone_proto")

def get_top_cat(doc):
    """
    Function to identify the highest scoring category
    prediction generated by the text categoriser. 
    """
    cats = doc.cats
    max_score = max(cats.values()) 
    max_cats = [k for k, v in cats.items() if v == max_score]
    max_cat = max_cats[0]
    return (max_cat, max_score)

text = "The witness, senior vice-president and controller at R. J. Reynolds Tobacco Holding Inc., was deposed by the plaintiffs. He described the financial status of the holding company and its economic activities. He indicated that industry changes, corporate changes, market changes, structural changes, and some legal developments have all had an adverse effect on the profitability of the company. The witness also noted that advertising and promotion restrictions placed on them in 1998 by the Master Settlement Agreement had caused a drop in sales volume. He said that punitive damage awards would have a devastating effect on the company, although he declined to say whether bankruptcy was being considered."

# Apply the model to the text
doc = nlp(text)

# Get the sentences in the passage of text
sentences = [sent.text for sent in doc.sents]

# Print the sentence and the corresponding predicted category.
for sentence in sentences:
    doc = nlp(sentence)
    top_category = get_top_cat(doc)
    print (f"\"{sentence}\" {top_category}\n")

