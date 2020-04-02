"""
Class Example
"""
import datetime

class User:
    """A member of FriendFace. For now we are
    only storing their name and birthday.
    But soon we will store an uncomforable
    amount of user information."""

    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday # yyyymmdd

        # Extract first and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """Return the age of the user in years."""
        today = datetime.date(2020, 2, 21)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        date_obj = datetime.date(yyyy, mm, dd)
        age_in_days = (today - date_obj).days
        age_in_years = age_in_days / 365
        return int(age_in_years)

def main():
    user1 = User("Dave Stenner", "19871004")

    print(user1.name)
    print(user1.first_name)
    print(user1.last_name)
    print(user1.birthday)

    # help(user1) # prints class help
    print(user1.age())

if __name__ == '__main__':
    main()