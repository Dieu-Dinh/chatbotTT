    import sys
    import google.generativeai as genai
    from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel, QHBoxLayout
    from PyQt5.QtCore import Qt

    # API Key Gemini
    API_KEY = "AIzaSyBWRSbJWIerS727egGbSbSGOhgzsdQKLSc"
    genai.configure(api_key=API_KEY)

    # Tạo model Gemini
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Lưu lịch sử hội thoại
    history = []

    def chat_with_gemini(user_input):
        try:
            history.append({"role": "user", "parts": [user_input]})
            response = model.generate_content(history)
            reply = response.text.strip()
            history.append({"role": "model", "parts": [reply]})
            return reply
        except Exception as e:
            return f"❌ Error: {e}"


    class ChatbotUI(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Gemini Chatbot")
            self.setGeometry(200, 200, 600, 500)

            # Layout chính
            layout = QVBoxLayout()

            # Cửa sổ chat
            self.chat_area = QTextEdit()
            self.chat_area.setReadOnly(True)
            self.chat_area.setStyleSheet("font-size: 14px;")
            layout.addWidget(self.chat_area)

            # Thanh nhập liệu + nút send
            input_layout = QHBoxLayout()
            self.input_field = QLineEdit()
            self.input_field.setPlaceholderText("Nhập tin nhắn...")
            self.input_field.setStyleSheet("font-size: 14px; padding: 5px;")
            input_layout.addWidget(self.input_field)

            self.send_button = QPushButton("Send")
            self.send_button.setStyleSheet("font-size: 14px; padding: 5px;")
            self.send_button.clicked.connect(self.send_message)
            input_layout.addWidget(self.send_button)

            layout.addLayout(input_layout)
            self.setLayout(layout)

            # Nhấn Enter để gửi
            self.input_field.returnPressed.connect(self.send_message)

        def send_message(self):
            user_input = self.input_field.text().strip()
            if not user_input:
                return

            # Hiện tin nhắn user
            self.chat_area.append(f"<b style='color:blue'>You:</b> {user_input}")

            # Gọi chatbot
            response = chat_with_gemini(user_input)

            # Hiện tin nhắn bot
            self.chat_area.append(f"<b style='color:green'>Bot:</b> {response}\n")

            # Xóa ô nhập
            self.input_field.clear()
            self.chat_area.verticalScrollBar().setValue(self.chat_area.verticalScrollBar().maximum())


    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = ChatbotUI()
        window.show()
        sys.exit(app.exec_())
