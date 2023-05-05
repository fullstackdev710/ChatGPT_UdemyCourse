import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton,QTextEdit
import openai
import docx

class EssayGenerator(QWidget):
   def __init__(self):
      super().__init__()
      self.initUI()

   def initUI(self):
      self.setWindowTitle("Article Generator")
      self.setGeometry(300,300,2500,1500)

      topic_label=QLabel('Enter the topic:',self)
      topic_label.move(20,40)

      self.topic_input=QLineEdit(self)
      self.topic_input.move(20,100)
      self.topic_input.resize(1200,50)

      self.essay_output=QTextEdit(self)
      self.essay_output.move(20,200)
      self.essay_output.resize(2100,1200)

      generate_button=QPushButton("Generate Essay", self)
      generate_button.move(1250,100)
      generate_button.clicked.connect(self.generate_essay)

   def generate_essay(self):
      pass


if __name__ == "__main__":
   app=QApplication(sys.argv)
   ex=EssayGenerator()
   ex.show()
   sys.exit(app.exec_())