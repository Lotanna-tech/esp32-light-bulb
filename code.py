import network
import socket
from machine import Pin
import time

# Wi-Fi credentials
WIFI_SSID = "Netfiber"       # Replace with your Wi-Fi SSID
WIFI_PASS = "1975QHEAL"   # Replace with your Wi-Fi password

# Relay Pin Configuration (GPIO 5)
relay = Pin(5, Pin.OUT)
relay.value(0)  # Start with relay OFF

# Connect to Wi-Fi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASS)
    print("Connecting to Wi-Fi...")
    while not wlan.isconnected():
        time.sleep(1)
    print("Connected to Wi-Fi:", wlan.ifconfig())

# HTML page for relay control
html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relay Control</title>
    <style>
        /* General Page Styles */
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #000000, #66a6ff);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            color: #ffffff;
            text-align: center;
        }
        
        h1 {
            margin-bottom: 20px;
            font-size: 2.5rem;
        }

        /* Button Styling */
        .button-container {
            display: flex;
            gap: 20px;
        }

        a {
            text-decoration: none;
        }

        button {
            font-size: 1.2rem;
            padding: 15px 30px;
            background: #FFA500; /* Green */
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        button:hover {
            background:#000000; /* Darker Green */
            transform: scale(1.05);
        }

        button:active {
            background: #388e3c; /* Even Darker Green */
            transform: scale(0.98);
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }
    </style>
</head>
<body>
    <h1>Relay Control</h1>
    <div class="button-container">
        <a href="/on"><button>Turn ON</button></a>
        <a href="/off"><button>Turn OFF</button></a>
    </div>
</body>
</html>
"""




# Create the web server
def web_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Listening on', addr)

    while True:
        cl, addr = s.accept()
        print('Client connected from', addr)
        request = cl.recv(1024)
        request_str = str(request)
        print("Request:", request_str)
        
        if '/on' in request_str:
            relay.value(1)  # Turn ON relay
            print("Relay ON")
        elif '/off' in request_str:
            relay.value(0)  # Turn OFF relay
            print("Relay OFF")
        
        # Send the HTML page
        cl.send('HTTP/1.1 200 OK\r\n')
        cl.send('Content-Type: text/html\r\n')
        cl.send('\r\n')
        cl.send(html)
        cl.close()

# Connect to Wi-Fi
connect_to_wifi()

# Start the web server
web_server()

