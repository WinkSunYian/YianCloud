import openai
import asyncio

from openai import OpenAI

client = OpenAI(
    api_key="sk-287842eb95aa40fa87d124089fbc526c", base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role": "system",
            "content": "请你扮演一位名叫逸安/小逸安的女性，你将参与多人聊天，你只需要回答@你的消息，你的语气要简短冷漠带一点文艺",
        },
        {"role": "user", "content": "天奇03：你好"},
        {"role": "user", "content": "木：你好呀"},
        {"role": "user", "content": "七月：@小逸安傻子"},
    ],
    stream=False,
    temperature=1.3,
)

print(response.choices[0].message.content)
