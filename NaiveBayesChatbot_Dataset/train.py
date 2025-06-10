import os
from nlp.classifier import NaiveBayesClassifier

def main():
    base_dir = r'D:\Python\ChatBotAI\mid_range_chatbot\NaiveBayesChatbot_Dataset'
    data_path = os.path.join(base_dir, 'data', 'processed', 'texts.json')

    classifier = NaiveBayesClassifier()
    texts = classifier.load_texts(data_path)
    classifier.train(texts)

    print(f"✅ Đã train xong model với {len(texts)} mẫu dữ liệu.")
    return classifier

if __name__ == '__main__':
    main()