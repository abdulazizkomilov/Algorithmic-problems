import asyncio
import httpx
import openai

openai.api_key = "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"



async def main():
    max_retries = 3
    timeout_duration = 30.0  # Adjust the timeout value as needed

    for attempt in range(max_retries):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "https://api.openai.com/v1/chat/completions",
                    headers={"Content-Type": "application/json",
                             "Authorization": f"Bearer {openai.api_key}"},
                    json={
                        "model": "gpt-3.5-turbo-1106",
                        "messages": [
                            {"role": "system",
                                "content": "You are a helpful assistant."},
                            {"role": "user",
                                "content": "aiogram orqali telegram bot qilib ber va misollar bilan tushuntir"}
                        ]
                    },
                    timeout=httpx.Timeout(timeout_duration)
                )
                yield response
        except httpx.ReadTimeout:
            if attempt == max_retries - 1:
                raise  # Raise the exception if max retries reached
            print(f"Request timed out. Retrying... (Attempt {attempt + 1})")
            
asyncio.run(main())


