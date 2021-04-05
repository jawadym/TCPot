.. role:: raw-html(raw)
    :format: html

============================
TCPot 
============================

------------------------------------------
A simple TCP Honeypot logger and notifier.  
------------------------------------------

^^^^^^^^^^
Setup
^^^^^^^^^^

* Python is installed (Unless you're using a brutally lightweight distro. Probably not ideal for documentation production).
* Install TCPot by typing the following commands to the terminal::
  
     sudo python3 setup.py develop

^^^^^^^^^^
Usage
^^^^^^^^^^
tcpot log <config_file> 
tcpot -h | --help
tcpot -v | --version

Options:
    <config_file>   Path to config file
    :raw-html:`<br />`  
    -h --help       Display help dialog
    :raw-html:`<br />`
    -v --version    Display version
    :raw-html:`<br />`

To run TCPot::

     python3 -m tcpot --help

Started by Muhammad Habib Jawady.
:raw-html:`<br />`  
Project is still under development!