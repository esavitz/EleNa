from flask import Flask, request, make_response
from flask_cors import CORS
from controller import controller

app = Flask(__name__) # create a Flask app
CORS(app)

# {
#     "start": string,
#     "end": string,
#     "percentage": number,
#     "max": boolean
# }


@app.route('/get_route', methods=['POST'])
def get_route():
    data = request.get_json()
    print(data)
    try:
        controller_obj = controller(data)
        model = controller_obj.get_model()
        return make_response({'route': controller_obj.get_lat_long_route(), 'gain': model.get_result_path_elevation(), 'len': model.get_result_path_length()}, 200)
    except Exception as e:
        return make_response(str(e), 500)


if __name__ == '__main__': 
    app.run() # run our Flask app default on localhost:5000