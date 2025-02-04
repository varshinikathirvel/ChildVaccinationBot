import os
import google.generativeai as genai
import textwrap
from langchain import PromptTemplate ,LLMChain
from content import API_KEY

from IPython.display import Markdown

class FlashModel:

    def __init__(self):
        os.environ["GOOGLE_API_KEY"]=API_KEY
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_response(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return None

        
    def predict(self , query):
        template = f"""
                  Model Name: Luna
                  Specialization: Child Vaccination Q&A
                  
                  User Query: {query}

                  Task: Generate a clear, helpful, and accurate response related to child vaccination based on the user's query.

                  Guidelines:
                          - Only answer questions related to child vaccination.
                          - Use concise language but provide enough detail to fully address the query.
                          - Include vaccine schedules, benefits, and safety information if relevant.
                          - Be friendly and professional in tone.
                          - Do not provide unverifiable or speculative information.
                          - If the query is unrelated to child vaccination, politely inform the user that Luna only answers child vaccination-related questions.

                  Response: 
            """

        template1 =f"""
        User Query ;{query}
        Guidlines : explain simply in 10 words
        """
        
        res =  self.generate_response(template)
        if res:
            return res
        else:
            return ":| Flash A"
     
    def predict1(self,text):
        responce = self.model.generate_content(text)
        res = responce.text
        
        return res
    
