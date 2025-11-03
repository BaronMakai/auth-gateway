import logging
import os
import urllib.parse
import yaml

def load_config_file(config_file):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)

def parse_qs(query_string):
    return dict(urllib.parse.parse_qsl(query_string))

def get_env_variable(key, default=None):
    return os.environ.get(key, default)