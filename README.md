# KF2-SRV
*Killing Floor 2 server tool for RHEL8/CentOS8*

[![build release](https://github.com/GenZmeY/KF2-SRV/workflows/build%20release/badge.svg)](https://github.com/GenZmeY/KF2-SRV/actions?query=workflow%3A%22build+release%22)
[![tests (master)](https://github.com/GenZmeY/KF2-SRV/workflows/tests%20(master)/badge.svg?branch=master)](https://github.com/GenZmeY/KF2-SRV/actions?query=workflow%3A%22tests+%28master%29%22)
[![GitHub release](https://img.shields.io/github/v/release/genzmey/KF2-SRV)](https://github.com/genzmey/KF2-SRV/releases/latest)
[![GitHub Release Date](https://img.shields.io/github/release-date/genzmey/KF2-SRV)](https://github.com/genzmey/KF2-SRV/releases/latest)
![GitHub](https://img.shields.io/github/license/genzmey/KF2-SRV)

# Warning
There is not and most likely never will be a detailed manual. If you don't have sufficient knowledge of Linux in general and CentOS in particular, as well as the ability to learn unknown tools, you probably shouldn't use this.

# Usage
You can find actual rpm packages here(\*): https://github.com/GenZmeY/KF2-SRV/releases  
And dependencies here: https://cloud.genzmey.su/index.php/s/3GiwtDpkNyCarXc  
Basic usage information: https://github.com/GenZmeY/KF2-SRV/blob/master/SOURCES/README  

\* inotify-tools requirement can be ignored  

- Install packages `steamcmd-2018.01.05-5.el8.x86_64.rpm`, `multini-0.4.3-1.el8.x86_64.rpm`, `kf2-srv-0.18.1-1.el8.noarch.rpm`  
- `kf2-srv game update` or `kf2-srv-beta game update`  
- use `kf2-srv --help` or `kf2-srv <COMMAND> --help` to see the actions available to you and decide what to do next  

**Filesystem:**  
configs: `/etc/kf2-srv/`  
game server: `/usr/games/kf2-srv`  
game server (beta): `/usr/games/kf2-srv-beta`  
cache: `/var/cache/kf2-srv`  
logs: `/var/log/kf2-srv`  
logs (beta): `/var/logs/kf2-srv`  

# License
[GNU GPLv3](LICENSE)
