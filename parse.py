import re
import json
import demjson

with open("transcript.html") as f:
    transcript = f.read()
    print(len(transcript))

pattern = "window.__data__.transcriptList.push\( (.+?)\);"

results = re.findall(pattern, transcript, re.DOTALL)
for i, result in enumerate(results):
    results[i] = demjson.decode(result)

with open("transcript.json", "w") as f:
    json.dump(results, f, indent=4)
