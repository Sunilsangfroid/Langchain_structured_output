from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'Sunil' # Default value
    age: Optional[int] = None # Optional field
    email: EmailStr # Email validation
    cgpa: float = Field(gt=0,lt=10,default=8,description='A decimal value representing the cgpa of the student.') # Field validation

new_student = {'age':'22','email':'abc@gmail.com','cgpa':9} # coercing the value to int without giving any warning and error (as here age)
student = Student(**new_student)

student_dict = dict(student)
print(student_dict['age'])

student_json = student.model_dump_json()
print(student_json)


# new_student = {'name':'Sunil'}
# #new_student = {'name':90} # This will raise a validation error
# student = Student(**new_student)
# print(student)