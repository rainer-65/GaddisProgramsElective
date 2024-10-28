import json

# Define JSON data as String
# JSON validation: https://jsonformatter.curiousconcept.com/
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "cooking"]
}

try:
    # pretty print JSON data
    # dumps: converts a Python object (like a dictionary) into a JSON formatted string
    pretty_json = json.dumps(data, indent=4)
except json.JSONDecodeError as e:
    print(f"JSONDecodeError: {e}")

# Print pretty JSON
print(pretty_json)
print(type(pretty_json))

# Printing first hobby
print("First Hobby in List: " + data["hobbies"][0])


# JSON string data
employee_string = '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}'

# Check data type with type() method
print(type(employee_string))

# Convert string to  object
# loads: converts string to object
json_object = json.loads(employee_string)

# Check new data type
print(type(json_object))

# Output
# <class 'dict'>

# Access first_name in dictionary
print(json_object["first_name"])

employees_string = '''
{
    "employees" : [
       {
           "first_name": "Michael", 
           "last_name": "Rodgers", 
           "department": "Marketing"

        },
       {
           "first_name": "Michelle", 
           "last_name": "Williams", 
           "department": "Engineering"
        }
    ]
}
'''
data = json.loads(employees_string)

print(type(data))
# output
# <class 'dict'>

# Access first_name
for employee in data["employees"]:
    print(employee["last_name"])