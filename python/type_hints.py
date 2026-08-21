from typing import NewType, TypedDict

# name: str = "Fiza"
# age: int = 21

# age = "21"  # This will raise a type error if type checking is enforced

RGB = NewType('RGB', tuple[int, int , int])
HSL = NewType('HSL', tuple[int, int , int])

class User(TypedDict):
    first_name: str
    last_name: str
    email: str
    age: int |None
    fav_color: RGB | HSL | None

# type User = dict[str, str , int | None]  #type alias for a user dictionary

def create_user(first_name: str, last_name: str, age:int | None =  None, fav_color: RGB |HSL| None = None) -> User:
    email = f"{first_name.lower()}_{last_name.lower()}@gmail.com"
    str_age = str(age)
    return  {
        "first_name": first_name,
        "last_name": last_name,
        "age":str_age,
        "email": email,
        "fav_color": fav_color
    }
user1 = create_user("Fiza", "Noor", 21, fav_color=RGB((255, 0, 0)))
user2 = create_user("Fiza", "Noor", 21, fav_color=HSL((255, 0, 0)))

print(user1)
print(user2)