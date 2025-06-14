from nlp.response_selector import ResponseSelector
import os
import train  # Chứa hàm train.main()

base_dir = '.'

if __name__ == "__main__":
    # Train model và hiển thị biểu đồ trong train.main()
    classifier = train.main()

    responses_path = os.path.join(base_dir, 'data', 'processed', 'intent_responses.json')
    selector = ResponseSelector(responses_path)

    print("\n--- BẮT ĐẦU CHATBOT TƯƠNG TÁC ---")
    while True:
        user_input = input("Bạn hỏi: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        intent = classifier.predict(user_input)
        response = selector.get_response(intent)
        print(f"👉 Intent dự đoán: {intent}")
        print(f"🤖 Chatbot trả lời: {response}")
