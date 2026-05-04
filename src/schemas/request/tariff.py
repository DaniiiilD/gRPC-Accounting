from pydantic import BaseModel

class TariffCreateRequest(BaseModel):
    min_days: int
    max_days : int | None
    price_per_day: int
    
class TariffUpdateRequest(BaseModel):
    min_days: int | None = None
    max_days: int | None = None
    price_per_day: int | None = None
    
    
