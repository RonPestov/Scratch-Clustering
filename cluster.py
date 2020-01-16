import re
str1 = ""
data = []
li = []
import json

with open("C:/Users/Ron/Desktop/project_block_stacks_mini.json") as f: #open the json file
    for f in open('C:/Users/Ron/Desktop/project_block_stacks_mini.json', 'r'): #iterates through every line inside json file
        dict = json.loads(f) #each line is stored in the dictionary dict
        str1 = dict['stack_squeak'] #appends the string with only stack_squeak element
        data.append(str1) #only the stack_squeak elements are added to the data list 
        str1 = ""
        #str1 += dict['stack_squeak'] #appends the string with only stack_squeak elements

for i in data: #the words "coming soon!" do not get properly deleted, but everything else should be parsed.
    str1 = re.sub('".*?"', '', i) #removes anything in the string surrounded by " "
    str1 = re.sub('[\)\(\=\>\<\&\+\|\*\/\-]', '',str1) #removes unnecesary symbols from list
    str1 = str1.strip() #removes unnecessary whitespace

    li.append(str1.split())
    str1 = ""
    
for i in li:
   print(i)

#from sklearn.feature_extraction.text import CountVectorizer
#corpus = li
#vectorizer = CountVectorizer()
#X = vectorizer.fit_transform(corpus)
#print(vectorizer.get_feature_names())
#
#print(X.toarray())