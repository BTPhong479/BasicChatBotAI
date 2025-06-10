import json
import random

class ResponseSelector:
    def __init__(self, responses_path):
        with open(responses_path, 'r', encoding='utf-8') as f:
            self.intent_responses = json.load(f)

    def get_response(self, intent):
        responses = self.intent_responses.get(intent, [])
        if responses:
            return random.choice(responses)
        else:
            return "Xin lỗi, tôi không hiểu câu hỏi của bạn."

# Test
if __name__ == "__main__":
    # Sửa đường dẫn ở đây để chạy test trực tiếp từ folder nlp
    # ".." nghĩa là lùi ra một cấp thư mục (để đến NaiveBayesChatbot_Dataset)
    selector = ResponseSelector('../data/processed/intent_responses.json')
    print(selector.get_response('cancel_order'))