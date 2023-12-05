import json

class UserInteractivity:
    def __init__(self, resource_management, data_info):
        self.resource_management=resource_management
        self.data_info=data_info

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
        self.resource_management.edit_resource(ID, latest_non_key_attribute)

    def delete_resource(self):
        ID = input("Please enter the resource ID to delete: ")
        self.resource_management.delete_resource(ID)

    def show_all_resources(self):
        full_resources = self.resource_management.get_full_resources()
        for resource in full_resources:
            print(resource)
























class Resources:
    def __init__(self, ID, key_attribute, non_key_attribute):
        self.ID=ID
        self.key_attribute=key_attribute
        self.non_key_attribute=non_key_attribute

    def __str__(self):
        return f"*ID: {self.ID} | Key Attribute: {self.key_attribute} | Non-Key Attribute: {self.non_key_attribute}*"
    
