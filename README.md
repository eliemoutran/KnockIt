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

