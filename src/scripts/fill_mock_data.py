import asyncio
import random
from src.orm.database import async_session_factory
from sqlalchemy import delete, select
from src.orm.repositories.tariff import TariffRepository
from src.orm.models.tariff import TariffRule

TIERS =[
    {"min_days": 1,  "max_days": 3,    "min_price": 6000, "max_price": 8000},
    {"min_days": 4,  "max_days": 7,    "min_price": 4500, "max_price": 6000},
    {"min_days": 8,  "max_days": 14,   "min_price": 3500, "max_price": 4500},
    {"min_days": 15, "max_days": 30,   "min_price": 2000, "max_price": 3500},
    {"min_days": 31, "max_days": None, "min_price": 500,  "max_price": 2000},
]

async def generate_mock_tariffs():
    async with async_session_factory() as session:
        try:
            repo = TariffRepository()
            
            existing = await repo.get_all()
            if existing:
                print("таблица содержит данные. Удаляем данные...")
                await session.execute(delete(TariffRule))
            
            for tier in TIERS:
                new_tarrif = TariffRule(
                    min_days = tier['min_days'],
                    max_days =  tier['max_days'],
                    price_per_day = random.randint(tier['min_price'], tier['max_price'])
                )
            
                await repo.create(new_tarrif)
            
            await session.commit()
            print("База даных успешно заполнена тестовыми тарифами!")
            
        except Exception as e:
            print(f"Произошла ошибка при заполнении: {e}")
            raise
        
if __name__ == "__main__":
    asyncio.run(generate_mock_tariffs())