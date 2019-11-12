#!/usr/bin/python3

import socket
import itertools
import sys
import time
import argparse

print("\n******************************************************")
print("*                                                    *")
print("*  _  __                     _     _____  _          *")
print("* | |/ /                    | |   |_   _|| |         *")
print("* | ' /  _ __    ___    ___ | | __  | |  | |_        *")
print("* |  <  | '_ \  / _ \  / __|| |/ /  | |  | __|       *")
print("* | . \ | | | || (_) || (__ |   <  _| |_ | |_        *")
print("* |_|\_\|_| |_| \___/  \___||_|\_\|_____| \__|       *")
print("*                                                    *")
print("*                                                    *")
print("* KnockIt v1.0                                       *")
print("* Coded by thebish0p                                 *")
print("* https://github.com/thebish0p/                      *")
print("******************************************************\n\n")

class Knockit(object):
    def __init__(self, args: list):
        self._parse_args(args)

    def _parse_args(self, args: list):
        parser = argparse.ArgumentParser()
        parser.add_argument('-d', '--delay', type=int, default=200,
                            help='Delay between each knock. Default is 200 ms.')
        parser.add_argument('-b', '--bruteforce', help='Try all possible combinations.', action='store_true')
        parser.add_argument('host', help='Hostname or IP address of the host.')
        parser.add_argument('ports', type=int, help='Port(s) to knock on', nargs='+')

        args = parser.parse_args(args)
        self.delay = args.delay / 1000
        self.ports = args.ports
        self.bruteforce = args.bruteforce
        self.host= args.host


    def knockit(self):
        self.ports = list(map(int, self.ports))
        if (self.bruteforce):
            print("[+] Knockit started attacking with all the possible combinations\n")
            print("******************************************************")            
            for port_list in itertools.permutations(self.ports):

                print("[+] Knocking with sequence: %s" % (port_list,))
                for port in port_list:
                    print("[+] Knocking on port %s:%s" % (self.host,port))
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(self.delay)
                    sock.connect_ex((self.host, port))
                    sock.close()

                print("******************************************************")

        else:
            for port in self.ports:
                print("[+] Knocking on port %s:%s" % (self.host,port))
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(self.delay)
                sock.connect_ex((self.host, port))
                sock.close()


if __name__ == '__main__':
    Knockit(sys.argv[1:]).knockit()