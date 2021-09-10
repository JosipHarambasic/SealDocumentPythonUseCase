import base64
import json
from json import JSONEncoder

import Document
import Position
import SealDocument
import User
import VisualSignature


def main():
    """Set the User credentials username and api-key"""
    userLogin = User.UserCredentials("api_demo_skribble_d901_0", "118d6d49-1415-4f8e-bd16-2a0ef03beaf9")

    """create the token"""
    token = userLogin.createToken()

    """give the full path of the pdf file that you want to seal"""
    content = encodeToBase64("C:\\Users\\41786\\OneDrive\\Desktop\\FormField.pdf")

    """make a visual signature where and how the seal should look like"""
    visual_signature = VisualSignature.VisualSignature(Position.Position(20,40,100,100,"0"))

    """create the document with all it needs for the API call"""
    document = Document.Document(content, "ais_demo_seal", visual_signature)

    """transform the Document into a JSON file"""
    documentAsString = DocumentEncoder().encode(document)
    documentAsJSON = json.loads(documentAsString)

    """seal the document and get the Document ID so we can do further operations with it"""
    seal = SealDocument.SealDocument()
    response = seal.seal(token,documentAsJSON)
    print(response)


"""We need this code to convert out PDF into base 64 to send it as content in the JSON request body for the Seal"""
def encodeToBase64(filepath):
    with open(filepath, "rb") as pdf_file:
        return base64.b64encode(pdf_file.read()).decode("utf-8")

"""Need this class to encode our Document Object into a JSON string"""
class DocumentEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


