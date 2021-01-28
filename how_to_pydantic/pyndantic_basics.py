from pydantic import BaseModel
from typing import List, Dict, Optional


class Person(BaseModel):
    name: str
    plays: str


class Band(BaseModel):

    name: str = "Ramones"  # If a default value is given, the field is optional.
    members: List[Person]
    manager: Optional[str] = "Danny"



init_data = {
    "name": "Ramones",
    "members": [Person(name="Johnny", plays="Guitar"),
                Person(**{"name": "Joey", "plays": "Vocals"}),
                Person(**{"name": "Dee Dee", "plays": "Bass"}),
                Person(**{"name": "Tommy", "plays": "Drums"})]
}

init_data = {
    "members": [Person(name="Johnny", plays="Guitar"),
                Person(**{"name": "Joey", "plays": "Vocals"}),
                Person(**{"name": "Dee Dee", "plays": "Bass"}),
                Person(**{"name": "Tommy", "plays": "Drums"})]
}

print(init_data)
band = Band(**init_data)
print(band)

print("WIP!")