import sys
from PySide2.QtWidgets import QApplication, QLabel


def main():
    print("Hello world")
    app = QApplication(sys.argv)
    # app.aboutQt()
    label = QLabel("Hello World")
    label.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
