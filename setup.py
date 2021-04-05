from setuptools import setup

def readme():
    with open("README.rst") as readme:
        return readme.read()


setup(
    name="TCPot",
    description = "Simple TCP Honeypot logger and notifier",
    long_description = readme(),
    version = "0.1.0",
    author = "Jawady Muhammad Habib",
    author_email = "mjawady31@gmail.com",
    license = "MIT",
    packages = ['tpot'],
    zip_safe = False,
    install_requires = [
        #'python_requires>=3"',
        "docopt",
        "schema",
        "configparser",
        "schema"
    ]
)