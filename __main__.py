# from methods import *
# from translators import *
import sys, os
import json

from classes.primary_data import get_last_primary_json

get_last_primary_json()
from classes.schlesson import SchLesson
from classes.schclass import SchClass
if not os.path.exists('./classes_json'):
    os.mkdir('classes_json')

    
inp_grade, inp_subgroup = "", 1
# Check if there are at least two arguments (the script name is the first argument)
if len(sys.argv) >= 3:
    inp_grade = sys.argv[1]  # First argument
    inp_subgroup = int(sys.argv[2])  # Second argument
else:
    print("Usage: python myscript.py arg1 arg2")


class Parser:
    @staticmethod
    def parse_timetable(className: str, subGroup: 1 | 2) -> dict:
        lessons: list[SchLesson] = SchClass.name(className).get_lessons()
        cards: list = []
        for lesson in lessons:
            cards += lesson.get_cards()

        cardsharp = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
        for card in cards:
            cardsharp[card.day].append(card)
        result_dict = {}

        for day, cardList in cardsharp.items():
            periodtuples: list = []
            for card in cardList:
                lesson = SchLesson(card.lessonid)
                group = int(lesson.group[0])

                if group == subGroup or group == 3:
                    periodtuples.append(
                        [
                            int(card.period),
                            {
                                "name": lesson.subjectName,
                                "room": lesson.classroom,
                                "teacher": lesson.teacherName,
                                "periods": lesson.periods,
                                "group": group,
                            },
                        ]
                    )

            periodtuples.sort(key=lambda x: x[0])
            result_dict[day] = periodtuples

        # Mapping of day numbers to day names
        day_names: dict[int, str] = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
        }

        # Replace day numbers with day names in the result
        sorted_result_dict = {
            day_names[day]: result_dict[day] for day in sorted(result_dict)
        }

        # Print the formatted result dictionary
        print(json.dumps(sorted_result_dict, ensure_ascii=False))

        return sorted_result_dict


Parser.parse_timetable(inp_grade, inp_subgroup)


# Parser.parse_timetable(inp_grade, inp_subgroup)
