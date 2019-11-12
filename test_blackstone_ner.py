import spacy

# Load the model
nlp = spacy.load("en_blackstone_proto")

text = "The witness, senior vice-president and controller at R. J. Reynolds Tobacco Holding Inc., was deposed by the plaintiffs. He described the financial status of the holding company and its economic activities. He indicated that industry changes, corporate changes, market changes, structural changes, and some legal developments have all had an adverse effect on the profitability of the company. The witness also noted that advertising and promotion restrictions placed on them in 1998 by the Master Settlement Agreement had caused a drop in sales volume. He said that punitive damage awards would have a devastating effect on the company, although he declined to say whether bankruptcy was being considered."

# Apply model to text
doc = nlp(text)

# Iterate through the entities identified by the model
for ent in doc.ents:
	print("entity: ",ent.text, " label: ", ent.label_)