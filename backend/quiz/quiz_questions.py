from typing import Dict, List
import aiohttp


async def get_questions(questions_num: int) -> List[Dict[str, any]] | None:
    url = f"https://jservice.io/api/random?count={questions_num}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Ошибка при запросе: {response.status}")
                return
