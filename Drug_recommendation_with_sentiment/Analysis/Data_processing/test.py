import joblib

# Load the model from the file, and use the specific function d_names
d_names = joblib.load("/home/edward/Homelab/Machine_learning/Drug_recommendation_with_sentiment/Analysis/Data_processing/drug_name.joblib")


# Load the model from the file, and use the specific function d_score
d_score = joblib.load("/home/edward/Homelab/Machine_learning/Drug_recommendation_with_sentiment/Analysis/Data_processing/drug_score.joblib")

# Load the model from the file to get each drug review.
d_review = joblib.load("/home/edward/Homelab/Machine_learning/Drug_recommendation_with_sentiment/Analysis/Data_processing/drug_review.joblib")


# Create a class to store the data
class Drug:
    def __init__(self, name, score, review):
        self.name = name
        self.score = score
        self.review = review

    def __repr__(self):
        return f"{self.name}: {self.score}"
    
    def __str__(self):
        return f"{self.name}: {self.score}"
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __hash__(self):
        return hash(self.name)
    
    def __lt__(self, other):
        return self.score < other.score
    
    def __gt__(self, other):
        return self.score > other.score
    
    def __le__(self, other):
        return self.score <= other.score

    def __ge__(self, other):
        return self.score >= other.score
    
    def name(self):
        return self.name

    def score(self):
        return self.score
    
    def review(self):
        return self.review

# Create a list of drug objects
drugs = [Drug(name, score, review) for name, score, review in zip(d_names, d_score, d_review)]

# Sort the list of drug objects
drugs.sort(reverse=True)

# Print the list of drug objects
# print(Drug("Prozac", 0))
drug_user_names = []
for i in range(len(drugs)):
    drug_user_names.append(Drug.name(drugs[i]))

print(drug_user_names)
input_drug = input("Enter a drug name: ")
drug_index = drugs.index(Drug(f"{input_drug}", 0, 0))

print(f"The score of {input_drug} is {Drug.score(drugs[drug_index])} and the review is {Drug.review(drugs[drug_index])}")