#!/usr/bin/python3
"""city class."""

from models.base_model import BaseModel


class City(BaseModel):
    """city state inheriting from Basemodel."""

    state_id = ""
    name = ""
