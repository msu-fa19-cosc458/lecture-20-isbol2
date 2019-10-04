import unittest
import functions

class ChatBotResponseTest(unittest.TestCase):
    def test_not_command(self):
        response = functions.get_chatbot_response("Purple")
        self.assertEqual(response, "")
    
    def test_add_command(self):
        add_command = functions.get_chatbot_response('!! add 2 2')
        self.assertEqual(add_command, 4)
    
    def test_divide_command(self):
        div = functions.get_chatbot_response('!! divide 6 3')
        self.assertEqual(div, 2)


if __name__ == '__main__':
    unittest.main()