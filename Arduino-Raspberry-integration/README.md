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
- Open the Raspberry IDE (often called Thonny), and type the simple-serial-raspberry code.


