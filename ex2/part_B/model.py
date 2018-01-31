from sqlalchemy import Column, Integer, Float, Date, String, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence
from sqlalchemy import ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship, backref

Base = declarative_base()
class Exchange(Base):
    """class exchange"""
    __tablename__ = 'exchange'
    id = Column(Integer, Sequence('exchange_sequence_id'), primary_key=True)
    name = Column(String(80), nullable=False)
    code = Column(String(20), unique=True, nullable=False, index=True)
    TradingHours = Column(Integer, unique=True, nullable=False, index=True)
    pair = relationship('pair',backref=backref("exchange", uselist=False))
    def __init__(self, name, code, TradingHours):
        self.name = name
        self.code = code
        self.TradingHours = TradingHours
    def __repr__(self):
        return "Exchange(name={self.name}, code={self.code},TradingHours={self.TradingHours})".format(self=self)
class Pair(Base):
    """class pair"""
    __tablename__ = 'pair'
    id = Column(Integer, Sequence('pair_sequence_id'), primary_key=True)
    code = Column(String(20), unique=True, nullable=False, index=True)
    coin = relationship('coin', single_parent=True)
    def __init__(self,code):
        self.code = code
    def __repr__(self):
        return "Pair(code={self.code})".format(self=self)
class Coin(Base):
    """class coin"""
    __tablename__ = 'coin'
    basecoin = Column(String(20), unique=True, nullable=False, index=True)
    crosscoin = Column(String(20), unique=True, nullable=False, index=True) 
class Tickdata_b(Base):
    """bid price ask"""
    __tablename__ = 'price'
    date = Column(Date, primary_key=True)
    last = Column(Float, nullable=False)
    bid =  Column(Float, nullable=False)
    ask =  Column(Float, nullable=False)
    pair = relationship('pair' , single_parent =True)
    def __init__(self,last,bid,ask):
        self.last = last
        self.bid = bid
        self.ask = ask
    def __repr__(Self):
        return "Tickdata_a(last={self.last}, bid={self.bid}, ask={self.ask} )".format(self.self)
class Tickdata_a(Base):
    """bid price ask"""
    __tablename__ = 'price'
    date = Column(Date, primary_key=True)
    last = Column(Float, nullable=False)
    bid =  Column(Float, nullable=False)
    ask =  Column(Float, nullable=False)
    pair = relationship('pair' , single_parent =True)
    def __init__(self,last,bid,ask):
        self.last = last
        self.bid = bid
        self.ask = ask
    def __repr__(Self):
        return "Tickdata_a(last={self.last}, bid={self.bid}, ask={self.ask})".format(self.self)
