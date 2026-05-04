from pydantic import BaseModel, ConfigDict

class TariffResponse(BaseModel):
    id: int
    min_days: int
    max_days: int | None
    price_per_day: int
    
    model_config = ConfigDict(from_attributes=True)
    
class TotalPriceResponse(BaseModel):
    total_price: int