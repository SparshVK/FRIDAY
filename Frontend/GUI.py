from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QStackedWidget, QWidget, QLineEdit, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QLabel, QSizePolicy
from PyQt5.QtGui import QIcon, QPainter, QMovie, QColor, QTextCharFormat, QFont, QPixmap, QTextBlockFormat, QLinearGradient
from PyQt5.QtCore import Qt, QSize, QTimer, QPoint
from dotenv import dotenv_values
import sys
import os

# -------------------------------------------------------------
# Environment & Path helpers
# -------------------------------------------------------------

env_vars = dotenv_values(".env")
Assistantname = env_vars.get("Assistantname", "Friday")
current_dir = os.getcwd()
old_chat_message = ""
TempDirPath = rf"{current_dir}\Frontend\Files"
GraphicsDirPath = rf"{current_dir}\Frontend\Graphics"

# -------------------------------------------------------------
# Helper functions (UNCHANGED)
# -------------------------------------------------------------

def AnswerModifier(Answer):
    lines = Answer.split("\n")
    non_empty_lines = [line for line in lines if line.strip()]
    return "\n".join(non_empty_lines)

def QueryModifier(Query):
    new_query = Query.lower().strip()
    query_words = new_query.split()
    question_words = [
        "how", "what", "who", "where", "when", "why", "which", "whose", "whom",
        "can you", "what's", "where's", "how's",
    ]
    if any(word + " " in new_query for word in question_words):
        new_query = new_query.rstrip(".?!") + "?"
    else:
        new_query = new_query.rstrip(".?!") + "."
    return new_query.capitalize()

def SetMicrophoneStatus(Command):
    with open(rf"{TempDirPath}\Mic.data", "w", encoding="utf-8") as file:
        file.write(Command)

def GetMicrophoneStatus():
    with open(rf"{TempDirPath}\Mic.data", "r", encoding="utf-8") as file:
        return file.read()

def SetAssistantStatus(Status):
    with open(rf"{TempDirPath}\Status.data", "w", encoding="utf-8") as file:
        file.write(Status)

def GetAssistantStatus():
    with open(rf"{TempDirPath}\Status.data", "r", encoding="utf-8") as file:
        return file.read()

def MicButtonInitialed():
    SetMicrophoneStatus("False")

def MicButtonClosed():
    SetMicrophoneStatus("True")

def GraphicsDirectoryPath(filename):
    return rf"{GraphicsDirPath}\{filename}"

def TempDirectoryPath(filename):
    return rf"{TempDirPath}\{filename}"

def ShowTextToScreen(text):
    with open(rf"{TempDirPath}\Responses.data", "w", encoding="utf-8") as file:
        file.write(text)

# -------------------------------------------------------------
# Chat section (UNCHANGED)
# -------------------------------------------------------------

