from jinja2 import Environment, FileSystemLoader
from jinja2 import Template
from docxtpl import DocxTemplate

doc = DocxTemplate("Test.docx")



data = {
    'ClientName': "Maggy Miggins",
    'ClientFirstName': "Maggy",
    'Objectives': ["Make piles of money", "Make loads of money"]
}


## In the actual docx file, use {% for line in address -%}, because the dash before the closing % sign removes newlines after each entry
## Nested dictionaries can have each line accessed with:

## {% for x, AddressLine in Address.items() %}
## {{ AddressLine }}
## {% endfor % }

## Otherwise you'll print the variable names

data['Address'] =  {
    'Addressee': "Mrs M Miggins",
    'FirstLine': "123 Fake Street"
}



## You can change dict items. You don't even have to define the item in the original declaration of the data dict
## This will still work if you remove the Objectives line from the initial declaration of data 
data["Objectives"] = ["Be less of a fool", "make wonga"]



doc.render(data)

doc.save("output.docx")

