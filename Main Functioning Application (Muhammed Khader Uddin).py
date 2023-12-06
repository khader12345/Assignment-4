import json

class UserInteractivity:
    def __init__(self, resource_management, data_info):
        self.resource_management = resource_management
        self.data_info = data_info

    def create_resource(self):
        ID = input("Please enter the resource ID: ")
        key_attribute = input("Please enter the key attribute: ")
        non_key_aatribute = input("Please enter the non-key attribute: ")
        self.resource_management.create_resource(ID, key_attribute, non_key_aatribute)

    def read_resource(self):
        key_attribute = input("Please enter the key attribute for resource to read: ")
        non_key_attribute = input("Please enter the non-key attribubte for resource to read: ")
        establish_resources = self.resource_management.read_resources(key_attribute, non_key_attribute)
        for resource in establish_resources:
            print(resource)

    def update_resources(self):
        ID = input("Please enter resource ID to update: ")
        latest_non_key_attribute = input("Please enter the new non-key attribute: ")
        self.resource_management.update_resource(ID, latest_non_key_attribute)

    def delete_resource(self):
        ID = input("Please enter the resource ID to delete: ")
        self.resource_management.delete_resource(ID)

    def show_all_resources(self):
        full_resources = self.resource_management.get_full_resources()
        for resource in full_resources:
            print(resource)

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

            if option=='1':
                self.create_resource()
            elif option=='2':
                self.find_resource()
            elif option=='3':
                self.change_resource()
            elif option=='4':
                self.delete_resource()
            elif option=='5':
                self.show_all_resources()
            elif option=='6':
                self.save_resource_exit()
                break
            else:
                print("*Incorrect option please try again correctly*")

    def save_resource_exit(self):
        self.data_info.store_data(self.resource_management.get_full_resources())



class Resources:

    def __init__(self, ID, key_attribute, non_key_attribute):
        self.ID=ID
        self.key_attribute=key_attribute
        self.non_key_attribute=non_key_attribute

    def __str__(self):
        return f"*ID: {self.ID} | Key Attribute: {self.key_attribute} | Non-Key Attribute: {self.non_key_attribute}*"
    
class ResourceManagement:
    def __init__(self):
        self.resources = []

    def create_resource(self, ID, key_attribute, non_key_attribute):
        resource = Resources(ID, key_attribute, non_key_attribute)
        self.resources.append(resource)

    def find_resource(self, key_attribute, non_key_attribute):
        return [resource for resource in self.resources
                if key_attribute.lower() in str(resource.key_attribute).lower()
                and non_key_attribute.lower() in str(resource.non_key_attribute).lower]
    
    def change_resource(self, ID, non_key_attribute):
        for resource in self.resources:
            if resource.ID == ID:
                resource.non_key_attribute = non_key_attribute

    def delete_resource(self, ID):
        self.resources = [resource for resource in self.resources if resource.ID != ID]

    def show_all_resources(self):
        return self.resources
       



    
