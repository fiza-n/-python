from typing import NewType, TypedDict, Any, TypeVar
from dataclasses import dataclass
import random
import requests

resp = requests.get("https://google.com", timeout=5)
status = resp.status_code
print(f"Status code: {status}")


# name: str = "Fiza"
# age: int = 21

# age = "21"  # This will raise a type error if type checking is enforced

RGB = NewType('RGB', tuple[int, int , int])
HSL = NewType('HSL', tuple[int, int , int])

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    age: int |None = None
    fav_color: RGB | HSL | None = None 

# # class User(TypedDict):
# #     first_name: str
# #     last_name: str
# #     email: str
# #     age: int |None
# #     fav_color: RGB | HSL | None

# # type User = dict[str, str , int | None]  #type alias for a user dictionary

def create_user(first_name: str, last_name: str, age:int | None =  None, fav_color: RGB |HSL| None = None) -> User:
    email = f"{first_name.lower()}_{last_name.lower()}@gmail.com"
    str_age = str(age)

    return User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        age=age,
        fav_color=fav_color
    )
    # return  {
    #     "first_name": first_name,
    #     "last_name": last_name,
    #     "age":str_age,
    #     "email": email,
    #     "fav_color": fav_color
    # }

# T = TypeVar('T')
def random_choice[T](items: list[T])-> T:# PYTHON 3.12 SYNTAX
    return random.choice(items)


user1 = create_user("Fiza", "Noor", 21, )
user2 = create_user("Fiza", "Noor", 21,)
users = [user1, user2]

email = [user.email for user in users]

random_user = random_choice(users)



print(random_choice(email))
print(random_user)
