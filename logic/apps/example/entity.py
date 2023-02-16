from uuid import UUID

from logic.apps.example.model import Example
from logic.libs.sqliteAlchemy import sqliteAlchemy
from sqlalchemy import Column, DateTime, Float, Integer, String

Entity = sqliteAlchemy.get_entity_class()


class ExampleEntity(Entity):
    __tablename__ = 'examples'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    string = Column(String(255))
    integer = Column(Integer)
    date_time = Column(DateTime)
    double = Column(Float)
    uuid = Column(String(255))

    def to_model(self) -> Example:
        return Example(
            id=self.id,
            string=self.string,
            integer=self.integer,
            date_time=self.date_time,
            double=self.double,
            uuid=UUID(self.uuid)
        )

    @staticmethod
    def from_model(m: Example) -> 'ExampleEntity':
        return ExampleEntity(
            id=m.id,
            string=m.string,
            integer=m.integer,
            date_time=m.date_time,
            double=m.double,
            uuid=str(m.uuid)
        )
