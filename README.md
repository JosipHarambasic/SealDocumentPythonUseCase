## This is an example how to use the Skribble Seal API with Python

### How it works
The code takes as an Argument the PDF root path and seals it on the first page of your Document. 
This can be changed in the code, but it helps you to understand how to use it.
As a return you will get a Document ID, you can use it for further processes with the document 

### Start
1. download the code with git clone or GitHub Desktop
2. open it in an IDE for example PyCharm
3. run `pip install requests` in your terminal
4. navigate to the src folder and run `python Main.py PDFRootPath` 
5. the PDFRootPath should look like this C:\Users\Desktop\MyPDF.pdf