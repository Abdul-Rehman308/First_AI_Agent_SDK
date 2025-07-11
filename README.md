# Website Developer AI Agent

This project is an AI Agent built using the Gemini API (Google Generative Language) and OpenAI SDK. The agent is designed to assist developers with website development tasks and can be easily configured for your own use.

## Features

- Gemini API integration
- Customizable agent instructions
- Easy configuration via `.env` file
- Developer-friendly and extendable code

## Requirements

- Python 3.8 or higher
- Install dependencies:  
  ```
  pip install -r requirements.txt
  ```
- Gemini API key (add to `.env` file)

## Usage

Run the agent using:

```bash
uv run main.py
```

## Configuration

Add your Gemini API key to a `.env` file in the project root:

## OpenRouter Integration

This project uses [OpenRouter](https://openrouter.ai/) as the API gateway for accessing various AI models.

**How to use:**
- Get your OpenRouter API key from [OpenRouter Dashboard](https://openrouter.ai/).
- Add it to your `.env` file like this:
  ```
  OPENROUTER_API_KEY=your_openrouter_api_key_here
  ```
- The agent is configured to connect to OpenRouter’s API endpoint and can use any supported model available on OpenRouter.

**Example model in use:**  
`deepseek/deepseek-r1-0528-qwen3-8b:free`

## Developer
**Syed AR**

---

Feel free to open an issue or pull request for improvements or questions.