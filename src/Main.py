import base64
import json
from json import JSONEncoder

import Document
import Position
import SealDocument
import User
import VisualSignature
"""Need this class to encode our Document Object into a JSON string"""
class DocumentEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

def main():
    userLogin = User.UserCredentials("api_demo_skribble_d901_0", "118d6d49-1415-4f8e-bd16-2a0ef03beaf9")
    token = userLogin.createToken()
    print(token)
    content = encodeToBase64("C:\\Users\\41786\\OneDrive\\Desktop\\FormField.pdf")
    visual_signature = VisualSignature.VisualSignature(Position.Position(20,40,100,100,"0"))
    account_name = "ais_demo_seal"
    document = Document.Document(content, account_name, visual_signature)
    documentAsJSON = DocumentEncoder().encode(document)
    docm = json.dumps(document, indent=4, cls=DocumentEncoder)
    print(docm)
    seal = SealDocument.SealDocument()
    response = seal.seal(token,content)
    print(response)


"""We need this code to convert out PDF into base 64 to send it as content in the JSON request body for the Seal"""
def encodeToBase64(filepath):
    with open(filepath, "rb") as pdf_file:
        return base64.b64encode(pdf_file.read()).decode("utf-8")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


