# app.py

from flask import Flask, request, render_template, jsonify
import os

from agents.issue_detector import detect_issues
from agents.tenancy_faq import answer_tenancy_question

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ----------------------------
# Route: Home - Issue Detector (Manual)
# ----------------------------
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files.get('image')
        context = request.form.get('context')

        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            result = detect_issues(filepath, context)
            return render_template('result.html', image=file.filename, output=result)

    return render_template('index.html')

# ----------------------------
# Route: Tenancy FAQ Agent (Manual)
# ----------------------------
@app.route('/faq', methods=['GET', 'POST'])
def faq():
    if request.method == 'POST':
        question = request.form.get('question')
        location = request.form.get('location')

        if question:
            response = answer_tenancy_question(question, location)
            return render_template('faq_result.html', question=question, location=location, answer=response)

    return render_template('faq_form.html')

# ----------------------------
# Route: Unified Chat - Auto-Routing
# ----------------------------
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        file = request.files.get('image')
        text = request.form.get('context')

        if file and file.filename != '':
            # Use Agent 1: Issue Detector
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            result = detect_issues(filepath, text)
            return render_template('result.html', image=file.filename, output=result)
        
        elif text:
            # Use Agent 2: Tenancy FAQ
            result = answer_tenancy_question(text)
            return render_template('faq_result.html', question=text, location=None, answer=result)

        else:
            return "Please enter a question or upload an image."

    return render_template('chat_unified.html')

@app.route('/api/chat', methods=['POST'])
def api_chat():
    file = request.files.get('image')
    text = (
        request.form.get('context')
        or request.values.get('context')
        or (request.json.get('context') if request.is_json and request.json else None)
    )
    response_data = {}

    if file and file.filename != '':
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        result = detect_issues(filepath, text)
        response_data = {
            'type': 'image',
            'image': file.filename,
            'output': result
        }
    elif text and text.strip():
        result = answer_tenancy_question(text)
        response_data = {
            'type': 'text',
            'question': text,
            'output': result
        }
    else:
        response_data = {
            'error': 'Please enter a question or upload an image.'
        }
    return jsonify(response_data)

# ----------------------------
# Run Flask App
# ----------------------------
if __name__ == '__main__':
    app.run(debug=True)
