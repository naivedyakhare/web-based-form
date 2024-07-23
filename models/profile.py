class Profile:
    def __init__(self):
        pass
        
    def set_profile(self, email, name, gender, exists):

        self.email = email
        self.name = name
        self.gender = gender

        self.exists = exists


    def set_qna(self, qna):
        if qna != {}:
            
            self.questions = {}
            self.answers = {}

            for num, pair in qna.items():
                self.questions[num] = pair['q']
                self.answers[num] = pair['a']


    def get_profile(self):
        data = {
            "profile": {
                "name": self.name,
                "email": self.email,
                "gender": self.gender
            }
        }

        return data
    
    def get_qna(self):
        
        data = {}
        for num in self.questions.keys():
            data[f"{num}"] = {self.questions[num], self.answers[num]}

        return {"QnA": data}
    
    def get_complete(self):
        return {"data": {**self.get_profile(),**self.get_qna()}}
        

if __name__ == "__main__":
    qna = {
        "1": {
            "q": "question1",
            "a": "answer1"
        },

        "2": {
            "q": "question2",
            "a": "answer2"
        },

        "3": {
            "q": "question3",
            "a": "answer3"
        }
    }
    user = Profile(email="@", name="a", gender="M", qna=qna, exists=True)
    print(user.questions)
    print(user.answers)
    print(user.get_profile())
    print(user.get_qna())
    print(user.get_complete())
