import socket # Module that provides access to the BSD socket interface, essential for network communications.
import struct # Helps convert between Python values and C structs serialized into Python bytes objects.
import serial # Module for accessing and managing serial ports.
import threading # For running different parts of code simultaneously.
from enum import Enum # A class in Python for creating enumerations, which are a set of symbolic names bound to unique, constant values.


class EnumMessageType(Enum):
    """
    Enums are used to create a readable and reliable set of constants.
    Using enums prevents issues from using simple constants where typos or
    duplicate values might lead to bugs. They provide a way to group related
    constants and enforce exclusivity.
    """
    TURN_ON_GREEN = 1
    TURN_ON_BLUE = 2
    TURN_OFF_GREEN = 3
    TURN_OFF_BLUE = 4
    ACTUATE_SERVO = 5
    QUERY_STATUS = 6
    ACKNOWLEDGE = 7
    ERROR = 8

def create_packege(action_type, data=''): # This sets a default value for data, making the parameter optional. If data is not provided when the function is called, it defaults to an empty string.
    data_bytes = data.encode('utf-8') # This converts the string data (a Python string, which is Unicode)into bytes, necessary for network transmission, using UTF-8 encoding, which is a standard way of encoding characters as bytes.
    data_length = len(data_bytes) 
    package = struct.pack('>BH', action_type.value, data_length) + data_bytes # Used for packing data into a binary format. The format string '>BH' tells struct how to pack the data or the values (action_type.value and data_length) into a binary stream. '>' means big-endian (most significant byte first), 'B' means unsigned char (1 byte), and 'H' means unsigned short (2 bytes).
    return package

def parse_package(package_bytes):
    header = package_bytes[:3] # These bytes represent the header of the packet, containing the action type and the length of the data. In Python, [:3] means from the start of the list up to but not including the index 3. This slices the first three bytes from package_bytes.
    action_type, data_lenght = struct.unpack('>BH', header) # Unpacks the first three bytes into an action type and data length using the same format used in packing.
    data = package_bytes[3:3 + data_lenght].decode('utf-8') # This extracts bytes from index 3 to 3 + data_length, representing the actual data. It then decodes these bytes back to a string using UTF-8.
    return MessageType(action_type), data

def handle_client(conn, addr):
    print(f"Connection from {addr} established.")
    try:
    	while True:
            data = conn.recv(1024) # 1024 is the buffer size; it specifies how many bytes of data to receive at once.
            if not data:
                break
            action_type, action_data = parse_package(data) 
            if action_type == MessageType.QUERY_STATUS:
                response = create_packege(EnumMessageType.ACKNOWLEDGE, "Command Processed.")
            conn.sendall(response)
    except Exception as e:
        error_response = create_packege(EnumMessageType.ERROR, "An error occurred.")
        conn.sendall(error_response)            
    finally:
        conn.close()

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) # Opens a serial port connection at /dev/ttyACM0 (common for Arduino devices connected via USB). 9600 is the baud rate, and timeout=1 means the serial operation will wait up to 1 second for data to be available before timeing out. 
ser.flush() # Clears any input or output buffers, ensuring there are no initial transmission leftovers which might corrupt data.

host = '0.0.0.0' # allows the server to accept connections on all available IPv4 addresses.
port = 2222

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # This line creates a new socket using IPv4 (AF_INET) and TCP (SOCK_STREAM), the protocol suitable for continuous data flow.

#socket.socket(socket.) why 3 socket and what does it mean when a dot is used between functins and variables?

s.bind((host,port)) # Associates the socket with a specific network interface and port number.
s.listen()  # Enables the server to accept connections.
print(f"TCP server listning on {host}:{port}")

try: 
    while True:
        conn, addr = s.accept() #We have a dot again? why and what does it do?
        thread = threading.Thread(target=handle_client, args=(conn, addr)) # why do i need thereading? in thread = threading.Thread why is thereading dot Thread and it also have a big T? what does target and args do here?
        thread.start() 
except KeyboardInterrupt: # Catches KeyboardInterrupt (generated, for example, by pressing Ctrl+C), allowing the server to shut down gracefully.
    print("Server shutdown initiated")
    s.close()