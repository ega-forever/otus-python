import aiohttp
from dataclasses import dataclass

ip_types = {
    "ip_api_com": 1,
    "ipapi_co": 2
}

@dataclass
class IpResponse:
    country: str
    region: str
    city: str
    zip: str
    lat: float
    lon: float
    ip: str
    source: int

async def fetch_ip_api_com() -> IpResponse:
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
                ip=data.get('query'),
                source=ip_types.get("ip_api_com")
            )

async def fetch_ipapi_co() -> IpResponse:
    async with aiohttp.ClientSession() as session:
        async with session.get('https://ipapi.co/json') as response:
            data: dict = await response.json()
            return IpResponse(
                country=data.get('country'),
                region=data.get('region'),
                city=data.get('city'),
                zip=data.get('zip'),
                lat=data.get('latitude'),
                lon=data.get('longitude'),
                ip=data.get('ip'),
                source=ip_types.get("ipapi_co")
            )
