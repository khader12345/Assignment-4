import json

#User interactivty class is made that represents the interaction with the user.

class UserInteractivity:
    def __init__(self, resource_management, data_info):
        self.resource_management = resource_management
        self.data_info = data_info

#The user is given the ID, Key attribute and non-key attribute prompts to create the resource.
#Allows the user to create resources and adds them to the resource manager’s collection. 
#For each resource the user will specify the attributes associated with the resource. 

    def create_resource(self):
        ID = input("Please enter the resource ID: ")
        key_attribute = input("Please enter the key attribute: ")
        non_key_attribute = input("Please enter the non-key attribute: ")
        self.resource_management.create_resource(ID, key_attribute, non_key_attribute)

#The different methods all have an important role for the program to work such as "read_resources" that searches for a resource.
#)Allows the user to search for a given resource based on:
#a.	One key attribute, and 
#b.	One non-key attribute. 

    def read_resources(self):
        key_attribute = input("Please enter the key attribute for resource to read: ")
        non_key_attribute = input("Please enter the non-key attribubte for resource to read: ")
        establish_resources = self.resource_management.read_resources(key_attribute, non_key_attribute)
        for resource in establish_resources:
            print(resource)

#This method is created to update a resource from the user.
#Allows the user to select a resource using a unique characteristic (e.g., ID, Code, etc.) 
#The UI module shall use the services of the resource manager to update the information of the matching resource, 
#by supplying new values for the rest of its attributes.

    def update_resource(self):
        ID = input("Please enter resource ID to update: ")
        latest_non_key_attribute = input("Please enter the new non-key attribute: ")
        self.resource_management.update_resource(ID, latest_non_key_attribute)

#This method is made to delete a resource from the user.
#Allows the user to select a resource using a unique characteristic and delete it from the application’s collection. 
#The UI module shall use the services of the resource manager to search and delete the information.

    def delete_resource(self):
        ID = input("Please enter the resource ID to delete: ")
        self.resource_management.delete_resource(ID)

#The method is created to display all the resources that have been made to the user when the user wants to see it.

    def show_all_resources(self):
        full_resources = self.resource_management.get_full_resources()
        for resource in full_resources:
            print(resource)

#This is the user menu to interact with the user.

    def menu(self):
        while True:
            print("\n*Menu*")
            print("1. |Create Resource|")
            print("2. |Read (Search) Resources|")
            print("3. |Edit Resource|")
            print("4. |Delete Resource|")
            print("5. |Show All Resources|")
            print("6. |Save Resource and Exit|")

            option = input("\nPlease enter your option for the prompts provided above: ")

#The if and elif statements are defined as shown and each input from the user from the prompts provided above connects 
#to the methods that have been defined in the user interactivity class. 

            if option=='1':
                self.create_resource()
            elif option=='2':
                self.read_resources()
            elif option=='3':
                self.update_resource()
            elif option=='4':
                self.delete_resource()
            elif option=='5':
                self.show_all_resources()
            elif option=='6':
                self.save_resource_exit()
                break
            else:
                print("*Incorrect option please try again correctly*")

#This saves the resources to the file before exiting. 

    def save_resource_exit(self):
        self.data_info.store_info(self.resource_management.get_full_resources())

#Resource class is defined thats being managed to represent a separate resource.

class Resources:

    def __init__(self, ID, key_attribute, non_key_attribute):
        self.ID=ID
        self.key_attribute=key_attribute
        self.non_key_attribute=non_key_attribute

#A string method is used to represent a resource. 

    def __str__(self):
        return f"*ID: {self.ID} | Key Attribute: {self.key_attribute} | Non-Key Attribute: {self.non_key_attribute}*"
    
#Class name "ResourceManagement" that represents the functionality required to create, read, update, delete a resource and manage a resource.
    
class ResourceManagement:
    def __init__(self):
        self.resources = []

#Method to make a new resource.

    def create_resource(self, ID, key_attribute, non_key_attribute):
        resource = Resources(ID, key_attribute, non_key_attribute)
        self.resources.append(resource)

#Method to search for a resource based on the attributes.

    def read_resources(self, key_attribute, non_key_attribute):
        return [resource for resource in self.resources
                if key_attribute.lower() in str(resource.key_attribute).lower()
                and non_key_attribute.lower() in str(resource.non_key_attribute).lower()]
    
#Method to update a resource.
    
    def update_resource(self, ID, latest_non_key_attribute):
        for resource in self.resources:
            if resource.ID == ID:
                resource.non_key_attribute = latest_non_key_attribute

#Method to delete a resource.

    def delete_resource(self, ID):
        self.resources = [resource for resource in self.resources if resource.ID != ID]

#Method to get all the resources. 

    def get_full_resources(self):
        return self.resources
    

class ExceptionHandling(Exception):
    pass

#Handling exception created to handle any errors during the resource creation. 
#Program handles both user input exceptions as well as environment exceptions.
#The program makes effective use of defensive programming techniques.

class UserExceptionHandling(UserInteractivity):
    def create_resource(self):
        try:
            super().create_resource()
        except Exception as e:
            print(f"Error: {e}")
            self.create_resource()

#Handling exceptions during the resource readings (searches).

    def read_resources(self):
        try:
            super().read_resources()
        except Exception as e:
            print(f"Error: {e}")
            self.read_resources()

#Handling exceptions during the resource editing. 

    def update_resource(self):
        try:
            super().update_resource()
        except Exception as e:
            print(f"Error: {e}")
            self.update_resource()

#Handling exceptions during the resource deletion.

    def delete_resource(self):
        try:
            super().delete_resource()
        except Exception as e:
            print(f"Error: {e}")
            self.delete_resource()

#Class named "DataPresistence" is created that represents code that is responsible with saving and loading resource data into / from files. 

class DataPresistence:
    def __init__(self, resource_path='data.txt'):
        self.resource_path = resource_path

#Method to store resource information in a file.

    def store_info(self, resources):
        with open(self.resource_path, 'w') as storage:
            for resource in resources:
                storage.write(f"{resource.ID},{resource.key_attribute},{resource.non_key_attribute}\n")

#The "try" method reads resource information from a file.
#It also analyzes the stored information and makes resource object.
#At the end if the file is not found it returns an empty list.

    def process_data(self):
        try:
            with open(self.resource_path, 'r') as storage:
                info = [code.strip().split(',') for code in storage]
                return [Resources(*resource_info) for resource_info in info]
        except FileNotFoundError:
            return[]
        
#This part at the end is for the functionality of the code
#It makea a DataPresistence object with the default file path.
#A ResourceManagement object is made.
#It also loads existing resources from the data file.
#A UserExceptionHandling object is made for user interaction.
#The code at the very end it to start the user interaction menu.

if __name__ == '__main__':
    data_info = DataPresistence()
    resource_managment = ResourceManagement()
    resource_managment.resources = data_info.process_data()

    UserInterface = UserExceptionHandling(resource_managment, data_info)
    UserInterface.menu()
