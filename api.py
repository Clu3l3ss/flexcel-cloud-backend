from flask import Flask, jsonify, request, render_template
from flask_restful import Api, Resource, reqparse, abort
import os
import json

path = 'storage/'

app = Flask(__name__)
#api = Api(app)

#stor_put_args = reqparse.RequestParser()
#stor_put_args.add_argument("type", type=str, help="Please specify the type of data.")
#stor_put_args.add_argument("value")

#class Storage(Resource):
    #def get(self, user_id):
        #args = stor_put_args.parse_args()
        #PATH = path + str(user_id) + "/" + args['type'] + '.json'
        #if os.path.isfile(PATH) == False:
            #abort(404, message="Could not find data.")
        #with open(PATH) as f:
            #return json.load(f), 200
    #def delete(self, user_id):
    #    args = stor_put_args.parse_args()
    #    PATH = path + str(user_id) + "/" + args['type'] + '.json'
    #    if os.path.isfile(PATH) == False:
    #        abort(404, message="Could not find data.")
    #    os.remove(PATH)
    #    return '', 200
    #def put(self, user_id):
        #args = stor_put_args.parse_args()
        #PATH = path + str(user_id) + "/" + args['type'] + '.json'
        #if os.path.exists('storage') == False:
            #os.mkdir('storage')
        #if os.path.exists(path + str(user_id)) == False:
            #os.mkdir(path + str(user_id))
        #if os.path.isfile(PATH) == False:
            #with open(PATH, 'w') as fp:
                #pass
        #with open(PATH, 'w') as json_file:
            #json.dump(args['value'], json_file)
        #return '', 200

@app.route('/storage/<int:user_id>', methods=['GET', 'PUT'])
def storage(user_id):
    # GET request
    if request.method == 'GET':
        args = request.get_json()
        PATH = path + str(user_id) + "/" + args['type'] + '.json'
        if os.path.isfile(PATH) == False:
            abort(404, message="Could not find data.")
        with open(PATH) as f:
            return json.load(f), 200
    # PUT request
    if request.method == 'PUT':
        args = request.get_json()
        PATH = path + str(user_id) + "/" + args['type'] + '.json'
        if os.path.exists('storage') == False:
            os.mkdir('storage')
        if os.path.exists(path + str(user_id)) == False:
            os.mkdir(path + str(user_id))
        if os.path.isfile(PATH) == False:
            with open(PATH, 'w') as fp:
                pass
        with open(PATH, 'w') as json_file:
            json.dump(args['value'], json_file)
        return {"TEST" : "000"}, 200

#api.add_resource(storage, "/storage/<int:user_id>")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    #app.run(debug=True)
