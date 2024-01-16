import zhipuai

zhipuai.api_key = "f4b9cf06347238b0945d6b57ef3a11b7.5SrQTPT92DloJvMU"

# 请求模型
response = zhipuai.model_api.invoke(
    model="chatglm_turbo",
    prompt=[
        {"role": "user", "content": "你好"},
        {"role": "assistant", "content": "我是人工智能助手"},
        {"role": "user", "content": "你叫什么名字"},
        {"role": "assistant", "content": "我叫chatGLM"},
        {"role":"user", "content":"你都可以做些什么事"},
    ]
)

print(response)