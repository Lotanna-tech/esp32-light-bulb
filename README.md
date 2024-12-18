# esp32-light-bulb
ESP32 Web Server Controlled Light Bulb               ~Ln_pfolio

Project Overview

This project demonstrates how to create a web server using an ESP32 microcontroller and MicroPython to control a light bulb connected to a relay.

Materials:

    ESP32 board
    Relay module
    Light bulb and lampholder
    Jumper wires
    Breadboard (optional)
    Power supply (5V)


Setup:

    Connect the Hardware:
        Connect the relay module to the ESP32 according to the circuit diagram.
        Connect the light bulb to the relay module.
    Upload the MicroPython Code:
        Use a tool like Thonny or uPyCraft to transfer the MicroPython code to your ESP32.

How it Works:

    Web Server:
        The ESP32 creates a simple web server.
        This server listens for requests from your computer or smartphone.
    Web Interface:
        The web server displays a basic web page with buttons to turn the light on and off.
    Button Clicks:
        When you click a button, the web server receives a request.
    Relay Control:
        The ESP32 processes the request and sends a signal to the relay module.
        The relay module switches the light bulb on or off.

Additional Notes:

    You can customize the web interface to your liking using HTML and CSS.
    For more complex projects, you can use JavaScript to add dynamic features to the web interface.
    Consider adding security measures to protect your web server, especially if it's exposed to the internet.

This project is a great way to learn about web servers, microcontrollers, and the basics of IoT.
