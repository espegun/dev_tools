from pydantic import BaseModel, validator
from pydantic.error_wrappers import ValidationError
from typing import List, Dict, Optional


class Person(BaseModel):
    name: str
    plays: str

    # For more complex validations, use @validator
    @validator("name")
    def ensure_not_elvis(cls, v):
        if v == "Elvis":
            raise ValueError("He's not welcome any more.")
        return v


class Band(BaseModel):

    name: str = "Ramones"  # If a default value is given, the field is optional.
    members: List[Person]
    manager: Optional[str] = "Danny"

    # For more complex validations, use @validatorere
    # Here iterating over every item in a list.
    # Note that when validating e.g. Optional[List[Dict]], you will get
    # within the dict level when iterating. You will have to can the
    # parameter definition to Optional[List] to iterate over the list.
    # if
    @validator("members", each_item=True)
    def validate_instruments(cls, v):

        if v.plays not in ["Guitar", "Vocals", "Bass", "Drums"]:
            raise TypeError(f"{v} doesn't fit this band.")
        return v


p0 = Person(name="Johnny", plays="Guitar")
p1 = Person(name="Joey", plays="Vocals")
p2 = Person(name="Dee Dee", plays="Bass")
p3 = Person(**{"name": "Tommy", "plays": "Drums"})

print("\n=== Bad argument sent to Person ===")
try:
    init_person = {"name": "Nico", "playz": "Drums"}
    Person(**init_person)
except ValidationError:
    print(f"Oh no! Could not initiate a Person object from {init_person}")

print("\n=== Note that non-str object can be cast ===")
init_person = {"name": "Some numbers", "plays": 1.234}
print(Person(**init_person))  # This works - plays become a string through unseen str(float)

print("\n=== He's not a candidate ===")
try:
    Person(name="Elvis", plays="Drums")
except ValueError as e:
    print(e)

print("\n=== Unsuitable object to add as band member ===")
init_band = {
    "name": "Ramones",
    "members": [p0, p1, p2, p3, "Not a Person object"]
}
try:
    band = Band(**init_band)
except ValidationError as e:
    print(f"Oh no! Could not initiate a Band object from {init_band}:\n{str(e)}")

print("\n=== Unsuitable instrument for the band ===")
init_band = {
    "name": "Ramones",
    "members": [p0, p1, p2, p3, Person(name="Morten", plays="Harmonica")]
}
try:
    band = Band(**init_band)
except ValidationError as e:
    print(e)

print("\n=== Good band ===")
init_band = {
    "name": "Ramones",
    "members": [p0, p1, p2, p3]
}
band = Band(**init_band)
print(band)
