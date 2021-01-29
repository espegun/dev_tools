from pydantic import BaseModel
from pydantic.error_wrappers import ValidationError
from typing import List, Dict, Optional


class Person(BaseModel):
    name: str
    plays: str


class Band(BaseModel):

    name: str = "Ramones"  # If a default value is given, the field is optional.
    members: List[Person]
    manager: Optional[str] = "Danny"


p0 = Person(name="Johnny", plays="Guitar")
p1 = Person(name="Joey", plays="Vocals")
p2 = Person(name="Dee Dee", plays="Bass")
p3 = Person(**{"name": "Tommy", "plays": "Drums"})

try:
    init_person1 = {"name": "Elvis", "playz": "Drums"}
    Person(**init_person1)
except ValidationError:
    print(f"Oh no! Could not initiate a Person object from {init_person1}")

init_person2 = {"name": "Elvis", "plays": 1.234}
print(Person(**init_person2))  # This works - plays become a string through unseen str(float)

init_band1 = {
    "name": "Ramones",
    "members": [p0, p1, p2, p3, "Elvis"]
}
try:
    band1 = Band(**init_band1)
except ValidationError as e:
    print(f"Oh no! Could not initiate a Band object from {init_band1}:\n{str(e)}")

init_band2 = {
    "name": "Ramones",
    "members": [p0, p1, p2, p3]
}
band2 = Band(**init_band2)
print(band2)
