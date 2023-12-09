import logging, uuid

from flask import Flask,request
from flask_restx import Resource, Api, fields

app = Flask(__name__)
api = Api(
        app = app,
        title = 'IoT API',
        description = '自宅用IoT APIのドキュメント',
        default = 'Home IoT',
        default_label = ''
    )

toilet_get_res = api.model(
    'toileAPIのレスポンス',
    {
        'update_time': fields.Date,
        'vacancy': fields.Boolean
    }
)

toilet_post_req = api.model(
    'toileAPIのpostリクエスト',
    {
        'id': fields.String,
        'update_time': fields.Date,
        'vacancy': fields.Boolean
    }
)

bedroom_light_req = api.model(
    'ベッドルームの照明 ON/OFF',
    {
        'id': fields.String,
        'light': fields.Boolean
    }
)

@api.route('/toilet')
class toilet_api(Resource):
    @api.marshal_with(toilet_get_res, code=200, description="")
    def get(self):
        return

    @api.expect(toilet_post_req)
    def post(self):
        return
    
@api.route('/bedroom_light')
class bedroom_light(Resource):
    @api.expect(bedroom_light_req)
    def put(self):
        return
    
if __name__ == '__main__':
    app.run(debug=True)