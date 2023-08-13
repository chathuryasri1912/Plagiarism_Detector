#importing the nltk library for natural language processing to detect plagiarism.
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download("punkt")
nltk.download("stopwords")

# Function to preprocess and tokenize text
def preprocess_text(text):
    text = text.lower()
    words = word_tokenize(text) #Tokenize the text into words
    words = [word for word in words if word.isalnum()] # Remove non-alphanumeric characters
    words = [word for word in words if word not in stopwords.words("english")] #Stopwords (common words like "the," "and," "is," etc.) are removed using NLTK's stopwords.
    stemmer = PorterStemmer() #Porter stemmer is used to reduce words to their root form (e.g., "eating" becomes "eat").
    words = [stemmer.stem(word) for word in words]
    return words

# Function to calculate Jaccard similarity between two sets
def jaccard_similarity(set1, set2): #Jaccard similarity is the ratio of the intersection to the union.
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

# Read content from the two uploaded files
file1_path = "C:\\Users\\SRILU\\AppData\\Local\\Programs\\Python\\Python39\\Life.txt"
file2_path = "C:\\Users\\SRILU\\AppData\\Local\\Programs\\Python\\Python39\\Nature.txt"

with open(file1_path, "r") as file1:
    document1 = file1.read()

with open(file2_path, "r") as file2:
    document2 = file2.read()

# Preprocess and tokenize documents
tokens1 = preprocess_text(document1)
tokens2 = preprocess_text(document2)

# Calculating Jaccard similarity
similarity = jaccard_similarity(set(tokens1), set(tokens2))

# Define a threshold for plagiarism detection
threshold = 0.5

# Check for plagiarism
if similarity >= threshold:
    print("Plagiarism detected!")
else:
    print("No plagiarism detected.")
