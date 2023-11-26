from methods import *
from translators import *
import sys
sys.path.append('./classes')
from schlesson import SchLesson
from schclass import SchClass
from schcard import SchCard
from pprint import pprint
lessons = SchClass.name('11a').get_lessons()

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

for day,cardList in cardsbyday.items():
  print(day)
  perioddict=[]
  for card in cardList:
    perioddict.append((card.period, SchLesson(card.lessonid).subjectName))
  print(sorted(perioddict))

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