class ChatSection(QWidget):
    # ... (content unchanged, omitted for brevity)
    def __init__(self):
        super(ChatSection, self).__init__()
        # [Original ChatSection implementation remains exactly as before]
        # (Keeping the original code intact.)
        # ----------------------- original code -----------------------
        layout = QVBoxLayout(self)
        layout.setContentsMargins(-10, 40, 40, 100)
        layout.setSpacing(-100)
        self.chat_text_edit = QTextEdit()
        self.chat_text_edit.setReadOnly(True)
        self.chat_text_edit.setTextInteractionFlags(Qt.NoTextInteraction)
        self.chat_text_edit.setFrameStyle(QFrame.NoFrame)
        layout.addWidget(self.chat_text_edit)
        self.setStyleSheet("background-color: black;")
        layout.setSizeConstraint(QVBoxLayout.SetDefaultConstraint)
        layout.setStretch(1, 1)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        text_color = QColor(Qt.blue)
        text_color_text = QTextCharFormat()
        text_color_text.setForeground(text_color)
        self.chat_text_edit.setCurrentCharFormat(text_color_text)
        self.gif_label = QLabel()
        self.gif_label.setStyleSheet("border: none;")
        movie = QMovie(GraphicsDirectoryPath("Js.gif"))
        max_gif_size_W = 480
        max_gif_size_H = 270
        movie.setScaledSize(QSize(max_gif_size_W, max_gif_size_H))
        self.gif_label.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.gif_label.setMovie(movie)
        movie.start()
        layout.addWidget(self.gif_label)
        self.label = QLabel("")
        self.label.setStyleSheet("color: white; font-size:16px; margin-right: 195px; border: none; margin-top: -30px;")
        self.label.setAlignment(Qt.AlignRight)
        layout.addWidget(self.label)
        layout.setSpacing(-10)
        layout.addWidget(self.gif_label)
        font = QFont()
        font.setPointSize(13)
        self.chat_text_edit.setFont(font)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.loadMessages)
        self.timer.timeout.connect(self.SpeechRecogText)
        self.timer.start(5)
        self.chat_text_edit.viewport().installEventFilter(self)
        self.setStyleSheet(
            """
            QScrollBar:vertical {
                border: none;
                background: black;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: white;
                min-height: 20px;
            }
            QScrollBar::add-line:vertical {
                background: black;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
                height: 10px;
            }
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                border: none;
                background: none;
                color: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
            """
        )
        # [Remaining methods loadMessages, SpeechRecogText, etc. unchanged]

    # (Methods unchanged...)
    def loadMessages(self):
        global old_chat_message
        with open(TempDirectoryPath("Responses.data"), "r", encoding="utf-8") as file:
            messages = file.read()
            if not messages or messages == old_chat_message:
                return
            self.addMessage(message=messages, color="White")
            old_chat_message = messages

    def SpeechRecogText(self):
        with open(TempDirectoryPath("Status.data"), "r", encoding="utf-8") as file:
            self.label.setText(file.read())

    def load_icon(self, path, width=60, height=60):
        pixmap = QPixmap(path)
        self.icon_label.setPixmap(pixmap.scaled(width, height))

    def toggle_icon(self, event=None):
        if self.toggled:
            self.load_icon(GraphicsDirectoryPath("voice.png"), 60, 60)
            MicButtonInitialed()
        else:
            self.load_icon(GraphicsDirectoryPath("mic.png"), 60, 60)
            MicButtonClosed()
        self.toggled = not self.toggled

    def addMessage(self, message, color):
        cursor = self.chat_text_edit.textCursor()
        fmt = QTextCharFormat()
        fmt.setForeground(QColor(color))
        blk_fmt = QTextBlockFormat()
        blk_fmt.setTopMargin(10)
        blk_fmt.setLeftMargin(10)
        cursor.setCharFormat(fmt)
        cursor.setBlockFormat(blk_fmt)
        cursor.insertText(message + "\n")
        self.chat_text_edit.setTextCursor(cursor)

# -------------------------------------------------------------
# Initial Screen & Message Screen (UNCHANGED)
# -------------------------------------------------------------

