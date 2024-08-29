# Packet-Sniffer
Sniffer For Http Credentials Requests

this packet sniffer searching for the http connection to get back the credentials like username and password for you

as well as it will sniff for the ip protocal whether it TCP or UDP

also will tell the source and destination IP and Ports

it has been bulit using scapy library


the system (linux) is prefered 

#
#

### REQUIREMENTS : 

scapy library you should download if you don't have 

python3 is required on your system

pyfiglet library you should download if you don't have

argparse library you should download if you don't have

#
#

### INSTALLATION :

//copy this commands and past it in your terminal

***cd ~/Desktop***

***git clone https://github.com/SIRunstoppable/Packet-Sniffer.git***

#

Python is typically pre-installed on most Linux distributions. You can check your Python version with :

***python3 --version***

if it told you that no python install , you can install it with command :

***sudo apt-get install python3***

#

write this commands to complete installation process : 

***sudo apt-get install python3-pip***

***pip3 install scapy***

***pip3 install pyfiglet***

OR

you can install scapy and pyfiglet by command :

***pip3 install scapy pyfiglet***

#
#

### Run The Tool With Command : 

//enter the dir

***cd packet-sniffer***

// you should specify your interface you want to sniff it's data for example **eth0**

// you can know which inter face to specify by write command : 

***ifconfig***

//then you can write this command and replace the "<interface>" word with your real interface :

***sudo python3 packet_sniffer.py -i <interface>***

or

***sudo python3 packet_sniffer.py --interface <interface>***

//you can write --help to know more about this tool


//If get any issue don't histate to ask and also try to get root privillages :

***sudo su***

#
#

### NOTE : 

This project does not accept contributions or modifications from external users.

If you wish to make changes, please fork the repository and do so on your own copy but is likely not best practice and definitely in need of optimization/cleanup. Any pull requests are appreciated!.
