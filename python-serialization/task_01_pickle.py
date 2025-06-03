import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance of the object and save it to a file.
        
        Args:
            filename: The name of the file to save the serialized object to
            
        Returns:
            None if an error occurs, otherwise nothing
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (IOError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance of CustomObject from a file.
        
        Args:
            filename: The name of the file to load the object from
            
        Returns:
            An instance of CustomObject or None if an error occurs
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (IOError, pickle.PickleError, AttributeError):
            return None
