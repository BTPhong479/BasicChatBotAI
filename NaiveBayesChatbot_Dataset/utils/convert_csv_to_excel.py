import pandas as pd

# Đường dẫn tới file CSV gốc bạn tải về
csv_path = r"C:\Users\UFO\Downloads\Bitext_Sample_Customer_Support_Training_Dataset_27K_responses-v11.csv"

# Đường dẫn nơi bạn muốn lưu file Excel
excel_path = r"D:\Python\ChatBotAI\mid_range_chatbot\NaiveBayesChatbot_Dataset\data\raw\train.xlsx"

# Đọc file CSV
df = pd.read_csv(csv_path)

# Ghi ra file Excel
df.to_excel(excel_path, index=False)

print("✅ Đã chuyển CSV sang Excel thành công!")
