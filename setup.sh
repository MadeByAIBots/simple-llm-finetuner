#!/bin/bash

# Install perf
sudo apt-get install -y linux-tools-common linux-tools-generic linux-tools-`uname -r`

# Install Python
sudo apt-get install -y python3.8 python3-pip
pip3 install --upgrade pip

# Install peft
pip3 install peft

