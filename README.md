# Real Estate Assistant Chatbot

A modern, AI-powered web application for property issue detection and tenancy law Q&A. Users can upload property images for analysis or ask tenancy-related questions via a real-time, full-screen chat interface.

## Features
- **Real-time Chat UI**: Modern, dark-themed, full-screen chat interface.
- **Image Issue Detection**: Upload property images to detect issues (e.g., mold, water damage) using Google Gemini AI.
- **Tenancy FAQ Agent**: Ask questions about tenancy law, landlord/tenant rights, and rental procedures.
- **Automatic Agent Routing**: The chatbot intelligently routes your input to the correct agent based on whether you upload an image or type a question.

## Demo
![screenshot](static/uploads/demo_screenshot.png) <!-- Add a screenshot if available -->

## Getting Started

### 1. Clone the Repository
```sh
git clone <repo-url>
cd realestate_bot
```

### 2. Create and Activate a Virtual Environment
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root with your Google Gemini API key:
```
GEMINI_API_KEY=your_actual_gemini_api_key
```

### 5. Run the Application
```sh
python app.py
```
Visit [http://127.0.0.1:5000/chat](http://127.0.0.1:5000/chat) in your browser.

## Project Structure
```
realestate_bot/
├── agents/
│   ├── issue_detector.py
│   └── tenancy_faq.py
├── app.py
├── static/
│   └── uploads/
├── templates/
│   ├── chat_unified.html
│   ├── faq_form.html
│   ├── faq_result.html
│   ├── index.html
│   └── result.html
├── utils/
│   └── router.py
├── venv/
└── README.md
```

## Usage
- **Ask a tenancy question**: Type your question and press Send.
- **Upload a property image**: Click the file input, select an image, and (optionally) add context, then press Send.
- The chatbot will respond in real time, displaying answers or analysis in the chat window.

## Requirements
- Python 3.7+
- Flask
- google-generativeai
- python-dotenv
- Pillow

(See `requirements.txt` for full list)

## Customization
- To further style or extend the chat interface, edit `templates/chat_unified.html`.
- To add more agents or routing logic, see `app.py` and the `agents/` directory.

## License
MIT License 