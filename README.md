
# Project Information

This Project is Information Security toolkit, that provide three hacking/security re
search tool. 
1. Port Scanning 
2. Firewall Detection 
3. Ping It 

## 1.Port Scanning 
Port scanning is a method of determining which ports on a network are open and 
could be receiving or sending data. It is also a process for sending packets to specific 
ports on a host and analyzing responses to identify vulnerabilities. 

## 2.Firewall Detection 
 Firewall determine that WAF(Web Application Firewall) is enable or disable. This 
website uses popular tool ‘waffw00f’ in backend. 
## 3.Ping It 
 This tool determine website is down or up. This website send 4 ping packets (ICMP 
echo request) and calculate received response.




# Installation

Run this project on pentesting distribution like Kali Linux where Nmap, Wafw00f installed.

Install these dependencies

```bash
  pip3 install django
  pip3 install ansi2html  
```

Change database configuration in Hacker/settings.py

then run these commands
```bash
    python3 manage.py migrate 
```
```bash
    python3 manage.py runserver 8000 
```
## Screenshots

![Home Page](/Screenshots/01homepage.png?raw=true "Home page")

![Login Page](/Screenshots/02loginpage.png?raw=true "Login page")

![Port Scan](/Screenshots/03portscannig.png?raw=true "Port scan")

![Port Scan Page](/Screenshots/04portscanpage.png?raw=true "Port scan page")

![Port scan result Page](/Screenshots/05portscanresult.png?raw=true "Port result page")


## 🚀 About Me
I'm a full stack developer...

Follow me on my Twitter -> @cyberjaygoswami