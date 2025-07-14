import pytest
from sqlalchemy.orm import Session
from .database import SessionLocal, Student

@pytest.fixture(scope="module")
def db():
    """Создает сессию для работы с БД."""
    session = SessionLocal()
    yield session
    session.close()

def test_add_student(db):

    new_student = Student(name="John Doe", age=25)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    assert new_student.id is not None
    assert new_student.name == "John Doe"
    db.delete(new_student)
    db.commit()

def test_update_student(db):

    new_student = Student(name="Jane Doe", age=22)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    new_student.name = "Jane Smith"
    db.commit()
    db.refresh(new_student)

    assert new_student.name == "Jane Smith"
    db.delete(new_student)
    db.commit()

def test_delete_student(db):

    student_to_delete = Student(name="Delete Me", age=20)
    db.add(student_to_delete)
    db.commit()
    db.refresh(student_to_delete)

    student_id = student_to_delete.id
    db.delete(student_to_delete)
    db.commit()


    deleted_student = db.query(Student).filter(Student.id == student_id).first()
    assert deleted_student is None