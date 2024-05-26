import os
import json
import requests

class JSONHandler:
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
      raise FileNotFoundError(f'File not found: {path}')
    
    with open(path, 'r') as file:
      return json.load(file)
  
  #############################################################################
  @staticmethod
  def get_from_url(url: str):
    """
    Get the json data from the specified url.
    """

    response = requests.get(url)

    # Raise an exception on bad response's status code
    response.raise_for_status()

    return response.json()

  #############################################################################
  @staticmethod
  def write_to_path(path: str, data: any):
    """
    Write to the json file at the specified path.
    """

    # If the file is not exist, a new file will be made
    with open(path, 'w') as file:
      json.dump(data, file, indent = 2)