from Course import Course
from Lesson import Lesson


lessons = [
    Lesson('angular', 3),
    Lesson('vue', 9),
    Lesson('react', 2),
    Lesson('redux', 4),
]
course = Course(lessons)

longest_lesson = course.max_by(lambda lesson: lesson.get_duration())
assert longest_lesson.get_duration() == 9



lessons = []
course = Course(lessons)
longest_lesson = course.max_by(lambda lesson: lesson.get_duration())
assert not longest_lesson
