"""Example python script for interacting with SOAP endpoints

This script serves as a sensible starting point for python based SOAP interactions.
"""
import os
from zeep.client import Client
from collections import namedtuple
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv(verbose=True)


def apply_method(zeep_client, method, *args):
    """Given an instance of a zeep client, calls a given method.

    Args:
        zeep_client: Instance of a zeep.client.Client
        method: A WSDL method to call
        *args: any number of arguments to be given to method call
    Returns:
        Response from zeep.client.Client.service['method']
    """
    return zeep_client.service[method](*args)


if __name__ == "__main__":
    # Define Config and instantiate Object
    Config = namedtuple("Config",  "ENDPOINT")
    print(os.environ['SOAP_ENDPOINT'])
    config = Config(ENDPOINT=os.environ['SOAP_ENDPOINT'])

    # Define Zeep Client
    client = Client(config.ENDPOINT)
    print(apply_method(client, "Method1",
                       'Zeep', 'is cool'))
