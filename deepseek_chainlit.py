import chainlit as cl 
import ollama 
import json 

@cl.on_message 
async def main(message: cl.Message):
    # Create a message dictionary instead of using Message objects directly 
    messages = [{'role': 'user', "content": str(message.content)}]
    
    # Create a message first 
    msg = cl.Message(content="")
    await msg.send()
    
    # create a stream with ollama
    stream = ollama.chat(
       model='deepseek-r1:1.5b',
       messages= messages,
       stream= True
    )
    
    # STREAM THE RESPONSE TOKEN BY TOKEN 
    for chunk in stream:
        if token := chunk['message']['content']:
            await msg.stream_token(token)
        
    # Update msg final time
    await msg.update()

@cl.on_chat_start
async def start():
    await  cl.Message(content="Hello, AI Anytime! How can I help you today?").send()