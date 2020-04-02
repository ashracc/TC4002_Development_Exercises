# Course: TC4002 Analysis, Design and Construction of Software Systems
# Enrollment: A00354823
# Author: Juan Francisco Corral Stenner

"""
Create a class to manage a directory of users containing data
Name
Address
Phone
Email
    The class must be enable:
    1- Creation of new record
    2- Save all records in a file
    3- Load records from a file
    4- Search and get data from a given record
"""


class User:
    """A member of a directory containing info like
Name
Address
Phone
Email"""
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email


class Directory:
    """A class to manage users"""
    def __init__(self, records):
        self.records = records

    def create_record(self,user):
        """Creates a new record"""
        self.records.append(user)

    def save_records_to_file(self, file_name):
        """Save the records to a file"""
        with open(file_name, "w") as file_obj:
            for record in self.records:
                print("{0}|{1}|{2}|{3}".format(
                    getattr(record, 'name'),
                    getattr(record, 'address'),
                    getattr(record, 'phone'),
                    getattr(record, 'email')
                ), file=file_obj)

    def load_records_from_file(self, file_name):
        """Loads the records from a file"""
        try:
            with open(file_name, "r") as file_obj:
                return file_obj.read()
        except:
            return None

    def search_record(self, parameter):
        """Searches a record"""
        if type(parameter) in [str]:
            for record in self.records:
                #print("Param: {0} vs {1} or {2}".format(parameter, getattr(record, 'name'), getattr(record, 'email')))
                if parameter in getattr(record, 'name') or parameter in getattr(record, 'email'):
                    return record
        return None
