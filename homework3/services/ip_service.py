import aiohttp
from dataclasses import dataclass
import os

@dataclass
class IpResponse:
    country: str
    region: str
    city: str
    zip: str
    lat: float
    lon: float
    query: str

db = os.getenv("DB", "http://ip-api.com/json")


async def fetch() -> IpResponse:
    async with aiohttp.ClientSession() as session:
        async with session.get('http://ip-api.com/json') as response:
            data: dict = await response.json()
            return IpResponse(
                country=data.get('country'),
                region=data.get('region'),
                city=data.get('city'),
                zip=data.get('zip'),
                lat=data.get('lat'),
                lon=data.get('lon'),
                query=data.get('query')
            )