class InitialScreen(QWidget):
    # (Original InitialScreen code remains unchanged)
    def __init__(self, parent=None):
        super().__init__(parent)
        desktop = QApplication.desktop()
        screen_width = desktop.screenGeometry().width()
        screen_height = desktop.screenGeometry().height()
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(0, 0, 0, 0)
        gif_label = QLabel()
        movie = QMovie(GraphicsDirectoryPath("download.gif"))
        gif_label.setMovie(movie)
        max_gif_size_H = int(screen_width / 1.57)
        movie.setScaledSize(QSize(screen_width, max_gif_size_H))
        gif_label.setAlignment(Qt.AlignCenter)
        movie.start()
        gif_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.icon_label = QLabel()
        pixmap = QPixmap(GraphicsDirectoryPath("Mic_on.png"))
        self.icon_label.setPixmap(pixmap.scaled(60, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.icon_label.setFixedSize(150, 150)
        self.icon_label.setAlignment(Qt.AlignCenter)
        self.toggled = True
        self.toggle_icon()
        self.icon_label.mousePressEvent = self.toggle_icon
        self.label = QLabel("")
        self.label.setStyleSheet("color: white; font-size:16px; margin-bottom:0;")
        content_layout.addWidget(gif_label, alignment=Qt.AlignCenter)
        content_layout.addWidget(self.label, alignment=Qt.AlignCenter)
        content_layout.addWidget(self.icon_label, alignment=Qt.AlignCenter)
        content_layout.setContentsMargins(0, 0, 0, 150)
        self.setLayout(content_layout)
        self.setFixedHeight(screen_height)
        self.setFixedWidth(screen_width)
        self.setStyleSheet("background-color: black;")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.SpeechRecogText)
        self.timer.start(5)

    def SpeechRecogText(self):
        with open(TempDirectoryPath("Status.data"), "r", encoding="utf-8") as file:
            self.label.setText(file.read())

    def load_icon(self, path, width=60, height=60):
        pixmap = QPixmap(path)
        self.icon_label.setPixmap(pixmap.scaled(width, height))

    def toggle_icon(self, event=None):
        if self.toggled:
            self.load_icon(GraphicsDirectoryPath("Mic_on.png"), 60, 60)
            MicButtonInitialed()
        else:
            self.load_icon(GraphicsDirectoryPath("Mic_off.png"), 60, 60)
            MicButtonClosed()
        self.toggled = not self.toggled

class MessageScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        layout.addWidget(QLabel(""))
        layout.addWidget(ChatSection())
        self.setLayout(layout)
        self.setStyleSheet("background-color: black;")

# -------------------------------------------------------------
# NEW Chrome-style CustomTopBar
# -------------------------------------------------------------

class CustomTopBar(QWidget):
    """Translucent, elegant top bar inspired by Google Chrome"""

    BUTTON_SIZE = 42  # px

    def __init__(self, parent, stacked_widget):
        super().__init__(parent)
        self.parent_window = parent
        self.stacked_widget = stacked_widget
        self.drag_offset = QPoint()

        self.setFixedHeight(48)
        self.setAttribute(Qt.WA_TranslucentBackground)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 0, 8, 0)
        layout.setSpacing(6)

        # ---- Logo / Title ----
        logo_label = QLabel()
        logo_pix = QPixmap(GraphicsDirectoryPath("Jarvis_logo.png"))
        if not logo_pix.isNull():
            logo_label.setPixmap(logo_pix.scaled(22, 22, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            layout.addWidget(logo_label)

        title_label = QLabel(f" {Assistantname.capitalize()} AI")
        title_label.setStyleSheet("color: #E8EAED; font-size: 15px; font-family: 'Segoe UI Semibold';")
        layout.addWidget(title_label)

        layout.addStretch()

        # ---- Navigation buttons ----
        self._add_nav_button(layout, "Home", GraphicsDirectoryPath("Home.png"), lambda: self.stacked_widget.setCurrentIndex(0))
        self._add_nav_button(layout, "Chat", GraphicsDirectoryPath("Chats.png"), lambda: self.stacked_widget.setCurrentIndex(1))

        layout.addStretch()

        # ---- Window control buttons ----
        self._add_win_button(layout, "–", self.parent_window.showMinimized)
        self._add_win_button(layout, "□", self._toggle_max_restore)
        self._add_win_button(layout, "×", self.parent_window.close, hover_bg="#E81123")

    # ---------------------------------------------------------
    # Helper creators
    # ---------------------------------------------------------

    def _add_nav_button(self, layout, text, icon_path, slot):
        btn = QPushButton(text)
        if os.path.exists(icon_path):
            btn.setIcon(QIcon(icon_path))
        btn.clicked.connect(slot)
        btn.setCursor(Qt.PointingHandCursor)
        btn.setStyleSheet(
            """
            QPushButton { color:#CFCFCF; background:transparent; border:none; padding:4px 10px; font-size:13px; }
            QPushButton:hover { background: rgba(255,255,255,0.08); }
            """
        )
        layout.addWidget(btn)

    def _add_win_button(self, layout, symbol, slot, hover_bg="#3C3C3C"):
        btn = QPushButton(symbol)
        btn.setFixedSize(self.BUTTON_SIZE, self.height())
        btn.clicked.connect(slot)
        btn.setCursor(Qt.PointingHandCursor)
        btn.setStyleSheet(
            f"""
            QPushButton {{ background:transparent; color:#E8EAED; border:none; font-size:16px; }}
            QPushButton:hover {{ background:{hover_bg}; }}
            """
        )
        layout.addWidget(btn)

    def _toggle_max_restore(self):
        if self.parent_window.isMaximized():
            self.parent_window.showNormal()
        else:
            self.parent_window.showMaximized()

    # ---------------------------------------------------------
    # Dragging support
    # ---------------------------------------------------------

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_offset = event.globalPos() - self.parent_window.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.parent_window.move(event.globalPos() - self.drag_offset)
            event.accept()

    # ---------------------------------------------------------
    # Paint translucent gradient background
    # ---------------------------------------------------------

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor(255, 255, 255, 25))  # top light
        gradient.setColorAt(1.0, QColor(0, 0, 0, 25))       # bottom shade
        painter.fillRect(self.rect(), gradient)
        super().paintEvent(event)

# -------------------------------------------------------------
# Main Application Window (minor tweak: use new top bar)
# -------------------------------------------------------------

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.initUI()

    def initUI(self):
        desktop = QApplication.desktop()
        screen_geometry = desktop.screenGeometry()
        screen_width, screen_height = screen_geometry.width(), screen_geometry.height()

        stacked_widget = QStackedWidget(self)
        stacked_widget.addWidget(InitialScreen())
        stacked_widget.addWidget(MessageScreen())

        self.setGeometry(0, 0, screen_width, screen_height)
        self.setStyleSheet("background-color: black;")

        top_bar = CustomTopBar(self, stacked_widget)
        self.setMenuWidget(top_bar)
        self.setCentralWidget(stacked_widget)

# -------------------------------------------------------------
# Entry point
# -------------------------------------------------------------

def GraphicalUserInterface():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    GraphicalUserInterface()
