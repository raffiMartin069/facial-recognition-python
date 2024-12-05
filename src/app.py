from PyQt5 import QtWidgets
from view.capture import Ui_MainWindow

if __name__ == "__main__":
    import sys
    
    # check if app is inside .venv, if not then create a virtual environment and activate it.
    if hasattr(sys, 'real_prefix'):
        print('Inside a virtual environment')
    else:
        print('Outside a virtual environment')
        print('Creating a virtual environment')
        import subprocess
        subprocess.check_call(["python3", "-m", "venv", ".venv"])
        print('Virtual environment created')
        print('Activating virtual environment')
        subprocess.check_call(["/.venv/bin/activate"])
        print('Virtual environment activated')
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())