from flask import Flask, request, make_response
from flask_restful import Resource, Api
from pymongo import MongoClient
from utils.mongo_json_encoder import JSONEncoder
from bson.objectid import ObjectId
import bcrypt


app = Flask(__name__)
mongo = MongoClient('localhost', 27017)
app.db = mongo.local
app.bcrypt_rounds = 12
api = Api(app)

class User(Resource):
    def post(self):

      new_hunter = request.json

      hunters_collection = app.db.Hunters

      result = myobject_collection.insert_one(new_hunter)
	  #querying for the object we just inserted into the database
      hunter_object = hunters_collection.find_one({"_id": ObjectId(result.inserted_id)})
	  #5
      return myobject
  
    def get(self, myobject_id):
      #6
      myobject_collection = app.db.myobjects
      #7
      myobject = myobject_collection.find_one({"_id": ObjectId(myobject_id)})

	  #8
      if myobject is None:
        response = jsonify(data=[])
        response.status_code = 404
        return response
      else:
        return myobject





@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(JSONEncoder().encode(data), code)
    resp.headers.extend(headers or {})
    return resp

if __name__ == '__main__':
    # Turn this on in debug mode to get detailled information about request
    # related exceptions: http://flask.pocoo.org/docs/0.10/config/
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
