import predict
import requests
from io import BytesIO
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api',methods=['POST'])
def prediction():
    data = request.get_json(force=True)
    image = BytesIO(requests.get(data['url']).content)
    output = predict.predict(image)
    #prediction = model.predict([[np.array(data['exp'])]])
    #output = prediction[0]
    #return jsonify(output)
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=8123, debug=True)