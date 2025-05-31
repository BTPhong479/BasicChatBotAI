import math
from collections import defaultdict, Counter
from nlp.preprocessing import tokenize


class NaiveBayesClassifier:
    def __init__(self):
        self.class_word_counts = defaultdict(Counter)
        self.class_counts = Counter()
        self.vocab = set()

    def train(self, data):
        for item in data:
            tokens = tokenize(item["text"])
            intent = item["intent"]

            self.class_counts[intent] += 1
            for token in tokens:
                self.class_word_counts[intent][token] +=1
                self.vocab.add(token)

        self.total_docs = sum(self.class_counts.values())


    def predict(self, text):
        tokens = tokenize(text)
        scores = {}

        valid_tokens = [t for t in tokens if t in self.vocab]
        if not valid_tokens:
            return "unknown"
        

        for intent in self.class_counts:
            log_prob = 0
            total_words = sum(self.class_word_counts[intent].values())
            for token in tokens:
                word_freq = self.class_word_counts[intent][token]

                prob = ( word_freq +1 )/(total_words + len(self.vocab))
                log_prob += math.log(prob)

            log_prob += math.log(self.class_counts[intent] / self.total_docs)
            scores[intent] = log_prob

        return max(scores, key=scores.get)
