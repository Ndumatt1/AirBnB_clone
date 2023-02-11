#!/usr/bin/python3
""" This modeule defines City class """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class to handle city object"""
    state_id = ""
    name = ""
