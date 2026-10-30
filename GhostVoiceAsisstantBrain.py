import ollama

class AssistantBrain:
    def __init__(self, model_name="Astrea"):
        self.model_name = model_name

        self.system_prompt = {
            "role" : "system",
            "content": "You are a helpful, concise, and friendly voice activated virtual assistant. Keep your ansswers breif and natural, as they will be spoken out loud."
        }

        self.conversation_history = [self.system_prompt]

    def think(self, user_input: str) -> str:
        """Takes text from the listener, processes it with Ollama, and returns the respond."""

        self.conversation_history.append({"role": "user", "content": user_input})

        try:

            response = ollama.chat(
                model=self.model_name,
                messages=self.
conversation_history
            )

            assistant_response = response[
'message']['content']

            self.conversation_history= [self.system_prompt] + self.conversation_history[-10:]

            return assistant_response
            
        except Exception as e:
            return f"Sorry, I had trouble finding the answer to that. Please try again. Error: {e}"

    if __name__ == "__main__":
        brain = AssistantBrain(model_name= "Astraea")

        mock_listen_input = """
    "Astraea, What is the capital of France?"
        Print(f"User said: {mock_listen_input}")"""

        Reply = brain.think(mock_listen_input)
        print(f"Astraea replied: {Reply}")