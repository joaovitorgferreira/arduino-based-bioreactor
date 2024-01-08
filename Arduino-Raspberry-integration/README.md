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

