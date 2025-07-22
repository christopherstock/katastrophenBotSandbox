import configparser

COLOR_OK = '\033[92m'
COLOR_DEFAULT = '\033[0m'

print("import config/config.ini", end="")
config = configparser.ConfigParser()
config.read("config/config.ini")
print(COLOR_OK + " OK" + COLOR_DEFAULT)

print("set OpenAI API key", end="")
import os
OPEN_AI_KEY = config.get("OpenAI", "OPEN_AI_KEY")
os.environ["OPENAI_API_KEY"] = OPEN_AI_KEY
print(COLOR_OK + " OK" + COLOR_DEFAULT)

print("import OpenAI libs", end="")
import openai
print(COLOR_OK + " OK" + COLOR_DEFAULT)

print("specify text generation method", end="")
def generate_text(prompt, model="gpt-4o-mini", max_tokens=10000):
    try:
        response = openai.completions.create(
            model=model,
            prompt=prompt,
            n=1,
            stop=None,
            temperature=0.7,
            max_tokens=max_tokens,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
print(COLOR_OK + " OK" + COLOR_DEFAULT)

if __name__ == "__main__":
    # Replace with your desired prompt
    my_prompt = """
        Create a Docker Compose setup for a web application with one frontend and one backend.
        The backend should be a SpringBoot application that serves a simple page with a greeting.
        The frontend should be a Node.js application with TypeScript, React and Material-UI that displays the greeting from the backend.
    """
    generated_text = generate_text(my_prompt)

    if generated_text:
        print()
        print("generated text output:")
        print()
        print(generated_text)
        print()
        print("text generation", end="")
        print(COLOR_OK + " OK" + COLOR_DEFAULT)
        print()
