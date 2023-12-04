

class Resources:
    def __init__(self, ID, key_attribute, non_key_attribute):
        self.ID=ID
        self.key_attribute=key_attribute
        self.non_key_attribute=non_key_attribute

    def __str__(self):
        return f"*ID: {self.ID} | Key Attribute: {self.key_attribute} | Non-Key Attribute: {self.non_key_attribute}*"