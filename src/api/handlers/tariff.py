from fastapi import Depends, HTTPException
from src.orm.repositories.tariff import TariffRepository
from src.schemas.request.tariff import TariffCreateRequest, TariffUpdateRequest
from src.schemas.response.tariff import TariffResponse, TotalPriceResponse
from src.orm.models.tariff import TariffRule


class TariffService:
    def __init__ (self,
                  tariff_repo: TariffRepository = Depends()):
        self.tariff_repo = tariff_repo
        
    async def create_tariff(self, data: TariffCreateRequest) -> TariffRule:
        tariff_data = data.model_dump()
        new_tariff = TariffRule(**tariff_data)
        return await self.tariff_repo.create(new_tariff)
        
    async def get_all(self) -> list[TariffRule]:
        return await self.tariff_repo.get_all()
    
    async def get_by_id(self, tariff_id: int):
        tariff = await self.tariff_repo.get_by_id(tariff_id)
        if not tariff:
            raise HTTPException(status_code=404, detail="Тариф не найден")
        return tariff
        
    async def update_tariff(self, tariff_id: int, data: TariffUpdateRequest):
        update_data = data.model_dump(exclude_unset=True)
        tariff = await self.tariff_repo.update(tariff_id, update_data)
        if not tariff:
            raise HTTPException(status_code=404, detail = "Тариф не найден")
        return tariff
    
    async def delete_tariff(self, tariff_id: int) -> None:
        await self.tariff_repo.delete(tariff_id)
        
    async def calculate_total_price(self, days: int) -> TotalPriceResponse:
        tariff = await self.tariff_repo.get_tariff_for_days(days)
        if not tariff:
            raise HTTPException(status_code=404, detail="Для такого количества дней тариф не найден")
        return TotalPriceResponse(total_price=tariff.price_per_day * days)