#!/usr/bin/env python3

import shutil
import psutil


# returns a check if there is more than 20% free
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

# returns if the cpu usage is less than 75%
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75


if not check_disk_usage("/") or not check_cpu_usage():
    print("error!!")
else:
    print("everything is ok")
