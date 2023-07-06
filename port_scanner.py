# Port-Scanner
import socket

class PortScanner:
    def __init__(self, target_host, port_range, connection_type):
        self.target_host = target_host
        self.port_range = port_range
        self.connection_type = connection_type
        self.open_ports = []
        self.closed_ports = []
        self.filtered_ports = []

    def scan_ports(self):
        print(f"Scanning ports for {self.target_host}...")
        for port in self.get_ports_to_scan():
            try:
                self.establish_connection(port)
                self.determine_port_status(port)
                # self.perform_banner_grabbing(port)
            except Exception as e:
                self.handle_error(e)
            self.display_scan_results()

    def get_ports_to_scan(self):
        start_port, end_port = map(int, self.port_range.split('-'))
        return range(start_port, end_port + 1)
    
    def establish_connection(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Setting a timeout for the connection attempt
            sock.settimeout(2)
            result = sock.connect_ex((self.target_host, port))
            if result == 0:
                self.open_ports.append(port)
            elif result == 11:
                self.filtered_ports.append(port)
            else:
                self.closed_ports.append(port)
    
    def determine_port_status(self, port):
        if port in self.open_ports:
            print(f"\nPort {port} is open")
        elif port in self.closed_ports:
            print(f"\nPort {port} is closed")
        elif port in self.filtered_ports:
            print(f"\nPort {port} is filtered")

    # def perform_banner_grabbing(self, port):
        # pass

    def display_scan_results(self):
        print("Scan Results:")
        print(f"Open Ports: {self.open_ports}")
        print(f"Closed Ports: {self.closed_ports}")
        print(f"Filtered Ports: {self.filtered_ports}")

    def handle_error(self, exception):
        print(f"An error occurred: {str(exception)}")
