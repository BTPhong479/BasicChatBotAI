from nlp.response_selector import ResponseSelector
import os
import train # Import module train để gọi train.main()

# Sửa: Đặt base_dir là '.' để trỏ đến thư mục hiện tại của Colab
base_dir = '.'

if __name__ == "__main__":
    classifier = train.main()  # train và lấy classifier
    # data_path cho responses_selector sẽ được xây dựng đúng cách từ base_dir
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