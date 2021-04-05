"""TCPot

Simple TCP Honeypot logger and notifier

Usage:
    tcpot log <config_file> 
    tcpot -h | --help
    tcpot -v | --version

Options:
    <config_file>   Path to config file
    -h --help       Display help dialog 
    -v --version    Display version 
"""

# Todo tcpot notify <config_file>
# Notify module required for next commit

import sys
import os
from docopt import docopt
from schema import Schema, And, Use, Or, SchemaError

import configparser

from tcpot import TCPpot

FALLBACK_CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "default.ini")


arguments = docopt(__doc__, version="0.1.0 Alpha")
schema = Schema({
    '<config_file>': Use(lambda x: x if os.access(x, os.R_OK) else FALLBACK_CONFIG_PATH, error='<config_file> should be writeable, Configure fallback config instead?'),
    'log': And(lambda state: state, error='TCPot state not specified'),
    '--version': Or(Use(lambda state: state)),
    '--help': Or(Use(lambda state: state))
})
try:
    arguments = schema.validate(arguments)
except SchemaError as e:
    exit(e)


config_file_path = arguments["<config_file>"]

try:
    if FALLBACK_CONFIG_PATH == config_file_path:
        print(f"""
    Warning: 
    <config_file> not specified correctly.
    RESOLVING TO FALLBACK FILE {FALLBACK_CONFIG_PATH} .
        """)
except NameError as e:
    """
    FALLBACK_CONFIG_PATH doesnt exist
    """
    pass

# config handling
config = configparser.ConfigParser()
config.read(config_file_path)


ports = config.get('default', 'ports', raw=True, fallback="4444, 2222")
bind = config.get('default', 'bind', raw=True, fallback="0.0.0.0")
log_file_path = config.get(
    'default', 'logfile', raw=True, fallback="/var/log/tcpot.log")

# starting honeypot
honeypot = TCPpot(bind, ports, log_file_path)
honeypot.listen()
