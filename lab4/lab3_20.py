# Course: TC4002 Analysis, Design and Construction of Software Systems
# Enrollment: A00354823
# Author: Juan Francisco Corral Stenner

"""
Implement a class that manages a directory that is saved in a text file. The data saved includes:
a. Name
b. Email
c. Age
d. Country of Origin
The class should have capabilities to:
- Add new record
- Delete a record
- Look for a record by mail and age
- List on screen all records
"""

class User:
    def __init__(self, name, email, age, country):
        self.name = name
        self.email = email
        self.age = age
        self.country = country

class Directory:
    """A class to manage users"""
    def __init__(self, records):
        self.records = records

    def add_record(self,user):
        """Creates a new record"""
        self.records.append(user)
        return len(self.records) - 1

    def del_record(self, idx):
        """Deletes a record"""
        del self.records[idx]
        return len(self.records)

    def search_record(self, parameter):
        """Searches a record"""
        if type(parameter) in [str]:
            for record in self.records:
                if parameter in getattr(record, "age") or parameter in getattr(record, "email"):
                    return record
        return None

    def save_to_file(self, file_name):
        """Save the records to a file"""
        with open(file_name, "w") as file_obj:
            for record in self.records:
                print("{0}|{1}|{2}|{3}".format(
                    getattr(record, 'name'),
                    getattr(record, 'email'),
                    getattr(record, 'age'),
                    getattr(record, 'country')
                ), file=file_obj)

    def load_records_from_file(self, file_name):
        """Loads the records from a file"""
        with open(file_name, "r") as file_obj:
            return file_obj.read()

    def get_records(self):
        content = ""
        for record in self.records:
            content += ("{0:}|{1}|{2}|{3}\n".format(
                getattr(record, 'name'),
                getattr(record, 'email'),
                getattr(record, 'age'),
                getattr(record, 'country')
            ))
        return content

# def main():
#     user1 = User("Juan Stenner", "juan.stenner@gmail.com", "32", "MX")
#     user2 = User("Esther Rivas", "esther.rivas@gmail.com", "32", "MX")
#     user3 = User("Javier Ramos", "javier.ramos@gmail.com", "35", "MX")
#     user4 = User("Ivette Rios", "ivette.rios@gmail.com", "36", "MX")
#     directory_obj = Directory([user1,user2,user3])
#     print (directory_obj.get_records())
#     directory_obj.add_record(user4)
#     print(user4.name, "Added")
#     print("Searching")
#     match = directory_obj.search_record("juan.stenner@gmail.com")
#     print("Match:", getattr(match, "name"))
#
#     print (directory_obj.get_records())
#
#     print (directory_obj.load_records_from_file())
#
#
# if __name__ == '__main__':
#     main()
