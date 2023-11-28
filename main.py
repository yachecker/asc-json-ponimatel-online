from methods import *
from translators import *
import sys
sys.path.append('./classes')
from classes import SchClass, SchCard, SchLesson
from pprint import pprint


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
        print(lesson.group)
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


Parser.parse_timetable('12a',1)


"""
        'Monday':[
          {
            'name': 'Кураторский час',
            'room': '222',
            'teacher':'Каримова Арайлым',
            'periods':1
          },
          {
            'name': 'Музыка',
            'room': '303',
            'teacher':'Амангельды Айсулу',
            'periods':1
          },
          {
            'name': 'Информатика',
            'room': '254',
            'teacher':'Ахметова Балгын',
            'periods':2
          },
                  {
            'name': 'Физика',
            'room': '242',
            'teacher':'Тутебаева Айсулу',
            'periods':1
          },
          {
            'name': 'Домбыра',
            'room': '',
            'teacher':'Токтаган Айтжан',
            'periods':1
          },
          {
            'name': 'Математика',
            'room': '223',
            'teacher':' ',
            'periods':1
          },
        ],

      }      'Monday':[
          {
            'name': 'Кураторский час',
            'room': '222',
            'teacher':'Каримова Арайлым',
            'periods':1
          },
          {
            'name': 'Музыка',
            'room': '303',
            'teacher':'Амангельды Айсулу',
            'periods':1
          },
          {
            'name': 'Информатика',
            'room': '254',
            'teacher':'Ахметова Балгын',
            'periods':2
          },
                  {
            'name': 'Физика',
            'room': '242',
            'teacher':'Тутебаева Айсулу',
            'periods':1
          },
          {
            'name': 'Домбыра',
            'room': '',
            'teacher':'Токтаган Айтжан',
            'periods':1
          },
          {
            'name': 'Математика',
            'room': '223',
            'teacher':'Джубатканов Кушаныш',
            'periods':1
          },
        ],

      }

  """
  # lesson = get_lesson_by_id('*32')
  # print(f"Class: {get_class_by_id(lesson['classids'][0])} | {get_subject_name(lesson['subjectid'])} - {get_group_name(lesson)} - {str(get_room_names(lesson['classroomidss'][0]))}")
  # print(get_cards_by_lesson_id('*1'))


  # lessons = get_lessons_by_class('11a')
  # cards = []
  # lessonidtosubjectname = {}
  # for lesson in lessons:
  #   lessonID = lesson['id']
  #   lessonidtosubjectname[lessonID] = get_subject_name(lesson['subjectid'])
  #   cards += get_cards_by_lesson_id(lessonID)

  # mondaycards = []
  # for card in cards:
  #   if card['day'] == 5:
  #     mondaycards.append(card)


  # mondayCards = [(lessonidtosubjectname[card['lessonid']]) for card in mondaycards]
  # print(sorted([(card['period'], lessonidtosubjectname[card['lessonid']]) for card in mondaycards]))