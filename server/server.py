from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names',methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET','POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bedroom = int(request.form['bedroom'])
    bath = int(request.form['bath'])
    asd = util.get_estimated_price(location,total_sqft,bedroom,bath)
    print(f"PARAMS ARE : location: {location}, total_sq: {total_sqft}, bed: {bedroom}, bath: {bath}, res is : {asd}")
    response = jsonify({
        'estimated_price': asd
    })
    
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


# @app.route('/distribute_inheritance', methods=['POST'])
# def calculate():
#     house_price = int(request.form['InheritancePrice'])
#     sons = int(request.form['sons'])
#     daughters = int(request.form['daughters'])
#     sisters = int(request.form['sisters'])
#     brothers = int(request.form['brothers'])
#     wives = int(request.form['wives'])
#     husband = request.form['husband'] == "yes"
#     mother = request.form['mother'] == "yes"
#     father = request.form['father'] == "yes"

#     response = jsonify({
#         'Inheritance': util.distribute_inheritance(house_price,sons,daughters,brothers,sisters,husband,wives,father,mother)
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')

#     return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()