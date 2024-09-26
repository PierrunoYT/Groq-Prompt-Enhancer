import gradio as gr
from groq import Groq
import os

# Initialize Groq client
client = Groq()

def generate_text(system_prompt, user_prompt, chat_history, temperature=0.7, max_tokens=1024, top_p=1):
    messages = [{"role": "system", "content": system_prompt}]
    for human, ai in chat_history:
        messages.append({"role": "user", "content": human})
        messages.append({"role": "assistant", "content": ai})
    messages.append({"role": "user", "content": user_prompt})

    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        stream=True,
        stop=None,
    )

    generated_text = ""
    for chunk in completion:
        text_chunk = chunk.choices[0].delta.content or ""
        generated_text += text_chunk
        yield chat_history + [[user_prompt, generated_text]]

# Create Gradio interface
with gr.Blocks() as iface:
    gr.Markdown("# Groq Prompt Generation")
    gr.Markdown("Generate text using Groq's llama-3.1-70b-versatile model. You can provide both a system prompt and a user prompt.")
    
    with gr.Row():
        with gr.Column(scale=2):
            chatbot = gr.Chatbot(label="Conversation")
            user_input = gr.Textbox(label="User Input", placeholder="Enter your message or question here...")
            system_prompt = gr.Textbox(lines=3, label="System Prompt", placeholder="Enter the system prompt here...")
        
        with gr.Column(scale=1):
            temperature = gr.Slider(minimum=0, maximum=1, step=0.1, label="Temperature", value=0.7)
            max_tokens = gr.Slider(minimum=1, maximum=4096, step=1, label="Max Tokens", value=1024)
            top_p = gr.Slider(minimum=0, maximum=1, step=0.01, label="Top P", value=1)
    
    submit_button = gr.Button("Submit")
    
    submit_button.click(
        generate_text,
        inputs=[system_prompt, user_input, chatbot, temperature, max_tokens, top_p],
        outputs=chatbot
    )

# Launch the app
iface.launch()
