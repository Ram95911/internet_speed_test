import speedtest
from flask import Flask, render_template, jsonify
import threading
import time

app = Flask(__name__)

# Global variable to store speed test results
speed_results = {
    'download': 0,
    'upload': 0,
    'ping': 0,
    'is_testing': False
}

def perform_speed_test():
    global speed_results
    speed_results['is_testing'] = True
    
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        
        # Download test
        speed_results['download'] = st.download() / 1_000_000  # Convert to Mbps
        
        # Upload test
        speed_results['upload'] = st.upload() / 1_000_000  # Convert to Mbps
        
        # Ping test
        speed_results['ping'] = st.results.ping
        
    except Exception as e:
        print(f"Error during speed test: {e}")
    
    speed_results['is_testing'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-test')
def start_test():
    if not speed_results['is_testing']:
        thread = threading.Thread(target=perform_speed_test)
        thread.start()
    return jsonify({'status': 'started'})

@app.route('/get-results')
def get_results():
    return jsonify(speed_results)

if __name__ == '__main__':
    app.run(debug=True)