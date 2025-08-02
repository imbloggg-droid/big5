
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_big_five(interview_text, player_name="Unknown"):
    prompt = open("prompt.txt", "r").read()
    full_prompt = prompt.replace("{{interview}}", interview_text).replace("{{player}}", player_name)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a sports psychologist evaluating football players using the Big Five personality model."},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.7
    )

    try:
        return eval(response["choices"][0]["message"]["content"])
    except Exception:
        return {"error": "Model returned invalid format."}
