import argparse

class ArgumentParser:
    def __init__(self) :
        self.parser = argparse.ArgumentParser(description='Port Scanner')
        self.add_arguments()

    def add_arguments(self):
        # Adding the necessary arguments to the parser
        self.parser.add_argument('target', help='Target host (IP address or domain)')
        self.parser.add_argument('-p', '--port-range', help='Port range (e.g., 1-100)')
        self.parser.add_argument('-c', '--connection-type', choices=['tcp', 'udp'], default='tcp', help='Connection type (default: tcp)')
    
    def parse_arguments(self):
        # Parsing the command-line arguments and returning the parsed values
        return self.parser.parse_args()
    

