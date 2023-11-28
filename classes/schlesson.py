import sys
sys.path.append('..')
from .schcard import SchCard
from methods import get_primary_data
from typing import List, Dict, Type
PRIMARY_DATA = get_primary_data()

class SchLesson:
  def __init__(self, id: str):
    lessonsList = PRIMARY_DATA['r']['dbiAccessorRes']['tables'][18]["data_rows"]
    self.id = ''
    for lesson in lessonsList:
      if lesson['id'] == id:
        self.id = id
        subject_id = lesson['subjectid']
        teacher_id = lesson['teacherids']
        classroom_id = lesson['classroomidss']
        group = lesson['groupnames'][0] if lesson['groupnames'][0] else '3'
        #print([*group])
        periods = lesson['durationperiods']
        self.subject_id = subject_id # get subject name,
        self.teacher_id = teacher_id[0] # get teacher name
        self.classroom = self.get_rooms_list()[classroom_id[0][0]] if len(classroom_id) else [] # get classroom name
        self.group = group.strip().replace(' ', '')
        self.periods = periods


        # TODO: adapt for 12th grade subject name
        subjectName = self.get_subjects_list()[self.subject_id]
        subjects = {
          'г': 'География',
          'ф': "Физика",
          "и": "Информатика",
          'р': 'Графика',
          'э': 'Экономика',
          "х": "Химия",
          "б": "Биология"
        }
        if 'Стандарт' in subjectName or '12кл_' in subjectName:
          subjectName = subjects[self.group[-4].lower()]
          # TODO: 12th grade profile subject choose plz omg stfu
          self.group = self.group[-3] + ' группа'
        match subjectName:
          case 'М_Мат_12кл':
            subjectName = 'МЭСК: Математика'
          case 'М_Мат_10':
            subjectName = 'МЭСК: Математика'
          case 'М_КСМ_12кл':
            subjectName = 'МЭСК: КСМ'
          case 'МЭСК Я1 12кл':
            subjectName = 'МЭСК: Я1'
          case 'М_Я2_10':
            subjectName = 'МЭСК: Я2'
          case 'М_Я1_10':
            subjectName = 'МЭСК: Я1'
          case 'М_Я2_11кл':
            subjectName = 'МЭСК: Я2'
          case 'М_ИстКаз_10':
            subjectName = 'МЭСК: История Казахстана'
          case 'Под.МЭСК.каз':
            subjectName = 'МЭСК: Профильный предмет'
          case 'Под.МЭСК.рус':
            subjectName = 'МЭСК: Профильный предмет'
            
            
        self.subjectName = subjectName
        self.teacherName = self.get_teachers_list()[self.teacher_id]['name']
        break
    if self.id == '':
      raise Exception('there is no lesson with id:' , id)
    self.id = id

  def get_subjects_list(write=False) -> dict:
    subjectsList = PRIMARY_DATA['r']['dbiAccessorRes']['tables'][13]["data_rows"]
    subjects = {}
    for recordDict in subjectsList:
      subjects[recordDict['id']] = recordDict['name']
      #sabyrzhan if you want color as well, please uncomment code below
      #subjects[recordDict['id']] = {'name': recordDict['name'], 'color': recordDict['color']}
    if write:
      with open('./files/subjects.txt','w+', encoding='UTF-8') as f:
        f.write(str(subjects))
    return subjects
  
  
  def get_rooms_list(self) -> dict:
    rooms_list = PRIMARY_DATA['r']['dbiAccessorRes']['tables'][11]["data_rows"]
    rooms = {}
    for room in rooms_list:
      if len(''.join(filter(str.isdigit, room['name']))) > 2:
        rooms[room['id']] = ''.join(filter(str.isdigit, room['name']))
      elif len(''.join(filter(str.isdigit, room['name']))) == 2:
        rooms[room['id']] = ''.join(filter(str.isdigit, room['name'])) + 'P'
      else:
        rooms[room['id']] = room['name']
    return rooms

  def get_teachers_list(self, write=False) -> dict:
    teachersList = PRIMARY_DATA['r']['dbiAccessorRes']['tables'][14]["data_rows"]
    teachers = {}
    for teacher in teachersList:
      teachers[teacher['id']] = {
        'name': teacher['short'],
        'color': teacher['color']
      }
    if write:
      with open('./files/teachers.txt','w+', encoding='UTF-8') as f:
        f.write(str(teachers))
    return teachers


  def get_cards_list(self, write=False) -> List['SchCard']:
    cardsList = PRIMARY_DATA['r']['dbiAccessorRes']['tables'][20]["data_rows"]
    cards = []
    for card in cardsList:
      period = card["period"]
      dayConvertDict = {'10000': 1,'01000': 2,'00100': 3,'00010':4,'00001':5, '': 6}
      day = dayConvertDict[card['days']]
      lessonID = card['lessonid']
      classRoomId = card['classroomids']
      cards.append({'lessonid': lessonID,
        'period':period,
        'day': day,
        'classRoomId': classRoomId,
      })
    if write:
      with open('./files/cards.txt','w+', encoding='UTF-8') as f:
        f.write(str(cards))
    return cards


  def get_cards(self) -> list:
    cardslist = self.get_cards_list()
    cards = []
    for card in cardslist:
      if card['lessonid'] == self.id:
        cards.append(SchCard(self.id, card['day'], card['period'], card['classRoomId']))
    return cards
    
  def __str__(self) -> str:
    return f"CLASS: 'LESSON' | Lesson ID: {self.id}, Subject: {self.subjectName}, Teacher Name: {self.teacherName}, Classroom ID: {self.classroom_id}, Group: {self.group}"
  
  
  def pprint(self):
    print(self.subjectName, self.teacherName)