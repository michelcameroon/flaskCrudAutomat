
#from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#from flask import current_app

class Table1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    description = db.Column(db.Text)
    # Other columns...

    
    def __repr__(self):
         return f'<Table1 {self.id}>'

    def __init__(self, firstName, lastName, description):
        self.fistName=firstName
        self.lastName=lastName
        self.description=description

    def get_field_names(model):
         return [column.name for column in model.__table__.columns]
         #return [column.name for column in model.students.columns]

    def get_field_namesNoId(model):
         fieldNames = Table1.get_field_names(model)
         fieldNamesNoId = []
         for fieldName in fieldNames:
             if  fieldName != 'id':
                 fieldNamesNoId.append(fieldName)
         
         return fieldNamesNoId



'''
def create_course_model(db):  # Pass db instance as an argument


    class CourseModel(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100))
        description = db.Column(db.Text)
        # Other columns...

    
        def __repr__(self):
            return f'<CourseModel {self.id}>'

        def __init__(self, name, description):
            self.name=name
            self.description=description

    return CourseModel
'''



#CourseModel = create_course_model(db)  # Call the function to create the model


