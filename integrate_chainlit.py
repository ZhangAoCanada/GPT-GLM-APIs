import chainlit as cl
import zhipuai

zhipuai.api_key = "f4b9cf06347238b0945d6b57ef3a11b7.5SrQTPT92DloJvMU"

prompt = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "我是人工智能助手"},
    {"role": "user", "content": "你叫什么名字"},
    {"role": "assistant", "content": "我叫chatGLM"},
]


@cl.step
def tool():
    return "Response from the tool!"


@cl.on_message  # this function will be called every time a user inputs a message in the UI
async def main(message: cl.Message):
    """
    This function is called every time a user inputs a message in the UI.
    It sends back an intermediate response from the tool, followed by the final answer.

    Args:
        message: The user's message.

    Returns:
        None.
    """

    # # Call the tool
    # tool()

    # format the input message into prompt
    prompt.append({"role": "user", "content": message.content})

    # get response from the model
    response = zhipuai.model_api.invoke(
        model="chatglm_turbo",
        prompt=prompt,
        top_p=0.9,
        temperature=0.9,
    )

    # get answer from the response
    answer = response['data']['choices'][0]['content']

    # add the response to the prompt
    prompt.append({"role": "assistant", "content": answer})

    # change format of the string
    answer = answer.replace(" ", "").replace('"', '').replace("\\n", "\n").replace("\\t", "\t")

    # Send the final answer.
    await cl.Message(content=answer).send()