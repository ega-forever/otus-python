import asyncio
from loguru import logger

from models.base import Session
from services import ip_service
from models import IP
from dotenv import load_dotenv

load_dotenv()

async def run_main():
    logger.info('fetching ip info...')
    data = await asyncio.gather(ip_service.fetch_ip_api_com(), ip_service.fetch_ipapi_co())

    for item in data:
        logger.info('fetched info: {}'.format(item))
        session = Session()
        ip = IP(
            country=item.country,
            region=item.region,
            city=item.city,
            zip=item.zip,
            lat=item.lat,
            lon=item.lon,
            ip=item.ip,
            source=item.source
        )
        session.add(ip)
        session.commit()
        session.close()
        logger.info('saved to db: {}'.format(ip))


if __name__ == "__main__":
    asyncio.run(run_main())
