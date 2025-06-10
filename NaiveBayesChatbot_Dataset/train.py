import os
import pickle # Thêm thư viện pickle để lưu/tải model
from nlp.classifier import NaiveBayesClassifier

def main():
    # Sửa: Đặt base_dir là '.' để trỏ đến thư mục hiện tại của Colab
    base_dir = '.'

    # data_path sẽ tự động được xây dựng đúng cách từ base_dir
    data_path = os.path.join(base_dir, 'data', 'processed', 'texts.json')

    # Khởi tạo và train classifier
    classifier_obj = NaiveBayesClassifier() # Đổi tên biến để rõ ràng hơn
    texts = classifier_obj.load_texts(data_path)
    classifier_obj.train(texts)

    print(f"✅ Đã train xong model với {len(texts)} mẫu dữ liệu.")

    # --- PHẦN LƯU MODEL MỚI THÊM VÀO ---
    # Tạo thư mục 'models' nếu chưa tồn tại
    models_dir = os.path.join(base_dir, 'models')
    os.makedirs(models_dir, exist_ok=True) # exist_ok=True giúp tránh lỗi nếu thư mục đã có

    # Lưu classifier (model Naive Bayes)
    classifier_filename = os.path.join(models_dir, 'naive_bayes_classifier.pkl')
    with open(classifier_filename, 'wb') as f:
        pickle.dump(classifier_obj.clf, f) # Lưu đối tượng Naive Bayes đã train
    print(f"✅ Đã lưu classifier vào: {classifier_filename}")

    # Lưu vectorizer (để tiền xử lý văn bản cho dự đoán)
    vectorizer_filename = os.path.join(models_dir, 'count_vectorizer.pkl')
    with open(vectorizer_filename, 'wb') as f:
        pickle.dump(classifier_obj.vectorizer, f) # Lưu đối tượng CountVectorizer đã fit
    print(f"✅ Đã lưu vectorizer vào: {vectorizer_filename}")
    # --- KẾT THÚC PHẦN LƯU MODEL ---

    # Trả về toàn bộ đối tượng NaiveBayesClassifier đã train
    return classifier_obj

if __name__ == '__main__':
    main()