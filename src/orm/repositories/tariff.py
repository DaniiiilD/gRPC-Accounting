from sqlalchemy import select, or_
from src.orm.repositories.base import BaseRepository
from src.orm.models.tariff import TariffRule

class TariffRepository(BaseRepository):
    model = TariffRule
    
    async def get_tariff_for_days(self, days_count: int) -> TariffRule | None:
        query = select(TariffRule).where(
            TariffRule.min_days <= days_count,
            or_(
            TariffRule.max_days >= days_count,
            TariffRule.max_days == None
            )
        )
        
        result = await self.session.execute(query)
        return result.scalar_one_or_none()