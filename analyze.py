from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_big_five(interview_text, player_name="Unknown"):
    try:
        with open("prompt.txt", "r") as f:
            prompt_template = f.read()

        full_prompt = prompt_template.replace("{{interview}}", interview_text).replace("{{player}}", player_name)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a sports psychologist evaluating football players using the Big Five personality model."
                },
                {
                    "role": "user",
                    "content": full_prompt
                }
            ],
            temperature=0.7
        )

        content = response.choices[0].message.content.strip()
        return eval(content)  # ⚠️ Только если полностью доверяешь результату

    except Exception as e:
        return {"error": str(e)}
