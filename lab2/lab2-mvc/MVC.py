from processing.entity.type.ControllerType import ControllerType
from processing.entity.thing.ControllerThing import ControllerThing
from processing.entity.person.ControllerPerson import ControllerPerson
from processing.entity.order.ControllerOrder import ControllerOrder
from processing.entity.departament.ControllerDepartament import ControllerDepartament
from processing.basic.View import View
from datetime import datetime as date
import datetime

# Change table by change controller
c = ControllerType(View())
table_name = c.get_table_name()
c.show_items()
attributes = list(c.get_item()[0].keys())
print("Do you want to test task 1 (Yes/No)[Y/N]:")
# c.update_item('thing_id', [6, 5, '21/12/2000', False, 3, 2, 'abs'])
# Task 1
if input().upper() == 'Y':
    print("Date input in format d/m/y")
    print("Do you want to delete row input [Y]:")
    # Task 1
    if input().upper() != 'Y':
        # Task 1 (input)
        list_input = c.get_list_input(table_name, attributes)
        print(list_input)
        c.insert_item(list_input)
        c.show_items()
    else:
        # Task 1 (delete)
        print(f"Input attribute {attributes} to delete:")
        atr = input()
        if attributes.__contains__(atr):
            print("Input value of attribute:")
            param = input()
            if param.isdigit():
                param = int(param)
            elif eval(param) or not eval(param):
                param = eval(param)
            elif type(date.strptime(param, '%d/%m/%Y')) == datetime.datetime:
                param = date.strptime(param, '%d/%m/%Y')
            c.delete_item(atr, param)
        else:
            print("WARNING: Incorrect attribute")
        c.show_items()
# Task 2
print("Do you want to test task 2 (Yes/No)[Y/N]:")
if input().upper() == 'Y':
    c.find()
# Task 3
print("Do you want to test task 3 (Yes/No)[Y/N]:")
if input().upper() == 'Y':
    c.generate_random(100)