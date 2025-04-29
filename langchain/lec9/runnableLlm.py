import random

class NakliLLm:
    def __init__(self):
        print("LLM created")

    def predict(self,prompt):
        responselist = [
            'response 1',
            'response 2',
            'response 3'
        ]

        return {"response": random.choice(responselist)}
    
class NakliPrompt:
    def __init__(self,template,input_variable):
        self.template = template
        self.input_variables = input_variable

    def format(self,input_dict):
        return self.template.format(**input_dict)
    

    
if __name__=="__main__":
    obj = NakliPrompt(
        template="Write a {length} poem about {topic}",
        input_variable=['topic','length']
    )
    prompt = obj.format({'length':'long','topic':'India'})
    llm = NakliLLm()
    print(llm.predict(prompt))