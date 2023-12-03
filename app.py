import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from flask import Flask, render_template
from flask import send_file

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('home.html', title='Home')


@app.route('/home.html')
def home():
    return render_template('home.html', title='Home')

@app.route('/image/')
def image():
    return send_file('images/slider-img.png', mimetype='image/png')

@app.route('/manager.html')
def manager():
    return render_template('manager.html', title='Manager')

@app.route('/payment.html')
def payment():
    return render_template('payment.html', title='Payment')

@app.route('/statistics.html')
def statistics():
    return render_template('statistics.html', title='Statistics')

@app.route('/settings.html')
def settings():
    return render_template('settings.html', title='Settings')



    
def run_flask_app():
    if __name__ == '__main__':
        app.run()


class WebAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finance Tracker")
        self.setWindowIcon(QIcon('favicon.ico'))  
        self.setFixedSize(560, 910) 
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)

        # виджет
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        # в отдельном потоке
        import threading
        flask_thread = threading.Thread(target=run_flask_app)
        flask_thread.start()

        self.web_view.setUrl(QUrl('http://127.0.0.1:5000')) 

def create_window():
    app = QApplication(sys.argv)
    window = WebAppWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    create_window()