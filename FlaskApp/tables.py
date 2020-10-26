from flask_table import Table, Col, LinkCol

## Not sure how to delete properly.
## Look at the deletepet route too.
class petList(Table):
    classes = ['table', 'table-bordered', 'table-striped', "sortable"]
    pet_name = Col('Pet Name')
    category = Col('Category')
    age = Col('Age')
    delete = LinkCol('Delete Pet', 'view.deletepet', url_kwargs=dict(pet_name='pet_name'))
    view_special_care = LinkCol('Special Care', 'view.view_special_care', url_kwargs=dict(pet_name='pet_name'))

class specialCarePet(Table):
    classes = ['table', 'table-bordered', 'table-striped']
    care = Col('Special Care')

class CareTakerAvailability(Table):
    classes = ['table', 'table-bordered', 'table-striped']
    date = Col('Date')
    pet_count = Col('Pet Count')
    leave = Col('Leave')
    available = Col('Availability')

class UserList(Table):
    classes = ['table', 'table-bordered', 'table-striped']
    username = Col('Username')

class FilteredCaretakers(Table):
    classes  = ['table', 'table-bordered', 'table-striped']
    username = Col('Caretaker Name')
    gender = Col('Gender')
    rating = Col('Rating')
    
