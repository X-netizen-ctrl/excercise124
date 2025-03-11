from PyQt6.QtWidgets import QApplication
from excercise_124.ui.MainWindow124EXT import MainWindow124EXT

app = QApplication([])
myui = MainWindow124EXT()
myui.show()  # ✅ Correct method
app.exec()
