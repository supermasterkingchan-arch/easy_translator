import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QTextEdit, QFrame, QLabel, QPushButton)
from PyQt6.QtCore import Qt, QPoint
from googletrans import Translator

class SimpleDictApp(QWidget):
    def __init__(self):
        super().__init__()
        self.translator = Translator()
        self.drag_position = None  # 드래그 위치 저장용 (None으로 초기화)
        self.initUI()
        self.load_stylesheet()

    def initUI(self):
        # 항상 위, 테두리 없음 설정
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setMinimumSize(400, 800)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # 메인 프레임
        self.frame = QFrame()
        self.frame.setObjectName("MainFrame")
        frame_layout = QVBoxLayout(self.frame)
        frame_layout.setContentsMargins(15, 10, 15, 15)
        
        # --- 커스텀 타이틀바 (드래그 가능 영역) ---
        self.header_widget = QWidget()
        header_layout = QHBoxLayout(self.header_widget)
        header_layout.setContentsMargins(5, 5, 5, 5)
        
        self.title_label = QLabel("English-Korean Translator")
        self.title_label.setObjectName("TitleLabel")
        
        self.close_button = QPushButton("×")
        self.close_button.setObjectName("CloseButton")
        self.close_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.close_button.clicked.connect(self.close)
        
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()
        header_layout.addWidget(self.close_button)

        # --- 입력창 및 결과창 ---
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("번역할 단어나 문장을 입력하세요...")
        self.input_box.returnPressed.connect(self.perform_translation)
        
        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        self.result_box.setPlaceholderText("결과가 여기에 표시됩니다.")
        
        frame_layout.addWidget(self.header_widget)
        frame_layout.addWidget(self.input_box)
        frame_layout.addWidget(self.result_box)
        
        layout.addWidget(self.frame)
        self.setLayout(layout)

    def load_stylesheet(self):
        try:
            with open("styles.qss", "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            pass

    def perform_translation(self):
        text = self.input_box.text().strip()
        if not text:
            return
        try:
            detected = self.translator.detect(text).lang
            dest_lang = 'ko' if detected == 'en' else 'en'
            result = self.translator.translate(text, dest=dest_lang)
            self.result_box.setText(result.text)
        except Exception as e:
            self.result_box.setText(f"Error: {e}")

# --- 드래그 이동 로직 (창 상단 header_widget 영역만 드래그 허용) ---
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.header_widget.geometry().contains(event.pos()):
                # 1. 시스템 네이티브 이동 시도 (리눅스/Wayland 등에서 필수)
                # 운영체제가 직접 창 이동을 처리하므로 훨씬 부드럽고 호환성이 좋습니다.
                if self.windowHandle().startSystemMove():
                    event.accept()
                    return

                # 2. 시스템 이동 미지원 시 수동 계산 방식 사용 (백업 로직)
                self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
                event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton and self.drag_position is not None:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.drag_position = None  # 드래그 종료 시 초기화

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimpleDictApp()
    ex.show()
    sys.exit(app.exec())