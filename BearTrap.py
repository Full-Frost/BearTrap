import os
print(r"""
______               _____               
| ___ \             |_   _|              
| |_/ / ___  __ _ _ __| |_ __ __ _ _ __  
| ___ \/ _ \/ _` | '__| | '__/ _` | '_ \ 
| |_/ /  __/ (_| | |  | | | | (_| | |_) |
\____/ \___|\__,_|_|  \_/_|  \__,_| .__/ 
                                  | |    
                                  |_|    
""")

class Inputs:
    def __init__(self) -> None:
        self.ipaddress = []
        self.hostname = []
    
    def add_ip(self, IP):
        self.ipaddress.append(IP)
    
    def add_hostname(self, host):
        self.hostname.append(host)

def hostfile_edit():
    DEFAULT = '172.0.0.1 DC01.contoso.org'
    HOSTS = os.path.join('C:', 'Windows', 'System32', 'Drivers', 'etc', 'hosts')
    hostfile = open(HOSTS, 'a')
    hostfile.write(DEFAULT)
    hostfile.close()

def menu():
    print(r"""Welcome to BearTrap, a Windows honeyfile generator and distributor. Please select the option you wish to edit.
[1] IP address(s)
[2] Hostname(s)
[3] Review options
""")
    INPUT_CLASS = Inputs()
    userInput = input('Your Selection: ')
    if userInput == '1':
        addressInput = input('Please enter an IP address for use: ')
        INPUT_CLASS.add_ip(addressInput)
    elif userInput == '2':
        hostnameInput = input('Please enter a hostname for use: ')
        INPUT_CLASS.add_hostname(hostnameInput)
    elif userInput == '3':
        pass
    
def main():
    menu()

main()