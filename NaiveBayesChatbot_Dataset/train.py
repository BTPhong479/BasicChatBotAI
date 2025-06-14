import os
import pickle
from nlp.classifier import NaiveBayesClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    base_dir = '.'
    data_path = os.path.join(base_dir, 'data', 'processed', 'texts.json')

    classifier_obj = NaiveBayesClassifier()
    texts = classifier_obj.load_texts(data_path)

    # --- CHIA TÁCH DỮ LIỆU ---
    X_data = [classifier_obj.preprocess(item['text']) for item in texts]
    y_data = [item['intent'] for item in texts]

    X_train, X_test, y_train, y_test = train_test_split(
        X_data, y_data, test_size=0.2, random_state=42, stratify=y_data
    )

    print(f"Tổng số mẫu: {len(X_data)}")
    print(f"Số mẫu huấn luyện: {len(X_train)}")
    print(f"Số mẫu kiểm tra: {len(X_test)}")

    # --- HUẤN LUYỆN ---
    classifier_obj.vectorizer = CountVectorizer()
    X_train_vec = classifier_obj.vectorizer.fit_transform(X_train)

    classifier_obj.clf = MultinomialNB()
    classifier_obj.clf.fit(X_train_vec, y_train)

    print(f"✅ Đã train xong model trên {len(X_train)} mẫu.")

    # --- ĐÁNH GIÁ ---
    X_test_vec = classifier_obj.vectorizer.transform(X_test)
    y_pred = classifier_obj.clf.predict(X_test_vec)

    print("\n--- ĐÁNH GIÁ HIỆU SUẤT ---")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print("\nBáo cáo phân loại:")
    print(classification_report(y_test, y_pred, zero_division=0))

    # --- CONFUSION MATRIX ---
    print("\n--- Biểu đồ Confusion Matrix ---")
    cm = confusion_matrix(y_test, y_pred)
    labels = classifier_obj.clf.classes_

    plt.figure(figsize=(len(labels) * 0.8 + 2, len(labels) * 0.7 + 2))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=labels, yticklabels=labels)
    plt.xlabel('Dự đoán (Predicted Intent)')
    plt.ylabel('Thực tế (True Intent)')
    plt.title('Confusion Matrix')
    plt.tight_layout()
    plt.show()  # ✅ QUAN TRỌNG để hiển thị trong Colab

    # --- LƯU MODEL ---
    models_dir = os.path.join(base_dir, 'models')
    os.makedirs(models_dir, exist_ok=True)

    with open(os.path.join(models_dir, 'naive_bayes_classifier.pkl'), 'wb') as f:
        pickle.dump(classifier_obj.clf, f)
    with open(os.path.join(models_dir, 'count_vectorizer.pkl'), 'wb') as f:
        pickle.dump(classifier_obj.vectorizer, f)
    print("✅ Đã lưu model và vectorizer.")

    return classifier_obj  # Không trả fig nữa


if __name__ == '__main__':
    main()
