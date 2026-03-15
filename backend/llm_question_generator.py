import json
from deepseek_client import get_deepseek_client
from taxonomy import get_allowed_labels, FALLBACK_LABEL


def generate_ai_question(concept: str, difficulty: str, question_type: str) -> dict:
    client = get_deepseek_client()

    allowed_labels = get_allowed_labels(concept)

    system_prompt = (
        "You are an educational assistant for Grade 10 programming teachers. "
        "Generate one short diagnostic programming question. "
        "Return valid JSON only."
    )

    user_prompt = f"""
Generate one Grade 10 programming diagnostic question.

Concept: {concept}
Difficulty: {difficulty}
Question type: {question_type}

Allowed target misconception labels:
{allowed_labels}

Return JSON with exactly these keys:
- prompt (string)
- code_snippet (string)
- correct_answer (string)
- target_misconception (string)

Rules:
- target_misconception must be one of the allowed labels exactly
- keep the question short and classroom-friendly
- make the code snippet simple and realistic for Grade 10
- correct_answer should be concise but accurate
"""

    response = client.chat.completions.create(
        model="deepseek-chat",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        max_tokens=500,
    )

    parsed = json.loads(response.choices[0].message.content)

    target_misconception = parsed.get("target_misconception", FALLBACK_LABEL)
    if target_misconception not in allowed_labels:
        target_misconception = FALLBACK_LABEL

    return {
        "prompt": parsed.get("prompt", "What will this code print?"),
        "code_snippet": parsed.get("code_snippet", ""),
        "correct_answer": parsed.get("correct_answer", ""),
        "target_misconception": target_misconception,
    }