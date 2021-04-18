import os
import openai
import json

openai.api_key = "sk-7feZk6oBEYLBfhLXSyF9wFjUrnBlwgt4J96Gqctp"

f = open("lecture_subs.txt")

all_text = f.read().replace("\n", " ")

f.close()

f = open("lecture_subs.txt")

"""
selected_text = "What is the key point in this text?\n'''\n"

for _ in range(176):
    f.readline()

for _ in range(88):
    new_line = f.readline()
    if new_line == "\n":
        continue
    selected_text += new_line.replace("\n", " ")

selected_text += "\n'''\n The key point is:\n"
"""

f = open("selected.txt")
selected_text = f.read().replace("\n", " ")

print(selected_text)

response = openai.Completion.create(
  engine="davinci",
  prompt=selected_text,
  temperature=0.1,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response)