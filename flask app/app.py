from flask import Flask, render_template, request, jsonify
import serial
import time
from datetime import datetime

app = Flask(__name__)

possible_ports = ['/dev/ttyACM0', '/dev/ttyACM1', '/dev/ttyUSB0']
baud_rate = 9600
ser = None

for port in possible_ports:
    try:
        ser = serial.Serial(port, baud_rate)
        break
    except serial.SerialException:
        pass

if ser is None:
    print("Failed to open any serial port.")
    exit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_serial_messages')
def get_serial_messages():
    if ser is not None and ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        if line:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"[{timestamp}] {line}"
            return jsonify({'message': message})
        return jsonify({'message': ''})

@app.route('/monitor')
def monitor():
    return render_template('monitor.html')

@app.route('/send_commands', methods=['POST'])
def send_commands():
    commands = request.form['commands']
    individual_commands = commands.split()

    for command in individual_commands:
        if command:
            ser.write(command.encode('utf-8') + b'\n')
            time.sleep(1)

    return {'status': 'success'}

if __name__ == '__main__':
        app.run(port=5100, debug=True)