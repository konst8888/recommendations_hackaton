import datetime
import sys
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException
from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics
from mnfst_network_latency_exporter import NetworkLatencySender
import os

app = Flask(__name__)
app.wsgi_app = NetworkLatencySender(app.wsgi_app)
app.wsgi_app = AppOpticsApmMiddleware(app.wsgi_app)
appmetrics = GunicornPrometheusMetrics(app, export_defaults=False)


@app.route('/hc', methods=['GET'])
def hc():
    return jsonify({'success': True})


@app.route('/api/recommend', methods=['POST'])
def v1_image_recognition():
    current_time = datetime.datetime.now()
    result = ImageRecognition(request.json).classify()
    print(
        f'TOTAL: {datetime.datetime.now() - current_time}', file=sys.stdout)
    return jsonify({'data': result})


@app.route('/api/recognition/v1/video', methods=['POST'])
def v1_video_recognition():
    return jsonify({'data': VideoRecognition(request.json).classify()})

if __name__ == '__main__':
    app.run()
