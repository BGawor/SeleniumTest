#  Script will install required module dependencies
import importlib, sys, os
import subprocess

print("INSTALLING MODULES USING PIP")

module = 'selenium'

try:
	importlib.import_module(module)
	print"installed " + module
except ImportError:
	subprocess.call("pip install " + module)