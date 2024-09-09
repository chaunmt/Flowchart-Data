"""
This module contains classes that help handle specific file format.
"""

import os
import json
import requests
from requests.exceptions import Timeout, HTTPError, RequestException

class JSONHandler():
    """
    Class to help handle json files.
    """

    #############################################################################
    @staticmethod
    def get_from_path(path: str):
        """
        Get the json data from the specified path.
        """

        if not os.path.exists(path):
            raise FileNotFoundError(f'File not found: {path}.')

        with open(path, 'r', encoding='utf-8') as file:
            # print(f'Data is fetched from {path}.')
            return json.load(file)

    #############################################################################
    @staticmethod
    def get_from_url(url: str):
        """
        Get the json data from the specified url.
        """
        
        while True:
            try:
                response = requests.get(url, timeout=10)

                # Raise an exception on bad response's status code
                response.raise_for_status()
                
                # print(f'Data is fetched from {url}.')
                return response.json()
            except Timeout:
                print("Timeout error occured. Retry request.")
            except HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}. Retry request.")
            except RequestException as err:
                print(f"An error occurred: {err}. Retry request.")

    #############################################################################
    @staticmethod
    def write_to_path(path: str, data: any) -> None:
        """
        Write to the json file at the specified path.
        """

        # If the file is not exist, a new file will be made
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent = 2)

        print(f'Data is dumped to {path}.')
