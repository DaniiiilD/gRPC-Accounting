from src.orm.database import Base
from sqlalchemy import Column, Integer, Numeric

class TariffRule(Base):
    __tablename__ = 'tariff_rules'
    
    id = Column(Integer, index=True, primary_key=True)
    min_days = Column(Integer, nullable=False)
    max_days = Column(Integer, nullable=True)
    price_per_day = Column(Numeric(10, 2), nullable= False)