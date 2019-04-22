import sys
import os
p = os.path.abspath(    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)+'/src'

# append module src directory to sys.path
sys.path.append(p)

