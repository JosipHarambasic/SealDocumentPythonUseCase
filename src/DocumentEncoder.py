from json import JSONEncoder

"""Need this class to encode our Document Object into a JSON string"""
class DocumentEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__