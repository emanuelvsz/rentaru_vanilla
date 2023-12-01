import sys
import os 

def input_ready():
    try:
        if os.name == 'nt':
            return
        else:
            import select
            return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])
    except:
        return False