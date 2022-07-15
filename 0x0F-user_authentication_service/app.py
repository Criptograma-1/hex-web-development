#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, jsonify,

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """Index route"""
    return jsonify({"message": "Bienvenue"}), 200
