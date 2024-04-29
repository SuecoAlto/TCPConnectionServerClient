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
data = response[3:3 + data_lenght].decode('utf-8')
print(f"This is the data from response------>{data}")

if response_type == MessageType.ACKNOWLEDGE:
    print("Server acknowledged the command.")
elif response_type == MessageType.ERROR:
    print(f"Error from server: {data}")


def get_user_command():
    """
    Displays a menu of options for the user and prompts for their choice.

    Returns:
        str: The user's choice as a string.
    """
    print("1: Turn on green light")
    print("2: Turn on blue light")
    print("3: Turn off green light")
    print("4: Turn off blue light")
    print("5: Actuate servo motor (requires additional input)")
    print("6: Query status")  
    print("Enter 'quit' to exit.")
    return input("Enter your choice: ")


def main():
    server_ip = '192.168.0.11'
    server_port = 2222

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    try: 
        while True:
            choice = get_user_command()
            if choice == 'quit':
                break
            if choice.isdigit():
                choice_num = int(choice)
                action_type = MessageType(choice_num)
                print(f"This is the action_type based on choise num-->{action_type}")
                if action_type == MessageType.ACTUATE_SERVO:
                    servo_position = input("Enter servo position (0-180): ")
                    package = create_package(action_type, servo_position)
                else:
                    package = create_package(action_type)
                client_socket.sendall(package)
                response = client_socket.recv(1024)
                handle_response(response)
        else:
            print("Invalid Input.")
    finally
        client_socket.close()


if __name__ == '__main__':
    main()