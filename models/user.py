#!/usr/bin/python3
""" Inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Inherits from BaseModel
    Args:
    email - string
    password - string
    first_name - string
    last_name - string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
