from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')


# Example POST Route (Form Submission)
# @app.route('/submit', methods=['POST'])
# def submit():
#     name = request.form.get('name')
    
#     # You can process data here
#     print("Received:", name)

#     return render_template('index.html', message=f"Hello {name}")


# Example API Route (If you use fetch/AJAX)
# @app.route('/api/data', methods=['POST'])
# def api_data():
#     data = request.json
    
#     return jsonify({
#         "status": "success",
#         "received": data
#     })


if __name__ == '__main__':
    app.run(debug=True)