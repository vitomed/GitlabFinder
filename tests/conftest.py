import os
import sys


root_dir = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, os.path.abspath(root_dir))

pytest_plugins = ['test_application']
