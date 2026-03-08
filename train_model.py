# Training the model with TF-IDF and Logistic Regression
# TF-IDF: Term Frequency - Inverse Document Frequency

# to save the trained model to a file so it can be loaded later without retraining
import pickle 

# for preporocessing
import spacy

# TfidfVectorizer converts text to numerical vectors using TF_IDF
# ML models cannot work directly with text, so sentences must be converted to numbers first
from sklearn.feature_extraction.text import TfidfVectorizer

# LogisticRegression is an ML classification algorithm
# It predicts which class (intent) a piece of text belongs to
from sklearn.linear_model import LogisticRegression

# import the training data with the example sentences and labels
from training_data import training_sentences

# load the English NLP model
nlp = spacy.load("en_core_web_sm")

# function to preprocess the user input
def preprocess(text):
    doc = nlp(text.lower()) # to lower case

    # extract lemmatized tokens for better matchings
    # lemmatization (turning “contacted”, “contacting” → “contact”)
    lemmas = [token.lemma_ for token in doc]

    return " ".join(lemmas)

# STEP 1: Separate text and labels

# extract the user sentences from the training data
# x[0] is the first element in each tuple (the sentence)
texts = [preprocess(x[0]) for x in training_sentences]

# extract the intent labels from the training data
# x[1] is the second element in each tuple (the intent)
labels = [x[1] for x in training_sentences]

# STEP 2: Convert text to numbers

# create a TF_IDF vectorizer object
# this will convert sentences into numerical feature vectors
vectorizer = TfidfVectorizer(lowercase=True, ngram_range=(1,2))

# use fit_transform to
# 1. learn the vocab from the training sentences
# 2. convert the sentences into numerical vectors
X = vectorizer.fit_transform(texts)

# STEP 3: Train the classifier

# create the Logistic Regression model
model = LogisticRegression()

# train the model using the numerical features (X) and their corresponding labels (intents)
model.fit(X, labels)

# STEP 5: Save the trained model

# save the classifier to a file so it can be reused later
# "wb" means write in binary mode
pickle.dump(model, open("intent_model.pkl", "wb"))

# save the TF-IDF vectorizer as well
# this is important because new user messages must be transformed with the same vocab learned during training
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

# STEP 5: Confirmation message
print("Model trained and saved.")