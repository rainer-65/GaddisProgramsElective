# Source: https://codepal.ai/code-generator/query/xmfZtOpn/python-audio-player-pyqt5-module-without-pygame
# small adaptions

import os

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog


class AudioPlayer(QWidget):
    """
    A simple audio player that uses PyQt5 and QMediaPlayer to play audio files.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Audio Player")
        self.setGeometry(100, 100, 500, 300)
        self.media_player = QMediaPlayer()
        self.play_button = QPushButton("Play")
        self.pause_button = QPushButton("Pause")
        self.stop_button = QPushButton("Stop")
        self.add_button = QPushButton("Add File")
        self.play_button.clicked.connect(self.play)
        self.pause_button.clicked.connect(self.pause)
        self.stop_button.clicked.connect(self.stop)
        self.add_button.clicked.connect(self.add_file)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.play_button)
        button_layout.addWidget(self.pause_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.add_button)
        layout = QVBoxLayout()
        layout.addLayout(button_layout)
        self.setLayout(layout)

    def play(self):
        """
        Plays the currently loaded media file.
        """
        self.media_player.play()

    def pause(self):
        """
        Pauses the currently playing media file.
        """
        self.media_player.pause()

    def stop(self):
        """
        Stops the currently playing media file.
        """
        self.media_player.stop()

    def add_file(self):
        """
        Opens a file dialog to select an audio file to load into the player.
        """
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", os.path.expanduser("~"),
                                                   "Audio Files (*.mp3 *.wav)")
        if file_path:
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
            self.media_player.play()


if __name__ == "__main__":
    app = QApplication([])
    player = AudioPlayer()
    player.show()
    app.exec_()
