from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/getZodiacInfo', methods=['POST'])
def get_zodiac_info():
    data = request.json
    year = data.get('year')
    
    # Assuming you have a script named `calculate_zodiac.py` that accepts a year
    result = subprocess.run(['python', 'calculate_zodiac.py', str(year)], capture_output=True, text=True)
    
    return jsonify({"output": result.stdout})

if __name__ == '__main__':
    app.run(debug=True)