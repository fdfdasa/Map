import flask
import flask_cors
from flask import request, jsonify
from test_data import find_best_match

app = flask.Flask(__name__)
flask_cors.CORS(app)

@app.route('/direction', methods=['POST'])
def home():
    data = request.json
    text = data.get('text', '')

    best_hospital = find_best_match(text)

    if best_hospital:
        print(f"Khớp với bệnh viện: {best_hospital['name']}")
        print(f"Địa chỉ: {best_hospital['address']}")
        print(f"Tọa độ: {best_hospital['coordinates']}")
    else:
        print("Không tìm thấy bệnh viện nào khớp.")
    
    response = {
        'name': best_hospital['name'],
        'address': best_hospital['address'],
        'coordinates': best_hospital['coordinates']
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)