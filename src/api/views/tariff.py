from fastapi import APIRouter, Depends
from src.api.handlers.tariff import TariffService
from src.api.middlewares.session import in_session
from src.schemas.request.tariff import TariffCreateRequest, TariffUpdateRequest
from src.schemas.response.tariff import TariffResponse, TotalPriceResponse

tariff_router = APIRouter(prefix='/tariffs', tags=['Тарифы'])

@tariff_router.post("/", response_model = TariffResponse)
@in_session
async def create_tariff(
    data: TariffCreateRequest,
    service: TariffService = Depends()
):
    return await service.create_tariff(data)

@tariff_router.get('/calculate', response_model= TotalPriceResponse)
@in_session
async def calculate_price(
    days: int,
    service: TariffService = Depends()
):
    return await service.calculate_total_price(days)

@tariff_router.get('/all', response_model = list[TariffResponse])
@in_session
async def get_all_tariffs(
    service: TariffService = Depends()
):
    return await service.get_all()

@tariff_router.get("/{tariff_id}", response_model = TariffResponse)
@in_session
async def get_tariff_by_id(
    tariff_id: int,
    service: TariffService = Depends()
):
    return await service.get_by_id(tariff_id)

@tariff_router.patch("/{tariff_id}", response_model= TariffResponse)
@in_session
async def update_tariff(
    tariff_id: int,
    data: TariffUpdateRequest,
    service: TariffService = Depends()
):
    return await service.update_tariff(tariff_id, data)

@tariff_router.delete('/{tariff_id}')
@in_session
async def delete_tariff(
    tariff_id: int,
    servcie: TariffService = Depends()
):
    await servcie.delete_tariff(tariff_id)
    return {'status': 'deleted'}