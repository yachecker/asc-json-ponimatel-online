#from methods import *
#from translators import *
import sys
sys.path.append('./classes')
from .classes import SchClass, SchCard, SchLesson
from pprint import pprint

def govniwe() -> str:
  print('shit')

class Parser:
  @staticmethod
  def parse_timetable(className: str, subGroup: 1 | 2) -> dict:
    lessons = SchClass.name(className).get_lessons()
    cards = []
    for lesson in lessons:
      cards += lesson.get_cards()

    cardsbyday = {
      1: [],
      2: [],
      3: [],
      4: [],
      5: [],
      6: []
    }
    for card in cards:
      cardsbyday[card.day].append(card)
    result_dict = {}
    for day, cardList in cardsbyday.items():
      periodtuples = []
      for card in cardList:
        lesson = SchLesson(card.lessonid)
        group = int(lesson.group[0])
        if group == subGroup or group == 3:
          periodtuples.append((
            int(card.period),
            {
              'name': lesson.subjectName,
              'room': lesson.classroom,
              'teacher': lesson.teacherName,
              'periods': lesson.periods,
              'group': group
            }
            ))

      periodtuples.sort(key=lambda x: x[0])
      result_dict[day] = periodtuples

    # Mapping of day numbers to day names
    day_names = {
      1: 'Monday',
      2: 'Tuesday',
      3: 'Wednesday',
      4: 'Thursday',
      5: 'Friday',
      6: 'Saturday'
    }

    # Replace day numbers with day names in the result
    sorted_result_dict = {day_names[day]: result_dict[day] for day in sorted(result_dict)}

    # Print the formatted result dictionary
    pprint(sorted_result_dict)

    return sorted_result_dict


Parser.parse_timetable('12c', 1)
