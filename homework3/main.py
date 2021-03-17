import asyncio
from loguru import logger

from models.base import Session
from services import ip_service
from models import IP
from dotenv import load_dotenv

load_dotenv()

async def run_main():
    logger.info('fetching ip info...')
    data = await ip_service.fetch()
    logger.info('fetched info: {}'.format(data))

    session = Session()
    ip = IP(
        country=data.country,
        region=data.region,
        city=data.city,
        zip=data.zip,
        lat=data.lat,
        lon=data.lon,
        ip=data.query
    )
    session.add(ip)
    session.commit()
    session.close()
    logger.info('saved to db: {}'.format(ip))


if __name__ == "__main__":
    asyncio.run(run_main())
