import os
import aiohttp

from app.adapters.client.nftbank_apispec import DailyEstimatedPriceResponse


class NFTBankApiClient:
    def __init__(self, host, api_key):
        self.host = host
        self.api_key = api_key

    async def get_daily_estimated_price(self, network_id: str, asset_contract: str, token_id: str) -> DailyEstimatedPriceResponse:
        url = f'{self.host}/estimates-v2/estimates/{asset_contract}/{token_id}?chain_id={network_id}'
        headers = {"X-API-KEY": self.api_key}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as resp:
                if resp.status != 200:
                    raise Exception(f'{resp.status} {resp.reason}')

                data = await resp.text()
                return DailyEstimatedPriceResponse.parse_raw(data)


async def main():
    client = NFTBankApiClient(
        'https://api.nftbank.ai', os.environ['NFTBANK_API_KEY'])

    # when
    result = await client.get_daily_estimated_price("ethereum", "0xbce3781ae7ca1a5e050bd9c4c77369867ebc307e", "4714")
    print(result)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
