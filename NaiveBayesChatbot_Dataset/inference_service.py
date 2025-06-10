import pickle
import os
import re
import nltk
from nltk.corpus import stopwords
from nlp.response_selector import ResponseSelector # Import để lấy câu trả lời

# Hàm tiền xử lý (preprocess) giống như trong NaiveBayesClassifier
# Cần phải có hàm này để tiền xử lý input trước khi dự đoán
def preprocess_text(text, stop_words):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = text.split()
    filtered = [word for word in tokens if word not in stop_words]
    return ' '.join(filtered)

class ChatbotInference:
    def __init__(self, models_dir='models'):
        self.classifier_model = None
        self.vectorizer_model = None
        self.stop_words = None
        self.response_selector = None # Thêm biến để lưu ResponseSelector

        try:
            self.stop_words = set(stopwords.words('english'))
        except LookupError:
            print("Stopwords not found, downloading...")
            nltk.download('stopwords')
            self.stop_words = set(stopwords.words('english'))

        # Đường dẫn tới các file model và data
        base_dir = '.' # Đảm bảo base_dir là thư mục hiện tại của chatbot
        classifier_filename = os.path.join(base_dir, models_dir, 'naive_bayes_classifier.pkl')
        vectorizer_filename = os.path.join(base_dir, models_dir, 'count_vectorizer.pkl')
        responses_path = os.path.join(base_dir, 'data', 'processed', 'intent_responses.json') # Đường dẫn tới file responses

        # Tải classifier (model Naive Bayes)
        with open(classifier_filename, 'rb') as f:
            self.classifier_model = pickle.load(f)
        print(f"✅ Đã tải classifier từ: {classifier_filename}")

        # Tải vectorizer (để chuyển đổi văn bản sang dạng số)
        with open(vectorizer_filename, 'rb') as f:
            self.vectorizer_model = pickle.load(f)
        print(f"✅ Đã tải vectorizer từ: {vectorizer_filename}")

        # Tải bộ chọn phản hồi
        self.response_selector = ResponseSelector(responses_path)
        print(f"✅ Đã tải bộ chọn phản hồi từ: {responses_path}")

    # Phương thức để dự đoán intent (chỉ trả về intent)
    def predict_intent(self, text):
        cleaned_text = preprocess_text(text, self.stop_words)
        X_vec = self.vectorizer_model.transform([cleaned_text])
        intent = self.classifier_model.predict(X_vec)[0]
        return intent

    # Phương thức mới để lấy cả intent và response
    def get_chatbot_response(self, user_input):
        intent = self.predict_intent(user_input) # Dự đoán intent
        response = self.response_selector.get_response(intent) # Lấy phản hồi
        return intent, response # Trả về cả hai

# --- PHẦN KIỂM TRA TRỰC TIẾP TRONG COLAB ---
if __name__ == "__main__":
    print("Đang khởi tạo dịch vụ dự đoán chatbot...")
    inference_service = ChatbotInference()

    print("\nBạn có thể bắt đầu hỏi chatbot (nhập 'exit' hoặc 'quit' để thoát):")
    while True:
        user_input = input("Bạn: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        predicted_intent, chatbot_response = inference_service.get_chatbot_response(user_input)
        print(f"👉 Intent dự đoán: {predicted_intent}")
        print(f"🤖 Chatbot trả lời: {chatbot_response}")