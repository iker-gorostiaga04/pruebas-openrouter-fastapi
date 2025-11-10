import os
import requests
from dotenv import load_dotenv

load_dotenv()  # carga el .env automáticamente


class OpenRouterClient:
    """
    	Versión inicial: solo maneja el modelo LLM gratuito (Gemini)
    """

    #CONTRUCTOR
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("No se encontró la clave API. Define OPENROUTER_API_KEY en tu archivo .env")

	#openrouter
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

 #Funciones

  #func priv
    def _make_request(self, model: str, messages: list) -> dict:
        """
          Método privado reutilizable para todos los publicos 
        """
        payload = {"model": model, "messages": messages}
        response = requests.post(self.base_url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()


  #func public
    def chat_llm(self, prompt: str) -> str:
        """
          Llamada al modelo Gemini gratuito (LLM normal)
        """
        model = "deepseek/deepseek-chat-v3-0324:free"
        messages = [{"role": "user", "content": prompt}]
        response = self._make_request(model, messages)
        return response["choices"][0]["message"]["content"]
