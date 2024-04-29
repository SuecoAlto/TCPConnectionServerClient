import socket
import struct
from enum import Enum

class MessageType(Enum):
    TURN_ON_GREEN = 1
    TURN_ON_BLUE = 2
    TURN_OFF_GREEN = 3
    TURN_OFF_BLUE = 4
    ACTUATE_SERVO = 5  
    QUERY_STATUS = 6
    ACKNOWLEDGE = 7
    ERROR = 8
    
def create_package(action_type, data=''):
    """
    Creates a package by encoding the action type and data.

    Args:
        action_type (Enum): The action type.
        data (str, optional): The data to be encoded. Defaults to an empty string.

    Returns:
        bytes: The encoded package.
    """
    if not data:
        data = str(action_type.value)
    print(f"This is data in create packet before encode------>{data}")
    data_bytes = data.encode('utf-8')
    print(f"This is data in create packet after encode------>{data_bytes}")
    package = struct.pack('>BH', action_type, len(data_bytes)) + data_bytes
    return package


def handle_response(response):
    """
    Handles the response received from a server.

    Args:
        response (bytes): The response received from the server.

    Returns:
        None

    Raises:
        ValueError: If the response type is invalid.
    """
    header = response[:3]
    response_type_validation, data_length = struct.unpack('>BH', header)
    try:
        response_type = MessageType(response_type_validation)
    except ValueError:
        return
ata = response[3:3 + data_lenght].decode('utf-8')
print(f"This is the data from response------>{data}")

if response_type == MessageType.ACKNOWLEDGE:
    print("Server acknowledged the command.")
elif response_type == MessageType.ERROR:
    print(f"Error from server: {data}")

