# Main
from argument_parser import ArgumentParser
from port_scanner import PortScanner
# Instantiating ArgumentParser
parser = ArgumentParser()

# Parsing the CLI arguments
args = parser.parse_arguments()

# Accessing the parsed values
target_host = args.target
port_range = args.port_range
connection_type = args.connection_type

# Instantiating the PortScanner
scanner = PortScanner(target_host, port_range, connection_type)

# Scanning ports
scanner.scan_ports()