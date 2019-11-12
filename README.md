# KnockIt

Description
------------
Knockit is a tool that conducts port knocking attack by bruteforcing port sequences and can act as a simple port knocking client.

Requirements
-------------
* Python 3.x.x_

Installing Dependencies
-------------
`pip install itertools`

Usage
-------------
`python knockit.py --help`

```
******************************************************
*                                                    *
*  _  __                     _     _____  _          *
* | |/ /                    | |   |_   _|| |         *
* | ' /  _ __    ___    ___ | | __  | |  | |_        *
* |  <  | '_ \  / _ \  / __|| |/ /  | |  | __|       *
* | . \ | | | || (_) || (__ |   <  _| |_ | |_        *
* |_|\_\|_| |_| \___/  \___||_|\_\|_____| \__|       *
*                                                    *
*                                                    *
* KnockIt v1.0                                       *
* Coded by thebish0p                                 *
* https://github.com/thebish0p/                      *
******************************************************


usage: knockit.py [-h] [-d DELAY] [-b] host ports [ports ...]

positional arguments:
  host                  Hostname or IP address of the host.
  ports                 Port(s) to knock on

optional arguments:
  -h, --help            show this help message and exit
  -d DELAY, --delay DELAY
                        Delay between each knock. Default is 200 ms.
  -b, --bruteforce      Try all possible combinations.
```

