class Query:
    def __init__(self):
        pass

    def search_profile(self, email):
        return {"data.profile.email": email}
    

    def update_profile(self, name=None, gender=None):
        
        updated_values = {}

        if name != None:
            updated_values["data.profile.name"] = name

        if gender != None:
            updated_values["data.profile.gender"] = gender

        query = {"$set": updated_values}
        print(query)
        return query

    
    def search_qna(self):
        pass

    def update_qna(self):
        pass