from datetime import datetime

from sqlalchemy import Column, Integer, Float, Boolean, String, DateTime, JSON, ARRAY, ForeignKey, relationship, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from enum import StrEnum, auto

Base = declarative_base()


class UserModel(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(256), nullable=False, unique=True)
    first_name = Column(String(96), nullable=False)
    last_name = Column(String(96), nullable=False)
    location = Column(String(10), nullable=False)
    created = Column(DateTime, default=datetime.utcnow)
    cases = relationship('CaseModel', backref='user', lazy=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return (
            f'UserModel(id={self.id}, first_name={self.first_name}, '
            f'last_name={self.last_name}, location={self.location}, '
            f'email={self.email}, created={self.created})'
        )

class CaseModel(Base):
    __tablename__ = 'case'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False, unique=True)
    description = Column(String(1024), nullable=False, default="")
    process_owner_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    it_owner_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    doc_link = Column(String(1024), nullable=False, default="")
    date_format = Column(String(10), nullable=False, default="%m/%d/%Y")
    explicit_wait = Column(Float, nullable=False, default=0.25)
    screenshot_on_pass = Column(Boolean, nullable=False, default=False)
    screenshot_on_fail = Column(Boolean, nullable=False, default=False)
    fail_on_error = Column(Boolean, nullable=False, default=True)
    exit_on_fail = Column(Boolean, nullable=False, default=True)
    system = Column(String(256), nullable=False)
    system_metadata = Column(JSON, nullable=True)
    steps = relationship('StepModel', backref='case', lazy=True)
    data = relationship('DataModel', backref='case', lazy=True)
    status = relationship('ResultModel', backref='case', lazy=True)


class StepModel(Base):
    __tablename__ = 'step'
    id = Column(Integer, primary_key=True)
    case_id = Column(Integer, ForeignKey('case.id'), nullable=False)
    action = Column(String(96), nullable=False)
    element_id = Column(String(1024), nullable=True)
    args = Column(ARRAY(String(256)), nullable=True)
    kwargs = Column(JSON, nullable=True)
    name = Column(String(256), nullable=False, default="")
    description = Column(String(1024), nullable=False, default="")
    system_metadata = Column(JSON, nullable=True)
    py_code = Column(String(2048), nullable=True)
    status = relationship('ResultModel', backref='step', lazy=True)


class DataModel(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    case_id = Column(Integer, ForeignKey('case.id'), nullable=False)


class Result(StrEnum):
    PASS = auto()
    FAIL = auto()
    WARN = auto()


class ResultModel(Base):
    __tablename__ = 'result'
    id = Column(Integer, primary_key=True)
    case_id = Column(Integer, ForeignKey('case.id'), nullable=False)
    step_id = Column(Integer, ForeignKey('step.id'), nullable=False)
    result = None


if __name__ == "__main__":
    users = [
        UserModel(first_name='Bob', last_name='Preston', 
                email='bob.preston@example.com', location='muus'),
        UserModel(first_name='Susan', last_name='Sage', 
                email='susan.sage@example.com', location='muus')
    ]

    session_maker = sessionmaker(
        bind=create_engine('mysql+pymysql://bptaapp:bpta123@172.17.0.3/bpta'))


    def create_users():
        with session_maker() as session:
            for user in users:
                session.add(user)
            session.commit()
    
    # create_users()


    with session_maker() as session:
        user_records = session.query(UserModel).all()
        for user in user_records:
            print(user)
