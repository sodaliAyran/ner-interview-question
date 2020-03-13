from flask import Flask, jsonify, make_response, g
import itertools
from sklearn.externals import joblib
from decorators import request_handler_factory
from helpers import get_features_from_text

app = Flask(__name__)


def predict(text):
    words, features = get_features_from_text(text.lower())
    entities = crf.predict(features)
    entities = list(itertools.chain.from_iterable(entities))
    return words, entities


@app.route('/named-entity-recognition', methods=['GET', 'POST'])
@request_handler_factory()
def submit():
    words, entities = predict(g.text)
    payload = {"words": words, "entities": entities}
    return make_response(jsonify(payload), 200)


@app.errorhandler(404)
def handle_bad_request(error):
    payload = {"message": "this endpoint does not exist."}
    return make_response(jsonify(payload), 404)


@app.errorhandler(400)
def handle_bad_request(error):
    payload = {"message": "request body has no 'text' property."}
    return make_response(jsonify(payload), 400)


@app.errorhandler(500)
def handle_internal(error):
    payload = {"message": "unexpected error, please try again later"}
    return make_response(jsonify(payload), 500)


if __name__ == '__main__':
    crf = joblib.load("ner_crf.joblib")
    app.run(host='0.0.0.0')
