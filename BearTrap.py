import os
import wmi

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

class Inputs_class:
    def __init__(self) -> None:
        self.ipaddress = []
        self.hostname = []
        self.filenames = []
        self.fileextension = []
        self.usernames = []
    
    def add_ip(self, IP):
        self.ipaddress.append(IP)
    
    def add_hostname(self, host):
        self.hostname.append(host)
    
    def add_filename(self, filename):
        self.filenames.append(filename)
    
    def add_fileextension(self, fileextension):
        self.fileextension.append(fileextension)
    
    def viewInput(self):
        print('IP Address List: ' + self.ipaddress)
        print('Hostname List: ' + self.hostname)
        print('Filename List: ' + self.filenames)
        print('File Extension List: ' + self.fileextension)

def hostfile_edit(hosts_lists: list):
    DEFAULT = '172.0.0.1 DC01.contoso.org'
    HOSTS = os.path.join('C:', 'Windows', 'System32', 'Drivers', 'etc', 'hosts')
    hostfile = open(HOSTS, 'a')
    if len(hosts_lists) > 0:
        print('Adding the following hosts into the hosts file: ')
        for host in hosts_lists:
            hostfile.write(host)
            print(host)
    else:
        hostfile.write(DEFAULT)
    hostfile.close()

def get_userList():
    DEFAULT_USERS = ['Administrator', 'Guest', 'WDAGUtilityAccount', 'KRBTGT', 'DefaultAccount']
    wmiObject = wmi.WMI()
    username_list = []
    for user in wmiObject.Win32_UserAccount(['Name']):
        if user.Name in DEFAULT_USERS:
            pass
        else:
            username_list.append(user.Name)
    return username_list

def honey_pdf():
    pass

def honey_excel():
    pass

def honey_text():
    pass

def honey_word():
    pass

def run():
    pass

def menu():
    print(r"""Welcome to BearTrap, a Windows honeyfile generator and distributor. Please select the option you wish to edit.
[1] IP address(s)
[2] Hostname(s)
[3] Filename(s)
[4] File Extension(s)
[5] Review options
[6] Run
""")
    INPUT_CLASS = Inputs_class()
    while(True):
        userInput = input('Your Selection: ')
        if userInput == '1':
            addressInput = input('Please enter an IP address for use: ')
            INPUT_CLASS.add_ip(addressInput)
        elif userInput == '2':
            hostnameInput = input('Please enter a hostname for use: ')
            INPUT_CLASS.add_hostname(hostnameInput)
        elif userInput == '3':
            filenameInput = input('Please enter a filename for use: ')
            INPUT_CLASS.add_filename(filenameInput)
        elif userInput == '4':
            fileextensionInput = input('Please enter a file extension for use: ')
            INPUT_CLASS.add_fileextension(fileextensionInput)
        elif userInput == '5':
            INPUT_CLASS.viewInput()
        elif userInput == '6':
            break
    
def main():
    menu()

main()