
from flask import Flask, jsonify, Response, request
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

request_count = Counter(
    'examination_http_requests_total',
    'Total HTTP requests received',
    ['method', 'endpoint']
)

@app.before_request
def count_requests():
    request_count.labels(
        method=request.method,
        endpoint=request.endpoint or 'unknown'
    ).inc()

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Online Examination Platform",
        "status": "Running"
    })

@app.route('/exam')
def exam():
    return jsonify({
        "exam_name": "DevOps Examination",
        "subject": "DevOps",
        "duration": "60 minutes",
        "total_questions": 3
    })

@app.route('/questions')
def questions():
    return jsonify({
        "questions": [
            {
                "id": 1,
                "question": "What is Kubernetes?",
                "options": ["Container orchestration", "Database", "Operating System"]
            },
            {
                "id": 2,
                "question": "What is Docker?",
                "options": ["Container platform", "Programming language", "Browser"]
            },
            {
                "id": 3,
                "question": "What is a Pod?",
                "options": ["Smallest deployable unit in Kubernetes", "A Docker image", "A network"]
            }
        ]
    })

@app.route('/metrics')
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=15000)
