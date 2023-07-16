from flask import Flask, request, Response, jsonify
from flask import render_template
from flask_cors import CORS
import flask
import json
from collections import defaultdict
import random
import sys

import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

app = Flask(__name__)
# CORS(app)


@app.route('/',)
def get_sample():
    history = request.json['history']
    response = sample(history)[0]
    return response



if __name__ == "__main__":

    # Append the root directory to path so that the soloist folder can be accessed
    import sys
    # sys.path.insert(0, '../..')

    model_name = sys.argv[1]

    from server import *
    current_dir = os.path.dirname(__file__)
    model_path = os.path.join(current_dir, 'models', model_name)
    args.model_name_or_path = model_path
    main()

    app.run(host='0.0.0.0', port=8000)