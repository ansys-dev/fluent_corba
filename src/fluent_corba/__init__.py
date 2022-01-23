import sys
import os

# Add Corba Libraries to the system path
corbaPath = os.path.dirname(__file__)
sys.path.insert(0, corbaPath)

from omniORB import CORBA
import AAS_CORBA

