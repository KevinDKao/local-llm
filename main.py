import requests
import json

def get_phi_response(prompt, api_url="http://localhost:11434/api/generate"):
    """
    Send a prompt to locally running Phi model via Ollama and return the response
    
    Args:
        prompt (str): The input prompt to send to Phi
        api_url (str): The Ollama API endpoint (default is localhost:11434)
        
    Returns:
        str: The complete response from Phi
    """
    # Prepare the request payload
    payload = {
        "model": "phi",
        "prompt": prompt,
        "stream": False
    }
    
    try:
        # Send POST request to Ollama API
        response = requests.post(api_url, json=payload)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Parse and return the response
        result = response.json()
        return result.get('response', '')
        
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Ollama: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    prompt = "How old am i?"
    response = get_phi_response(prompt)
    if response:
        print(f"Prompt: {prompt}\nResponse: {response}")