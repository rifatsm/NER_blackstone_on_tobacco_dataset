# Filename: test_blackstone.py

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

text = """
It is a well-established principle of law that the transactions of independent states between each other are governed by other laws than those which municipal courts administer. \
It is, however, in my judgment, insufficient to react to the danger of over-formalisation and “judicialisation” simply by emphasising flexibility and context-sensitivity. \
The question is whether on the facts found by the judge, the (or a) proximate cause of the loss of the rig was “inherent vice or nature of the subject matter insured” within the meaning of clause 4.4 of the Institute Cargo Clauses (A).
"""

# Apply the model to the text
doc = nlp(text)

# Get the sentences in the passage of text
sentences = [sent.text for sent in doc.sents]

# Print the sentence and the corresponding predicted category.
for sentence in sentences:
    doc = nlp(sentence)
    top_category = get_top_cat(doc)
    print (f"\"{sentence}\" {top_category}\n")