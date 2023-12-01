# from flask import Flask,request,jsonify
# import json
#
# app = Flask(__name__)
#
# @app.route('/home/aman/info')
# def intro():
#     return 'Hello Python'
#
#
# @app.route('/locations')
# def get_location_names():
#     with open('venv/banglore_files/columns.json','r') as f:
#         data = json.load(f)
#     return data
#
# if __name__ == '__main__':
#     app.run()