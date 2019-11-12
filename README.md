# KnockIt

Description
------------
Knockit is a tool that conducts port knocking attack by bruteforcing port sequences and can act as a simple port knocking client.

Requirements
-------------
* Python 3.x.x

Installing Dependencies
-------------
`pip install itertools`

Usage
-------------
```
usage: knockit.py [-h] [-d DELAY] [-b] host ports [ports ...]

positional arguments:
  host                  Hostname or IP address of the host.
  ports                 Port(s) to knock on

optional arguments:
  -h, --help            show this help message and exit
  -d DELAY, --delay DELAY
                        Delay between each knock. Default is 200 ms.
  -b, --bruteforce      Try all possible sequence combinations.
```

Examples
-------------
* Simple port knocking example: 
`python knockit.py 127.0.0.1 23 25 8080`

```
[+] Knocking on port 127.0.0.1:23
[+] Knocking on port 127.0.0.1:25
[+] Knocking on port 127.0.0.1:8080
```
`python knockit.py -b 127.0.0.1 23 25 8080`

* Bruteforce port knocking example: 
```
[+] Knockit started attacking with all the possible combinations

******************************************************
[+] Knocking with sequence: (23, 25, 8080)
[+] Knocking on port 127.0.0.1:23
[+] Knocking on port 127.0.0.1:25
[+] Knocking on port 127.0.0.1:8080
******************************************************
[+] Knocking with sequence: (23, 8080, 25)
[+] Knocking on port 127.0.0.1:23
[+] Knocking on port 127.0.0.1:8080
[+] Knocking on port 127.0.0.1:25
******************************************************
[+] Knocking with sequence: (25, 23, 8080)
[+] Knocking on port 127.0.0.1:25
[+] Knocking on port 127.0.0.1:23
[+] Knocking on port 127.0.0.1:8080
******************************************************
[+] Knocking with sequence: (25, 8080, 23)
[+] Knocking on port 127.0.0.1:25
[+] Knocking on port 127.0.0.1:8080
[+] Knocking on port 127.0.0.1:23
******************************************************
[+] Knocking with sequence: (8080, 23, 25)
[+] Knocking on port 127.0.0.1:8080
[+] Knocking on port 127.0.0.1:23
[+] Knocking on port 127.0.0.1:25
******************************************************
[+] Knocking with sequence: (8080, 25, 23)
[+] Knocking on port 127.0.0.1:8080
[+] Knocking on port 127.0.0.1:25
[+] Knocking on port 127.0.0.1:23
******************************************************
```

