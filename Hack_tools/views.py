import re

from django.shortcuts import render
import subprocess
from django.http import HttpResponse
from ansi2html import Ansi2HTMLConverter
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required(login_url='LoginPage')
def scanning(request):
    # return HttpResponse("scanning page")
    username = request.user.username
    regexDomain = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" +"+[A-Za-z]{2,6}"
    regexIP = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
    d = re.compile(regexDomain)
    i = re.compile(regexIP)

    if request.method == "POST":
        scanDomain = request.POST['scanDomain']
        versionScan = request.POST.get('versionScan', False)
        osScan = request.POST.get('osScan', False)
        isDomain = re.search(d,scanDomain)
        isIp = re.search(i,scanDomain)
        if isDomain or isIp :
            if versionScan == 'yes':
                AnsiResult = subprocess.check_output("nmap -T5 -sV -F " + scanDomain, shell=True)
                # convert byte to string
                AnsiResult = AnsiResult.decode()
                conv = Ansi2HTMLConverter()
                result = conv.convert(AnsiResult)

                context = {
                    'result': result,
                    'username': username
                }

                return render(request, "Hack_tools/scanResult.html", context)

            if osScan == 'yes':
                AnsiResult = subprocess.check_output("nmap -O -p22,80,443,21,23 " + scanDomain, shell=True)
                # convert byte to string
                AnsiResult = AnsiResult.decode()
                conv = Ansi2HTMLConverter()
                result = conv.convert(AnsiResult)
                context = {
                    'result': result,
                    'username': username
                }
                return render(request, "Hack_tools/scanResult.html", context)

            else:
                AnsiResult = subprocess.check_output("nmap -T4 " + scanDomain, shell=True)
                # convert byte to string
                AnsiResult = AnsiResult.decode()
                # result = result.replace('\n', '<br>')
                conv = Ansi2HTMLConverter()
                result = conv.convert(AnsiResult)

                context = {
                    'result': result,
                    'username': username
                }

                return render(request, "Hack_tools/scanResult.html", context)
                # return HttpResponse("Value is " + str(execute) )
        else:
            context = {
                'username' : username
            }
            messages.error(request, "Enter domain name or ip address ")
            return render(request,"Hack_tools/scanning.html",context)



    context = {
        'username' : username
    }
    return render(request,"Hack_tools/scanning.html",context)

@login_required(login_url='LoginPage')
def firewall(request):
    if request.method == "POST":
        firewallDomain = request.POST['firewallDomain']
        AnsiResult = subprocess.check_output("wafw00f " + firewallDomain ,shell=True)
        #convert byte to string
        AnsiResult = AnsiResult.decode()
        conv = Ansi2HTMLConverter()
        result = conv.convert(AnsiResult)
        context = {
            'result' : result
        }
        return render(request,"Hack_tools/firewallResult.html",context)

    username = request.user.username
    context = {
        'username' : username
    }
    return render(request,"Hack_tools/firewall.html",context)

def ping(request):

    regexDomain = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,6}"
    regexIP = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
    d = re.compile(regexDomain)
    i = re.compile(regexIP)
    if request.method == "POST":
        PingDomain = request.POST['scanDomain']
        isDomain = re.search(d, PingDomain)
        isIp = re.search(i, PingDomain)
        if isDomain or isIp:
            try :
                pingResult = subprocess.check_output("ping -c 4 " + PingDomain ,shell=True)
                # #convert byte to string
                pingResult = pingResult.decode()
                pingResult = re.search(r"\d received",pingResult).group(0)
                result = pingResult.split()
                result = int(result[0])
                username = request.user.username
                print(result)

                if result >= 1:
                    context = {
                        'status': 'Up',
                        'username' : username
                    }
                    return render(request,"Hack_tools/ping.html",context)
                else:
                    context = {
                        'status': 'Down',
                        'username' : username
                    }
                    return render(request, "Hack_tools/ping.html", context)
            except Exception as e:
                username = request.user.username
                print(e)
                context = {
                    'status' : 'Destination Unreachable',
                    'username' : username
                }
                return render(request, "Hack_tools/ping.html", context)
        else:
            context = {
                'username' : request.user.username
            }
            messages.error(request,"Enter domain name or ip address")
            return  render(request,"Hack_tools/ping.html",context)
    username = request.user.username
    context = {
        'username' : username
    }
    
    return render(request,"Hack_tools/ping.html",context)