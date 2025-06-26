from helpers import get_credentials
import requests

def hf_inference(prompt, model_id, temperature, max_new_tokens):

    hf_token, _ = get_credentials.get_hf_credentials()

    API_URL = "https://router.huggingface.co/together/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {hf_token}",
    }

    response = requests.post(
        API_URL,
        headers=headers, 
        json={
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        },
                    ]
                }
            ],
            "model": model_id,
            'temperature': temperature,
            'max_new_tokens': max_new_tokens,
        }
    )
    
    return response.json()["choices"][0]["message"]

def replicate_inference(prompt, model_id, temperature, max_new_tokens):

    repl_token = get_credentials.get_replicate_credentials()

    API_URL = f"https://api.replicate.com/v1/models/{model_id}/predictions"
    headers = {
        "Authorization": f"Bearer {repl_token}",
        "Content-Type": "application/json",
        "Prefer": "wait"
    }

    response = requests.post(
        API_URL,
        headers=headers, 
        json={
            "input": {
                "prompt": prompt,
                "temperature": temperature,
                "max_tokens": max_new_tokens,
            }
        }
    )

    return {
        "content": "".join(response.json()['output'])
    }

INFERENCE_HANDLER = {
    'huggingface': hf_inference,
    'replicate': replicate_inference
}