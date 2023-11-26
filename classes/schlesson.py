import sys
sys.path.append('..')
from schcard import SchCard
from methods import get_primary_data
PRIMARY_DATA = get_primary_data()

class SchLesson:
  
  
  def __init__(self, id):
    lessonsList = PRIMARY_DATA['r']['dbiAccessorRes']['tables'][18]["data_rows"]
    self.id = ''
    for lesson in lessonsList:
      if lesson['id'] == id:
        self.id = id
        subject_id = lesson['subjectid']
        teacher_id = lesson['teacherids']
        classroom_id = lesson['classroomidss']
        group = lesson['groupnames']
        self.subject_id = subject_id # get subject name, 
        self.teacher_id = teacher_id[0] # get teacher name 
        self.classroom_id = classroom_id[0] if len(classroom_id) else '' # get classroom name
        self.group = group # have get group
        self.subjectName = self.get_subjects_list()[self.subject_id]
        self.teacherName = self.get_teachers_list()[self.teacher_id]['name']
        break
    if self.id == '':
      raise Exception('there is no lesson with id:' , id)        
        
      
    
    
    self.id = id
    
    
  def get_subjects_list(write=False):
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
  
  
  def get_rooms_list():
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
  
  
  def get_teachers_list(write=False):
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

		
  def get_cards_list(write=False):
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


  def get_cards(self):
    cardslist = self.get_cards_list()
    cards = []
    for card in cardslist:
      if card['lessonid'] == self.id:
        cards.append(SchCard(self.id, card['day'], card['period'], card['classRoomId']))
    return cards
    
  def __str__(self):
    return f"CLASS: 'LESSON' | Lesson ID: {self.id}, Subject: {self.subjectName}, Teacher Name: {self.teacherName}, Classroom ID: {self.classroom_id}, Group: {self.group}"
  
  
  def pprint(self):
    print(self.subjectName, self.teacherName)