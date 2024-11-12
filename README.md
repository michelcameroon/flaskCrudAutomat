# flaskCrudAutomat:
create new crud change only models.py :
class for table and fields definitions
__init__ with fields of table and these 2 funtions for the fieldnames

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

i have try to work in app.py only with the instance of Table1 but not going ervery where, why?
i should b e a good ides to work only with instance especially when we work with 2 or more tables
