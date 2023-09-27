import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / 'src'))

from main import greet

def test_greet():
    assert greet("World") == "Hello, World!"
