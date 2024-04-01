import socket
import termcolor
from func import scan

targets = input(termcolor.colored(("[*] Enter Targets To Scan(split them by ,): "), 'blue'))
ports = int(input(termcolor.colored(("[*] Enter How Many Ports You Want To Scan: "), 'blue')))
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split(','):
		scan.scan(ip_addr.strip(' '), ports)
else:
	scan.scan(targets,ports)
