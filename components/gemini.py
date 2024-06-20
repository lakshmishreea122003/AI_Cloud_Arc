import google.generativeai as genai
import os

class Gen_ai:

    def __init__(self,prompt):
        self.prompt = prompt

    def advice_arc(self):
        pr1 = f'for the give cloud architecture requirements {self.prompt} suggest aws cloud architecture. It should be cost efficient and best suited for the requirements. Also provide estimated cost.'
        genai.configure(api_key=os.environ.get('gemini_api'))
        model = genai.GenerativeModel('gemini-1.5-flash')
        res_arc = model.generate_context(pr1).text
        return res_arc
    
    def simplify_arc(self):
        res_arc = self.advice_arc()
        pr2 = f'For the given cloud architecture {res_arc}, give a simplified details of this architecture.  Here mention names of each of the instances in standard short forms mention how many of these instances and also how each instance is connected to others. Also give 2-3 words about each of the instance.'
        genai.configure(api_key=os.environ.get('gemini_api'))
        model = genai.GenerativeModel('gemini-1.5-flash')
        simplified_arc = model.generate_context(pr2).text
        simplified_arc = "Give d2lang code for the given cloud architecture. " + simplified_arc
        return res_arc, simplified_arc

        


