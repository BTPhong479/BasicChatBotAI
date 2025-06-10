import json
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords

class NaiveBayesClassifier:
    def __init__(self):
        self.vectorizer = None
        self.clf = None
        try:
            self.stop_words = set(stopwords.words('english'))
        except LookupError:
            print("Stopwords not found, downloading...")
            nltk.download('stopwords')
            self.stop_words = set(stopwords.words('english'))

    def preprocess(self, text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)  # loại bỏ dấu câu
        tokens = text.split()
        filtered = [word for word in tokens if word not in self.stop_words]
        return ' '.join(filtered)

    def load_texts(self, json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            texts = json.load(f)
        return texts

    def train(self, texts):
        X = [self.preprocess(item['text']) for item in texts]
        y = [item['intent'] for item in texts]

        self.vectorizer = CountVectorizer()
        X_vec = self.vectorizer.fit_transform(X)

        self.clf = MultinomialNB()
        self.clf.fit(X_vec, y)

    def predict(self, text):
        cleaned = self.preprocess(text)
        X = self.vectorizer.transform([cleaned])
        pred = self.clf.predict(X)
        return pred[0]
