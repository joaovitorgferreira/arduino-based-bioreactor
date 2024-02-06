from flask import Flask, render_template, request, jsonify
import serial
import time
from datetime import datetime
import csv
import os

app = Flask(__name__)

#Detecting which USB port is being used
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

#Function to write received data to CSV file
def write_to_csv(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('messages.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([timestamp, message])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_serial_messages')
def get_serial_messages():
    if ser is not None and ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        if line:
            write_to_csv(line)
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

@app.route('/download_csv')
def download_csv():
    return send_file('messages.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(host = '143.107.203.195', port=5100, debug=True)
