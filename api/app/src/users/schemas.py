from pydantic import BaseModel

import datetime

class NewUser:
    def __init__(self, username: str, role: str):
        self.username = username
        self.role = role
        self.created_at = datetime.datetime