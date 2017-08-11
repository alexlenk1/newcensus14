from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref

engine = create_engine('postgresql://postgres:joseph@localhost/newcensus11')
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, Sequence("state_id_seq"), primary_key=True)
    user = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zipcode = Column(String)
    geography_id = Column(Integer, ForeignKey('geography.id'))

    geography = relationship('Geography', backref=backref('address', order_by=id))

class Geography(Base):
    __tablename__ = 'geography'
    id = Column(Integer, Sequence("geography_id_seq"), primary_key=True)
    state = Column(String)
    county = Column(String)
    tract = Column(String)
    blockgrp = Column(String)
    block = Column(String)
    geoid = Column(String)

    censusdatablk_id = Column(Integer, ForeignKey('censusdatablk.id'))

    censusdatablk = relationship('CensusDataBlk', backref=backref('censusdatablk', order_by=id))


class CensusDataBlk(Base):
    __tablename__ = 'censusdatablk'
    id = Column(Integer, Sequence('censusdatablk_id_seq'), primary_key=True)
    B02008_001E = Column(String)
    B02009_001E = Column(String)
    B02010_001E = Column(String)
    B02011_001E = Column(String)
    B02012_001E = Column(String)
    B02013_001E = Column(String)
    B03002_001E = Column(String)
    B03002_002E = Column(String)
    B03002_003E = Column(String)
    B03002_004E = Column(String)
    B03002_005E = Column(String)
    B03002_006E = Column(String)
    B03002_007E = Column(String)
    B03002_008E = Column(String)
    B03002_009E = Column(String)
    B03002_010E = Column(String)
    B03002_011E = Column(String)
    B03002_012E = Column(String)
    B03002_013E = Column(String)
    B03002_014E = Column(String)
    B03002_015E = Column(String)
    B03002_016E = Column(String)
    B03002_017E = Column(String)
    B03002_018E = Column(String)
    B03002_019E = Column(String)
    B03002_020E = Column(String)
    B03002_021E = Column(String)
    B09002_001E = Column(String)
    B09002_002E = Column(String)
    B09002_003E = Column(String)
    B09002_004E = Column(String)
    B09002_005E = Column(String)
    B09002_006E = Column(String)
    B09002_007E = Column(String)
    B09002_008E = Column(String)
    B09002_009E = Column(String)
    B09002_010E = Column(String)
    B09002_011E = Column(String)
    B09002_012E = Column(String)
    B09002_013E = Column(String)
    B09002_014E = Column(String)
    B09002_015E = Column(String)
    B09002_016E = Column(String)
    B09002_017E = Column(String)
    B09002_018E = Column(String)
    B09002_019E = Column(String)
    B09002_020E = Column(String)
    B15003_001E = Column(String)
    B15003_002E = Column(String)
    B15003_003E = Column(String)
    B15003_004E = Column(String)
    B15003_005E = Column(String)
    B15003_006E = Column(String)
    B15003_007E = Column(String)
    B15003_008E = Column(String)
    B15003_009E = Column(String)
    B15003_010E = Column(String)
    B15003_011E = Column(String)
    B15003_012E = Column(String)
    B15003_013E = Column(String)
    B15003_014E = Column(String)
    B15003_015E = Column(String)
    B15003_016E = Column(String)
    B15003_017E = Column(String)
    B15003_018E = Column(String)
    B15003_019E = Column(String)
    B15003_020E = Column(String)
    B15003_021E = Column(String)
    B15003_022E = Column(String)
    B15003_023E = Column(String)
    B15003_024E = Column(String)
    B15003_025E = Column(String)
    B16002_001E = Column(String)
    B16002_002E = Column(String)
    B16002_003E = Column(String)
    B16002_004E = Column(String)
    B16002_005E = Column(String)
    B16002_006E = Column(String)
    B16002_007E = Column(String)
    B16002_008E = Column(String)
    B16002_009E = Column(String)
    B16002_010E = Column(String)
    B16002_011E = Column(String)
    B16002_012E = Column(String)
    B16002_013E = Column(String)
    B16002_014E = Column(String)
    B19083_001E = Column(String)
    B23025_001E = Column(String)
    B23025_002E = Column(String)
    B23025_003E = Column(String)
    B23025_004E = Column(String)
    B23025_005E = Column(String)
    B23025_006E = Column(String)
    B23025_007E = Column(String)
    B27010_001E = Column(String)
    B27010_002E = Column(String)
    B27010_003E = Column(String)
    B27010_004E = Column(String)
    B27010_005E = Column(String)
    B27010_006E = Column(String)
    B27010_007E = Column(String)
    B27010_008E = Column(String)
    B27010_009E = Column(String)
    B27010_010E = Column(String)
    B27010_011E = Column(String)
    B27010_012E = Column(String)
    B27010_013E = Column(String)
    B27010_014E = Column(String)
    B27010_015E = Column(String)
    B27010_016E = Column(String)
    B27010_017E = Column(String)
    B27010_018E = Column(String)
    B27010_019E = Column(String)
    B27010_020E = Column(String)
    B27010_021E = Column(String)
    B27010_022E = Column(String)
    B27010_023E = Column(String)
    B27010_024E = Column(String)
    B27010_025E = Column(String)
    B27010_026E = Column(String)
    B27010_027E = Column(String)
    B27010_028E = Column(String)
    B27010_029E = Column(String)
    B27010_030E = Column(String)
    B27010_031E = Column(String)
    B27010_032E = Column(String)
    B27010_033E = Column(String)
    B27010_034E = Column(String)
    B27010_035E = Column(String)
    B27010_036E = Column(String)
    B27010_037E = Column(String)
    B27010_038E = Column(String)
    B27010_039E = Column(String)
    B27010_040E = Column(String)
    B27010_041E = Column(String)
    B27010_042E = Column(String)
    B27010_043E = Column(String)
    B27010_044E = Column(String)
    B27010_045E = Column(String)
    B27010_046E = Column(String)
    B27010_047E = Column(String)
    B27010_048E = Column(String)
    B27010_049E = Column(String)
    B27010_050E = Column(String)
    B27010_051E = Column(String)
    B27010_052E = Column(String)
    B27010_053E = Column(String)
    B27010_054E = Column(String)
    B27010_055E = Column(String)
    B27010_056E = Column(String)
    B27010_057E = Column(String)
    B27010_058E = Column(String)
    B27010_059E = Column(String)
    B27010_060E = Column(String)
    B27010_061E = Column(String)
    B27010_062E = Column(String)
    B27010_063E = Column(String)
    B27010_064E = Column(String)
    B27010_065E = Column(String)
    B27010_066E = Column(String)
    C15010_001E = Column(String)
    C15010_002E = Column(String)
    C15010_003E = Column(String)
    C15010_004E = Column(String)
    C15010_005E = Column(String)
    C15010_006E = Column(String)
    C17002_001E = Column(String)
    C17002_002E = Column(String)
    C17002_003E = Column(String)
    C17002_004E = Column(String)
    C17002_005E = Column(String)
    C17002_006E = Column(String)
    C17002_007E = Column(String)
    C17002_008E = Column(String)

Base.metadata.create_all(engine)