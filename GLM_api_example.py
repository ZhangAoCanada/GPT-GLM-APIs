import zhipuai
import asyncio
import collections

zhipuai.api_key = "f4b9cf06347238b0945d6b57ef3a11b7.5SrQTPT92DloJvMU"

response = zhipuai.model_api.sse_invoke(
    model="chatglm_turbo",
    prompt=[
        {"role": "user", "content": "你好"},
        {"role": "assistant", "content": "我是人工智能助手"},
        {"role": "user", "content": "你叫什么名字"},
        {"role": "assistant", "content": "我叫chatGLM"},
        {"role":"user", "content": "你都可以做些什么事"},
    ],
    temperature=0.95,
    top_p=0.7,
    incremental=True
)


for event in response.events():
    if event.event == "add":
        print(event.data)
    elif event.event == "error" or event.event == "interrupted":
        print(event.data)
    elif event.event == "finish":
        print(event.data)
        print(event.meta)
    else:
        print(event.data)


# class AsyncGenerator:
#     def __init__(self, response):
#         self.response = response
#         self.queue = collections.deque()

#     def __aiter__(self):
#         return self

#     async def __anext__(self):
#         if not self.queue:
#             await self.fetch_even()
#             if not self.queue:
#                 raise StopAsyncIteration
#         return self.queue.popleft()
    
#     async def fetch_even(self):
#         for event in self.response.events():
#             self.queue.append(event.data)
#             if event.event == "finish":
#                 break


# async def main():
#     answer = ""
#     async for data in AsyncGenerator(response):
#         answer += data
#         print(answer)

# asyncio.run(main())

