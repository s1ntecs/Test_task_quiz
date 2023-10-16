from typing import List, Dict, Tuple

import httpx


async def get_questions_data(count: int) -> Tuple[List[Dict], int]:
    async with httpx.AsyncClient() as client:
        url = f"https://jservice.io/api/random?count={count}"
        response = await client.get(url)
        data = response.json()
    return data, response.status_code
