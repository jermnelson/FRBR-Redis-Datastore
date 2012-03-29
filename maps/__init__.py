import sys,os

MAP_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(MAP_ROOT)[0]
FIXURES_ROOT = os.path.join(PROJECT_ROOT,'fixures')
LIB_ROOT = os.path.join(PROJECT_ROOT,'lib')

sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, LIB_ROOT)
sys.path.insert(0, FIXURES_ROOT)
