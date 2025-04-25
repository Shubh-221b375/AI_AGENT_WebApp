from flask import Flask, request, jsonify, render_template
from ai_api import get_plan

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Serves the web UI

@app.route('/api/plan', methods=['POST'])
def generate_plan():
    data = request.get_json()
    task = data.get('task', '')
    plan = get_plan(task)
    return jsonify({'plan': plan})

if __name__ == '__main__':
    app.run(debug=True)
