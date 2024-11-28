import unittest
from unittest.mock import patch, MagicMock
from src.chatgpt_client import AskGpt

class TestAskGpt(unittest.TestCase):
    
    def setUp(self):
        # Reset the messages list before each test
        AskGpt.messages = []
    
    @patch('src.chatgpt_client.client.chat.completions.create')
    def test_ask_gpt(self, mock_create):
        # Arrange: Setup mock response from OpenAI
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content="It is sunny in Anand, Gujarat."))]
        mock_create.return_value = mock_response
        
        # Act: Call the method with a test prompt
        user_prompt = "What is the weather today like in Anand, Gujarat? Respond with maximum 20 words."
        response = AskGpt.ask_gpt(user_prompt)
        
        # Assert: Verify that the method returns the correct response
        self.assertEqual(response, "It is sunny in Anand, Gujarat.")
        self.assertEqual(len(AskGpt.messages), 2)  # Ensure messages are appended correctly
        self.assertEqual(AskGpt.messages[0]["role"], "user")
        self.assertEqual(AskGpt.messages[1]["role"], "assistant")

if __name__ == '__main__':
    unittest.main()