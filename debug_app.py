#!/usr/bin/env python3

print("=== Debug App Creation ===")

try:
    print("1. Importing Flask...")
    from flask import Flask, request, render_template
    print("   ✓ Flask imported")
    
    print("2. Importing issue detector...")
    from agents.issue_detector import detect_issues
    print("   ✓ Issue detector imported")
    
    print("3. Importing os...")
    import os
    print("   ✓ OS imported")
    
    print("4. Creating Flask app...")
    app = Flask(__name__)
    print("   ✓ Flask app created")
    
    print("5. Setting up upload folder...")
    UPLOAD_FOLDER = 'static/uploads'
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    print("   ✓ Upload folder created")
    
    print("6. Defining route...")
    @app.route('/', methods=['GET', 'POST'])
    def home():
        if request.method == 'POST':
            file = request.files['image']
            text = request.form.get('context')
            if file:
                path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(path)
                result = detect_issues(path, text)
                return render_template('result.html', image=file.filename, output=result)
        return render_template('index.html')
    
    print("   ✓ Route defined")
    
    print("7. Testing app.run()...")
    if __name__ == '__main__':
        print("   ✓ In main block")
        app.run(debug=True)
    else:
        print("   ✗ Not in main block")
        
except Exception as e:
    print(f"   ✗ Error: {e}")
    import traceback
    traceback.print_exc() 