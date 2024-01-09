# Arduino-Raspberry Pi integration

This Arduino-Raspberry Pi integration tutorial is based on [this article](https://roboticsbackend.com/raspberry-pi-arduino-serial-communication/).

## Basic requirements

To adjust, adapt and/or transfer the code to the Arduino board, the following software is required:

- [Arduino IDE](https://www.arduino.cc/en/software)

> For this project, version 2.1.1 was used.

In terms of hardware, we used the following:

- Arduino UNO board
- Raspberry Pi 1 B board
- USB cable

## Hardware setup for Serial communication

We use a USB cable between both Arduino and Raspberry Pi boards.

> Serial communication transfers data one bit at a time. To communicate between Arduino and Raspberry Pi, the UART protocol is used, allowing asynchronous data transfer. In multi-master UART, connected devices can send data freely, with libraries simplifying the implementation.

## Raspberry Pi setup

- Make sure your Pi has an OS installed. In case it doesn't, you can easy do so by using a SD card and installing the appropriate OS in it, using [Raspberry Pi's official Imager software](https://www.raspberrypi.com/software/).

- Once your Pi has an installed OS, connect to it by plugin a screen-mouse-keyboard setting and open a terminal.

- To avoid permission errors, make sure your user is added to the dialout group. To do so, type the following command in the terminal.

> sudo adduser your_username dialout

- To use the Serial interface with Python, you need to install the pyserial library, in case it is not already installed.

> python3 -m pip install pyserial

- Once you've done that, the Raspberry Pi setup is ready.

## Simple Serial communication from Arduino to Raspberry Pi

- Connect the Arduino board to the computer using the USB cable, open the Arduino IDE and upload the simple-serial-arduino code to the board.
- Unplug your Arduino board from your computer and connect it to the Pi board using the USB cable.
- Open the Raspberry IDE (often called Thonny), and type the simple-serial-raspberry code.

> Attention: The serial device name for the Arduino is typically '/dev/ttyACM0', '/dev/ttyUSB0', or something similar. You may need to adjust it in the code. To determine the appropriate one, open a terminal on the Raspberry Pi and execute the following command: ls /dev/tty*

- Run the serial communication code in the Raspberry Pi's IDE. The output should be a sequence of "Hello from Arduino!"

## Bidirectional Serial communication between Arduino and Raspberry Pi

- Connect the Arduino board to the computer using the USB cable, open the Arduino IDE and upload the bidirectional-serial-arduino code to the board.
- Unplug your Arduino board from your computer and connect it to the Pi board using the USB cable.
- Open the Raspberry's IDE, and type the bidirectional-serial-raspberry code.
- Run the serial communication code in the Raspberry Pi's IDE. The output should be a sequence of "You sent me: Hello from Raspberry Pi!"

### Arduino-Raspberry Serial communication application

In this simple application, after a push button is pressed on the Arduino, the Raspberry Pi generates a random integer (1 to 4) and send it to the Arduino board, which then lights up the corresponding LED and turn off the others.

To do so:

- Make the following circuit:
  
![Untitled Sketch_bb](https://github.com/joaovitorgferreira/arduino-based-bioreactor/assets/90862308/b6cff327-76d6-4329-93c5-f5990f25960e)

- Connect the Arduino board to the computer using the USB cable, open the Arduino IDE and upload the app-serial-arduino code to the board.
- Unplug your Arduino board from your computer and connect it to the Pi board using the USB cable.
- Open the Raspberry's IDE, and type the app-serial-raspberry code.
- Run the serial communication code in the Raspberry Pi's IDE. In addition to the LED being illuminated, the output should state: "Button has been pressed. Sending number X to Arduino," where X represents a number ranging from 1 to 4.





