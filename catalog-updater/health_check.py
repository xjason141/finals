#!/usr/bin/env python3

import shutil, psutil
import socket
import os
import emails_two


#error reports
def cpu_check():
    usage = psutil.cpu_percent(interval=1)
    return usage < 80.0

def disk_check():
    usage = psutil.disk_usage('/')
    return usage.percent < 80.0

def memory_check():
    memory = psutil.virtual_memory()
    THRESHOLD = 500 * 1024 * 1024  
    return memory.available < THRESHOLD

def localhost_check():
    ip = socket.gethostbyname('localhost')
    return ip == '127.0.0.1'


sender = 'automation@example.com'
recipient = 'student@example.com'
title = 'Please check your system and resolve the issue as soon as possible.'

def error_email(notice):
    prep = emails_two.generate_email(sender, recipient, title, notice)
    emails_two.send_email(prep)


if __name__ == "__main__":
    if cpu_check() == False:
        notice = "Error - CPU usage is over 80%"
        error_email(notice)

    if memory_check() == False:
        notice = "Error - Available memory is less than 500MB"
        error_email(notice)

    if disk_check() == False:
        notice = "Error - Available disk space is less than 20%"
        error_email(notice)

    if localhost_check() == False:
        notice = "Error - localhost cannot be resolved to 127.0.0.1"
        error_email(notice)