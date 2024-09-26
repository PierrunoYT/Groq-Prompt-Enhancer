# Groq Text Generation with Gradio Interface

This project provides a user-friendly web interface for generating text using Groq's llama-3.1-70b-versatile model. It utilizes the Gradio library to create an interactive UI where users can input prompts and adjust various parameters to control the text generation process.

## Features

- Interactive chat interface
- System prompt input for setting context
- User input for specific queries or prompts
- Adjustable parameters:
  - Temperature
  - Max Tokens
  - Top K
  - Top P
- Real-time streaming of generated text

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- Groq API key (set as an environment variable)

## Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # OR
   source venv/bin/activate  # On macOS and Linux
   ```

3. Install the required dependencies:
   ```
   pip install gradio groq
   ```

4. Set up your Groq API key as an environment variable:
   ```
   set GROQ_API_KEY=your_api_key_here  # On Windows
   # OR
   export GROQ_API_KEY=your_api_key_here  # On macOS and Linux
   ```

## Usage

To run the application, execute the following command in your terminal:

```
python gradio_groq_app.py
```

This will start the Gradio server, and you should see output indicating the local URL where you can access the interface (typically http://127.0.0.1:7860).

In the web interface:

1. Enter a system prompt to set the context for the AI (optional).
2. Type your specific query or prompt in the "User Input" field.
3. Adjust the sliders for Temperature, Max Tokens, Top K, and Top P as desired.
4. Click the "Submit" button to generate text.
5. The generated response will appear in the chat interface.

## Contributing

Contributions to this project are welcome. Please feel free to submit a Pull Request.

## License

[Specify your license here]

## Acknowledgements

- This project uses the [Groq API](https://www.groq.com/) for text generation.
- The web interface is built with [Gradio](https://www.gradio.app/).
