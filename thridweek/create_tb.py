from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('mysql://root:@localhost/shiyanlou')
Base  = declarative_base(engine)
Session = sessionmaker(bind=engine)
session = Session()


class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    course_name = Column(String(10))

    def __repr__(self):
        return 'id:{},course_name:{}'.format(self.id,self.course_name)

class Lab(Base):
    __tablename__ = 'lab'
    id = Column(Integer,primary_key=True)
    course_id = Column(Integer,ForeignKey('course.id'))
    course = relationship('Course',backref='labs')

    def __repr__(self):
        return 'id:{0},name:{1}'.format(self.id,self.course_id)

class Path(Base):
    __tablename__ = 'path'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(20),nullable=False)
    config = Column(String(128))

    def __repr__(self):
        return 'id:{0},name:{1},config{2}'.format(self.id,self.name,self.config)


if __name__ == '__main__':
    Base.metadata.create_all()
