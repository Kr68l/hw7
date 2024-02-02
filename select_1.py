from sqlalchemy import func, desc
from models import Student, Grade, Subject, Teacher, Group, Session

def select_1():
    return Session.query(Student.fullname, func.round(func.avg(Grade.value), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

def select_2(subject_name):
    return Session.query(Student.fullname, func.round(func.avg(Grade.value), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).filter(Subject.name == subject_name).group_by(Student.id)\
        .order_by(desc('avg_grade')).limit(1).all()

def select_3(subject_name):
    return Session.query(Group.name, func.round(func.avg(Grade.value), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).join(Group).filter(Subject.name == subject_name).group_by(Group.id).all()

def select_4():
    return Session.query(func.round(func.avg(Grade.value), 2).label('avg_grade')).scalar()

def select_5(teacher_name):
    return Session.query(Subject.name).join(Teacher).filter(Teacher.name == teacher_name).all()

def select_6(group_name):
    return Session.query(Student.fullname).join(Group).filter(Group.name == group_name).all()

def select_7(group_name, subject_name):
    return Session.query(Student.fullname, Grade.value).join(Group).join(Subject).filter(Group.name == group_name, Subject.name == subject_name).all()

def select_8(teacher_name):
    return Session.query(func.round(func.avg(Grade.value), 2).label('avg_grade')).join(Teacher).filter(Teacher.name == teacher_name).scalar()

def select_9(student_name):
    return Session.query(Subject.name).join(Student).filter(Student.fullname == student_name).all()

def select_10(student_name, teacher_name):
    return Session.query(Subject.name).join(Student).join(Teacher).filter(Student.fullname == student_name, Teacher.name == teacher_name).all()
