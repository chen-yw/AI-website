from zhipuai import ZhipuAI
import os
def Zhipu_AI_API(prompt):
    client = ZhipuAI(api_key="429f22fdba8940a6be56c2776e671c88.xaIC5iPAFCM8aO3s")  
    # client = ZhipuAI(api_key=os.getenv("ZHIPU_API_KEY"))
    print("开始询问")
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
    
    
    
    