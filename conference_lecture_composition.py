from datetime import time, timedelta

class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        for obj, name in ([start_time, "start_time"], [duration, "duration"]):
            hours, minutes = map(int, obj.split(":"))
            self.__dict__[name] = timedelta(hours=hours, minutes=minutes)


class Conference:
    def __init__(self):
        self.lectures = []
        
    def add(self, lecture):
        if not self.lectures:
            self.lectures.append(lecture)
        else:
            lecture_start = lecture.start_time
            lecture_end = lecture.start_time + lecture.duration
            
            for added_lecture in self.lectures:
                added_lecture_start = added_lecture.start_time
                added_lecture_end = added_lecture.start_time + added_lecture.duration
                
                overlap_start = max(added_lecture_start, lecture_start)
                overlap_end = min(added_lecture_end, lecture_end)
                if overlap_start < overlap_end:
                    raise ValueError("Провести выступление в это время невозможно")
                    
            self.lectures.append(lecture)
            
    @staticmethod
    def _translate_timedelte_to_time(tdelta):
        total_seconds = tdelta.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int(total_seconds % 3600 // 60)
        return time(hours, minutes)
    
    def total(self):
        total_time = timedelta()
        for lecture in self.lectures:
            total_time += lecture.duration
        tm = self._translate_timedelte_to_time(total_time)
        return time.strftime(tm, "%H:%M")
    
    def longest_lecture(self):
        max_duration = timedelta()
        for lecture in self.lectures:
            max_duration = max(max_duration, lecture.duration)
        tm = self._translate_timedelte_to_time(max_duration)
        return time.strftime(tm, "%H:%M")

    def longest_break(self):
        max_break = timedelta()
        sorted_lectures = sorted(self.lectures, key=lambda lecture: lecture.start_time)
        for i in range(len(sorted_lectures) - 1):
            lecture_break = sorted_lectures[i + 1].start_time - (sorted_lectures[i].start_time + sorted_lectures[i].duration)
            max_break = max(max_break, lecture_break)
            
        tm = self._translate_timedelte_to_time(max_break)
        return time.strftime(tm, "%H:%M")

# TEST_1:
conference = Conference()

conference.add(Lecture('Простые числа', '08:00', '01:30'))
conference.add(Lecture('Жизнь после ChatGPT', '10:00', '02:00'))
conference.add(Lecture('Муравьиный алгоритм', '13:30', '01:50'))
print(conference.total())
print(conference.longest_lecture())
print(conference.longest_break())

# TEST_2:
conference = Conference()
conference.add(Lecture('Простые числа', '08:00', '01:30'))

try:
    conference.add(Lecture('Жизнь после ChatGPT', '09:00', '02:00'))
except ValueError as error:
    print(error)

# TEST_3:
conference = Conference()
conference.add(Lecture('Декоратор @property', '09:30', '00:30'))
conference.add(Lecture('Свойства', '09:00', '00:30'))
conference.add(Lecture('Модификаторы доступа и аксессоры', '08:30', '00:30'))

print(conference.longest_lecture())
print(conference.longest_break())

# TEST_4:
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))
conference.add(Lecture('Декоратор @singledispatchmethod', '09:00', '00:30'))
conference.add(Lecture('Создание, инициализация и очищение объектов', '11:00', '00:30'))
conference.add(Lecture('Унарные операторы и функции', '10:45', '00:15'))
conference.add(Lecture('Арифметические операции', '10:00', '00:30'))
conference.add(Lecture('Вызываемые объекты', '08:00', '01:00'))

print(conference.total())
print(conference.longest_lecture())
print(conference.longest_break())

# TEST_5:
conference = Conference()

conference.add(Lecture('Жизнь после ChatGPT', '10:00', '02:00'))
print(conference.total())
print(conference.longest_lecture())
print(conference.longest_break())