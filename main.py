from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, Date, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("postgresql://land_registry:land_registry@db:5432/land_registry")
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True)
    paon = Column(Text, nullable=True)
    saon = Column(Text, nullable=True)
    street = Column(Text, nullable=True)
    locality = Column(Text, nullable=True)
    town = Column(Text, nullable=True)
    district = Column(Text, nullable=True)
    county = Column(Text, nullable=True)
    postcode = Column(Text, nullable=True)
    tenure = Column(Text, nullable=False)
    property_type = Column(Text, nullable=True)
    sales = relationship("Sale", backref="property")


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    is_new_build = Column(Boolean, nullable=False)

    property_id = Column(Integer, ForeignKey("properties.id"), nullable=False)


def main():
    pass

if __name__ == "__main__":
    main()
