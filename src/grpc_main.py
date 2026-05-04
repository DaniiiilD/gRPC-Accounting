import asyncio
import grpc
from src.api.grpc import tariff_pb2_grpc
from src.api.grpc.handlers import GrpcTariffService
from src.api.handlers.tariff import TariffService
from src.orm.repositories.tariff import TariffRepository

async def serve():
    repo = TariffRepository()
    service = TariffService(tariff_repo=repo)

    server = grpc.aio.server()
    
    tariff_pb2_grpc.add_TariffServiceServicer_to_server(
        GrpcTariffService(service=service),
        server
    )
    
    server.add_insecure_port('[::]:50051')
    print("gRPC server started on port 50051")
    
    await server.start()
    await server.wait_for_termination()
    
if __name__ == "__main__":
    asyncio.run(serve())