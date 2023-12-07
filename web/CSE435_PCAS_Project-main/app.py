from flask import Flask, render_template
import main
import Vehicle
import Pedestrian

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    return "Script has been run!"

if __name__ == '__main__':
    main.main_loop()
    app.run()