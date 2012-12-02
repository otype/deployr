# -*- coding: utf-8 -*-
"""

    deployr

    created by hgschmidt on 26.11.12, 22:40 CET
    
    Copyright (c) 2012 apitrary

"""
from deployrlib.repositories import filesystem_repository

def write_file(filename, content):
    """
        Write a given content to a file with given filename.
    """
    return filesystem_repository.write_file(filename=filename, content=content)