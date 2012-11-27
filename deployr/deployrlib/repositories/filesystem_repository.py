# -*- coding: utf-8 -*-
"""

    <application_name>    

    created by hgschmidt on 26.11.12, 22:27 CET
    
    Copyright (c) 2012 apitrary

"""

def write_file(filename, content):
    """
        Write a given content to a file with given filename.
    """
    with open(filename, 'w') as f:
        f.write(content)
        f.write('\n')


