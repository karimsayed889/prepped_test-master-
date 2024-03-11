import time
import random
from flask import Flask
import requests # for request API 

app = Flask(__name__)

def generate_log():
    logs = [
        "Success",
        "Created",
        "Failed",
    ]
    return random.choice(logs)

@app.route('/api_1')
def api_call():
    log_message = generate_log()
    print(f"Operation log: {log_message}")
    time.sleep(0.5)  # Wait for half a second
    return f"completed: {log_message}"

@app.route('/download_external_logs')
def api_call():
    request= requests.get("https://api.openweathermap.org/data/2.5/weather?appid={}".format(os.environ.get("EXTERNAL_INTGERATION_KEY"))) 
    return request.content

@app.route('/health_check')
def health_check():
    return f"healthy"

if __name__ == '__main__':
    app.run(debug=True)
