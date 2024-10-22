import openai
from apps.YianBot.models import User


async def get_ai_chat(user: User, user_message: str):
    openai.api_key = "sk-B8qI0lVqWROZrWkb517b7102F9544f5bB97e84EaD3E8Bf8e"
    openai.base_url = "https://aigcbest.top/v1/"

    messages = [
        {
            "role": "system",
            "content": "你将扮演一位名叫逸安的女性，接下来我会与你聊天，你不需要太过于热情",
        }
    ]

    # 获取最新的5条对话记录
    dialogues = await user.get_dialogues(5)
    
    # 构建历史消息
    for dialogue in dialogues:
        messages.append({"role": "user", "content": dialogue.content})
        messages.append({"role": "assistant", "content": dialogue.content})

    # 添加当前用户消息
    messages.append({"role": "user", "content": user_message})

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125", messages=messages
    )
    # 保存对话记录
    await user.add_dialogue("user", user_message)
    await user.add_dialogue("assistant", response.choices[0].message.content)
    return response.choices[0].message.content
