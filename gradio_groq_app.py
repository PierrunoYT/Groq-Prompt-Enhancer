import gradio as gr
from groq import Groq
import os

# Initialize Groq client
client = Groq()

def generate_text(system_prompt, user_prompt, temperature=0.7, max_tokens=1024):
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        stream=True,
        stop=None,
    )

    generated_text = ""
    for chunk in completion:
        text_chunk = chunk.choices[0].delta.content or ""
        generated_text += text_chunk
        yield generated_text

# Create Gradio interface
iface = gr.Interface(
    fn=generate_text,
    inputs=[
        gr.Textbox(lines=3, label="System Prompt", placeholder="Enter the system prompt here..."),
        gr.Textbox(lines=5, label="User Input", placeholder="Enter your message or question here..."),
        gr.Slider(minimum=0, maximum=1, step=0.1, label="Temperature", value=0.7),
        gr.Slider(minimum=1, maximum=2048, step=1, label="Max Tokens", value=1024),
    ],
    outputs=gr.Textbox(lines=10, label="Generated Text"),
    title="Groq Text Generation",
    description="Generate text using Groq's llama-3.1-70b-versatile model. You can provide both a system prompt and a user prompt.",
    live=True,
)

# Launch the app
iface.launch()
