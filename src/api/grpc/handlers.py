import grpc
from src.api.grpc import tariff_pb2, tariff_pb2_grpc
from src.api.handlers.tariff import TariffService
from src.orm.database import async_session_factory
from src.orm.repositories.tariff import TariffRepository

class GrpcTariffService(tariff_pb2_grpc.TariffServiceServicer):
    
    def __init__(self, service: TariffService):
        self.service = service
        
    async def CalculatePrice(self, request, context):
        days = request.days
        
        try:
            async with async_session_factory() as session: 
                repo = TariffRepository()
                tariff = await repo.get_tariff_for_days(days)
                if not tariff:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    context.set_details("Tariff not found")
                    return tariff_pb2.GetDailyPriceResponse()
                   
                total = tariff.price_per_day * days
                
                return tariff_pb2.GetDailyPriceResponse(
                    price_per_day=int(tariff.price_per_day),
                    total_price= int(total)
                )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Server error: {str(e)}')
            return tariff_pb2.GetDailyPriceResponse()