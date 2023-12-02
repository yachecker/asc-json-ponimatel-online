import sys, os

# sys.path.insert(0, os.path.abspath(".."))
from classes.schlesson import SchLesson
from typing import Type, List, Dict
import json

sys.path.insert(0, os.path.abspath(".."))
from classes.primary_data import get_last_primary_json

primary_data_json_name: str | None = get_last_primary_json()[1][0]
with open(os.path.abspath(primary_data_json_name), encoding="UTF-8") as json_data:
    PRIMARY_DATA = json.load(json_data)


class SchClass:
    @staticmethod
    def name(classname: str) -> "SchClass":
        class_list = SchClass.get_classes_list()
        for k, v in class_list.items():
            if v == classname:
                return SchClass(k)
        raise Exception(f"Class '{classname}' is not found")

    def __init__(self, id: str):
        self.id = id
        self.className = SchClass.get_classes_list()[self.id]

    @staticmethod
    def get_classes_list(write=False) -> dict:
        classesList = PRIMARY_DATA["r"]["dbiAccessorRes"]["tables"][12]["data_rows"]
        classes = {}
        for className in classesList:
            id = className["id"]
            name = className["name"][: className["name"].find("_")].lower()
            classes[id] = name
        if write:
            with open("./files/classes.txt", "w+", encoding="UTF-8") as f:
                f.write(str(classes))
        return classes

    def display_info(self):
        print(f"Class ID: {self.classID}")
        print(f"Class Name: {self.className}")

    def get_lessons(self, write=False) -> List["SchLesson"]:
        lessons = PRIMARY_DATA["r"]["dbiAccessorRes"]["tables"][18]["data_rows"]
        classLessons = []
        for lesson in lessons:
            if self.id in lesson["classids"]:
                classLessons.append(SchLesson(lesson["id"]))
        if write:
            with open("./files/lessons.txt", "w+", encoding="UTF-8") as f:
                f.write(str(classLessons))
        return classLessons

    def get_class_id(self) -> str:
        return self.id


# seventh_a = SchClass('*1')
# b = seventh_a.get_lessons(True)[0].get_cards()[0]
# print(b)
"""

Naming Conventions: In Python, it's a standard convention to use CamelCase for class names. So, schclass would be more appropriately named SchClass.

Static Method: The method get_classes_list is used like a static method but is not explicitly declared as one. You should decorate it with @staticmethod if it does not need access to any instance-specific data.

Error Handling: It's good to add some error handling in case the class ID is not found in the PRIMARY_DATA.

Method Accessibility: The get_classes_list method is used to initialize class attributes in the constructor. It would be better if this method is accessible without creating an instance of the class.

Variable Name Consistency: In the display_info method, you are using self.classID, but in the constructor, you are initializing self.id. These should be consistent.

Dependency on External Data: The class heavily relies on PRIMARY_DATA from an external source. Ensure that this data is always available and in the correct format.


"""
