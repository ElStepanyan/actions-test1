from flask import Flask
from flask import jsonify
    
import os,platform,socket,psutil


appName = os.getenv('F_NAME', 'F_APP_DEFAULT')

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(
        application = appName,
        ipAddress = socket.gethostbyname(socket.gethostname()),
        hostName = socket.gethostname(),
        platform = platform.system(),
        architecture = platform.machine(),
        processor = platform.processor(),
        ram = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
    )
