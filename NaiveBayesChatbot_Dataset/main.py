from nlp.response_selector import ResponseSelector
import os
import train

base_dir = r'D:\Python\ChatBotAI\mid_range_chatbot\NaiveBayesChatbot_Dataset'

if __name__ == "__main__":
    classifier = train.main()  # train và lấy classifier
    responses_path = os.path.join(base_dir, 'data', 'processed', 'intent_responses.json')
    selector = ResponseSelector(responses_path)

    while True:
        user_input = input("Bạn hỏi: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        intent = classifier.predict(user_input)
        response = selector.get_response(intent)
        print(f"👉 Intent dự đoán: {intent}")
        print(f"🤖 Chatbot trả lời: {response}")
