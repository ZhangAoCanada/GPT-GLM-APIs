import zhipuai

zhipuai.api_key = "f4b9cf06347238b0945d6b57ef3a11b7.5SrQTPT92DloJvMU"

response = zhipuai.model_api.async_invoke(
    model="chatglm_turbo",
    prompt=[
        {"role": "user", "content": "你好"},
        {"role": "assistant", "content": "我是人工智能助手"},
        {"role": "user", "content": "你叫什么名字"},
        {"role": "assistant", "content": "我叫chatGLM"},
        {"role":"user", "content":"你都可以做些什么事"},
    ]
)

response = zhipuai.model_api.query_async_invoke_result("70217042412551178252651738010520012")

print(response)


