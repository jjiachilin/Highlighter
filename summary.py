import os
import openai
import json

openai.api_key = "sk-7feZk6oBEYLBfhLXSyF9wFjUrnBlwgt4J96Gqctp"

"""
f = open("lecture_subs.txt")

all_text = f.read().replace("\n", " ")

f.close()

f = open("lecture_subs.txt")
selected_text = ""

for _ in range(176):
    f.readline()

for _ in range(88):
    new_line = f.readline()
    if new_line == "\n":
        continue
    selected_text += new_line.replace("\n", " ")
"""

# returns string summary
def get_summary(selected_text):
    selected_text.replace("\n", " ")
    selected_text += "\n\ntl;dr"

    response = openai.Completion.create(
        engine="davinci",
        prompt=selected_text,
        temperature=0.2,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    # clean up response
    response = response["choices"][0]["text"]
    if response[len(response)-1] != ".":
        if response.rfind(".") != -1:
            response = response[:response.rfind(".")+1]
    response = response.replace("\n", " ")    
    while not response[0].isalnum():
        response = response[1:]
    return response.strip()

# returns an array of strings for keywords
def get_keywords(selected_text):
    selected_text = "Text: " + selected_text + " \n\nKeywords:"
    keywords = openai.Completion.create(
        engine="davinci",
        prompt=selected_text,
        temperature=0.3,
        max_tokens=max(20, int(len(selected_text)/15)),
        top_p=1.0,
        frequency_penalty=0.9,
        presence_penalty=0.0,
        stop=["\n"]
    )
    return keywords["choices"][0]["text"].replace(" ", "").split(",")

print(get_summary(selected_text))
print(get_keywords(selected_text))