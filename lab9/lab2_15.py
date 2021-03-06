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
import random
import logging


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

    def __str__(self):
        return self.name

class Directory:
    """A class to manage users"""
    def __init__(self, records):
        self.records = records

    def create_record(self,user):
        """Creates a new record"""
        logger.info("Creating '{}' user".format(user))
        try:
            logger.info("Appending '{}' to records".format(user))
            self.records.append(user)
        except:
            logger.error("Unable to add '{}'".format(user))
            print(" Unable to add user")

    def save_records_to_file(self, file_name):
        """Save the records to a file"""
        logger.info("Saving records to '{}'".format(file_name))
        with open(file_name, "w") as file_obj:
            for record in self.records:
                print("Name: {0:20s} Address: {1:20s} Phone: {2:20s} email: {3:20s}".format(
                    getattr(record, 'name'),
                    getattr(record, 'address'),
                    getattr(record, 'phone'),
                    getattr(record, 'email')
                ), file=file_obj)

    def load_records_from_file(self, file_name):
        """Loads the records from a file"""
        logger.info("Loading records from '{}'".format(file_name))
        try:
            with open(file_name, "r") as file_obj:
                self.file_content = file_obj.read()
            logger.info("{} successfully read".format(file_name))
                # print(file_name, "successfully read")
        except:
            logger.error("Unable to read '{}'".format(file_name))
            print(" Unable to read: ", file_name)

    def search_record(self, idx):
        logger.info("Searching for user at index '{}'".format(idx))
        print("Name: {0:20s} Address: {1:20s} Phone: {2:20s} email: {3:20s}".format(
            getattr(self.records[idx], 'name'),
            getattr(self.records[idx], 'address'),
            getattr(self.records[idx], 'phone'),
            getattr(self.records[idx], 'email')
        ))

    def print_records(self):
        logger.info("Printing records")
        for record in self.records:
            print("Name: {0:20s} Address: {1:20s} Phone: {2:20s} email: {3:20s}".format(
                getattr(record, 'name'),
                getattr(record, 'address'),
                getattr(record, 'phone'),
                getattr(record, 'email')
            ))

def main():
    file_name = "lab2-15-records.txt"
    user1 = User("Juan Stenner", "Paseos del Sol", "33-33-33-33-33", "juan.stenner@oracle.com")
    user2 = User("Francisco Corral", "Ciudad del Sol", "11-11-11-11-11", "francisco.corral@hotmail.com")
    user3 = User("Guido Python", "Guido Address", "22-22-22-22-22", "guido.python@yahoo.com")

    directory_obj = Directory([user1, user2, user3])

    print("{:=^50}".format(" Content of the Directory "))
    directory_obj.print_records()

    user4 = User("Esther Rivas", "Zapopan", "44-44-44-44-44", "esther.rivas@hotmail.com")

    print("{:=^50}".format(" Adding a new record "))
    directory_obj.create_record(user4)
    directory_obj.print_records()

    directory_obj.save_records_to_file(file_name)
    directory_obj.load_records_from_file(file_name)

    print("{:=^50}".format(" Content of " + file_name + " "))
    print(directory_obj.file_content)

    random_ix = random.randrange(0, len(directory_obj.records))

    print("{:=^50}".format(" Searching and printing a random record "))
    directory_obj.search_record(random_ix)

LOG_FORMAT = "[%(levelname)s] <%(asctime)s> <%(funcName)s: %(message)s>"

logging.basicConfig(level=logging.DEBUG,
                    datefmt="%Y/%m/%d %H:%M:%S",
                    format=LOG_FORMAT,
                    handlers=[logging.FileHandler('lab2_15.log', mode='w'), logging.StreamHandler()]
                    )
logger = logging.getLogger()


if __name__ == '__main__':
    main()

