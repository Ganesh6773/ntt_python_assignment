from flask import Flask, jsonify
from flask import request
import argparse
from file_parser import FileParser
app = Flask(__name__)

fileParser = FileParser('./data.txt')


def setup_app():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', dest='txtFile', default='./data.txt',
                        help='text file with structured data to be parsed')
    args = parser.parse_args()
    fileParser = FileParser(args.txtFile)
    app.run(debug=True)


@app.route('/', methods=['GET'])
def index_route():
    return jsonify({'about': 'python assignment'})


@app.route('/interface/<path:interface>', methods=['GET'])
def interface_route(interface):
    if(interface == 'all'):
        return jsonify(fileParser.getAllInterfaces())
    else:
        return jsonify(fileParser.getInterface(interface))


if(__name__ == "__main__"):
    setup_app()
