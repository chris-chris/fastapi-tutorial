from datetime import datetime
from typing import Optional, Iterator, List

from pydantic import BaseModel, Field
from humps import camel


class DailyEstimatedPriceItemPrice(BaseModel):
    currency_symbol: str
    estimate_price: float

    class Config:
        alias_generator = camel.case
        allow_population_by_field_name = True


class DailyEstimatedPriceItem(BaseModel):
    id: str = Field(alias='_id')
    asset_contract: str
    chain_id: str
    estimate: List[DailyEstimatedPriceItemPrice]
    estimated_at: str
    item_id: str
    token_id: str

    class Config:
        alias_generator = camel.case
        allow_population_by_field_name = True


class DailyEstimatedPriceResponse(BaseModel):
    data: List[DailyEstimatedPriceItem]
    response: int
    message: str

    class Config:
        alias_generator = camel.case
        allow_population_by_field_name = True
