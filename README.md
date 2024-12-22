# Internet Speed Test Application

A modern web-based application that provides real-time visualization of network performance metrics using Flask and JavaScript. The application features dynamic speedometer gauges to display download speed, upload speed, and ping measurements in real-time.

## Features

- Real-time speed testing with animated gauges
- Download speed measurement in Mbps
- Upload speed measurement in Mbps
- Ping latency measurement in milliseconds
- Detailed test results with timestamps
- Responsive design that works on both desktop and mobile devices
- Asynchronous testing to prevent UI blocking

## Demo Preview


## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, for cloning the repository)

## Installation

1. Clone the repository (or download the ZIP file):
```bash
git clone https://github.com/yourusername/speed-test-app.git
cd speed-test-app
```

2. Create a virtual environment:

For Windows:
```bash
python -m venv e1
e1\Scripts\activate
```

For macOS/Linux:
```bash
python3 -m venv e1
source e1/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Project Structure
```
speed_test_app/
├── e1/
├── templates/
│   └── index.html
├── static/
├── app.py
├── requirements.txt
└── README.md
```

## Usage

1. Activate the virtual environment (if not already activated):

For Windows:
```bash
e1\Scripts\activate
```

For macOS/Linux:
```bash
source e1/bin/activate
```

2. Run the Flask application:
```bash
python app.py
```

3. Open your web browser and navigate to:
```
http://localhost:5000
```

4. Click the "Start Speed Test" button to begin testing your internet connection.

## Configuration

You can modify the gauge ranges in `templates/index.html` by adjusting the `max` values in the gauge configuration:

```javascript
const downloadGauge = new Gauge(document.getElementById('download-gauge')).setOptions({
    max: 100, // Adjust this value based on your expected maximum speed
    // ... other options
});
```

## Troubleshooting

1. **Module Not Found Errors**
   - Ensure your virtual environment is activated
   - Try reinstalling requirements: `pip install -r requirements.txt`

2. **Permission Errors**
   - For Linux/Mac: Use `sudo` for package installation
   - For Windows: Run command prompt as administrator

3. **Port Already in Use**
   - Modify the port in `app.py`:
     ```python
     if __name__ == '__main__':
         app.run(debug=True, port=5001)  # Change to any available port
     ```

## Dependencies

- Flask==3.0.0
- speedtest-cli==2.1.3
- Gauge.js (included via CDN)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request


## Acknowledgments

- [Speedtest-CLI](https://github.com/sivel/speedtest-cli) for the speed testing functionality
- [Gauge.js](https://bernii.github.io/gauge.js/) for the speedometer visualizations
- Flask team for the awesome web framework

