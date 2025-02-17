from zhipuai import ZhipuAI
from openai import OpenAI
import os

def Zhipu_AI_API(prompt):
    client = ZhipuAI(api_key=os.getenv("ZHIPU_API_KEY"))
    # print("开始询问")
    response = client.chat.completions.create(
        model="glm-4-plus",  # 请填写您要调用的模型名称
        messages=[
            {"role": "user", "content": "作为一名风水大师，请帮助我根据用户的出生时间以及当前的阳历时间，预测用户这一天的运势。"},
            {"role": "assistant", "content": "好的，请给我更多的信息"},
            {"role": "user", "content": prompt},
        ],
    )
    message_content = response.choices[0].message.content
    print(message_content)
    return str(message_content)
    
def Doubao_AI_API(prompt):
    client = OpenAI(
        # 从环境变量中读取您的方舟API Key
        api_key=os.environ.get("ARK_API_KEY"), 
        base_url="https://ark.cn-beijing.volces.com/api/v3",
        )
    response = client.chat.completions.create(
        # 替换 <YOUR_ENDPOINT_ID> 为您的方舟推理接入点 ID
        model="ep-20250217102136-wb8dc",
        # model = os.getenv("ARK_endpoint"),
        messages=[
            {"role": "user", "content": "作为一名风水大师，请帮助我根据用户的出生时间以及当前的阳历时间，预测用户这一天的运势。"},
            {"role": "assistant", "content": "好的，请给我更多的信息"},
            {"role": "user", "content": prompt},
        ]
    )
    message_content = response.choices[0].message.content
    print(message_content)
    return str(message_content)
    
def Kimi_AI_API(prompt):
    client = OpenAI(
        api_key = "sk-UMFLgh3REAEbsli8dddZqmufG4V33waBbGkbgkOnHDxEzjfn",
        # api_key = os.getenv("KIMI_API_KEY"),
        base_url = "https://api.moonshot.cn/v1",
    )
    
    response = client.chat.completions.create(
        model = "moonshot-v1-8k",
        messages = [
            {"role": "user", "content": "作为一名风水大师，请帮助我根据用户的出生时间以及当前的阳历时间，预测用户这一天的运势。"},
            {"role": "assistant", "content": "好的，请给我更多的信息"},
            {"role": "user", "content": prompt},
        ],
        temperature = 0.3,
    )
    message_content = response.choices[0].message.content
    print(message_content)
    return str(message_content)