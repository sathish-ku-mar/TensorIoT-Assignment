import jsonschema
from jsonschema import validate

user_schema = {
   'type': 'object',
   'properties': {
       'email': {
            "title": "Email address",
            "type": "string",
            "pattern": "^\\S+@\\S+\\.\\S+$",
            "format": "email",
            "minLength": 6,
            "maxLength": 127
       },
       'password': {
            "title": "Password",
           'type': 'string',
           "minLength": 5,
           "maxLength": 15
       },

   },
   'required': ['email', 'password']
}



def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=user_schema)
    except jsonschema.exceptions.ValidationError as err:
        return err.message
    return None