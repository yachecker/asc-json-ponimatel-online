from methods import *
from translators import *

# lesson = get_lesson_by_id('*32')
# print(f"Class: {get_class_by_id(lesson['classids'][0])} | {get_subject_name(lesson['subjectid'])} - {get_group_name(lesson)} - {str(get_room_names(lesson['classroomidss'][0]))}")
# print(get_cards_by_lesson_id('*1'))


lessons = get_lessons_by_class('11a')
cards = []
lessonidtosubjectname = {}
for lesson in lessons:
  lessonID = lesson['id']
  lessonidtosubjectname[lessonID] = get_subject_name(lesson['subjectid'])
  cards += get_cards_by_lesson_id(lessonID)

mondaycards = []
for card in cards:
  if card['day'] == 5:
    mondaycards.append(card)


mondayCards = [(lessonidtosubjectname[card['lessonid']]) for card in mondaycards]
print(sorted([(card['period'], lessonidtosubjectname[card['lessonid']]) for card in mondaycards]))