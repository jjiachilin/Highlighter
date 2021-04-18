import re
import json
import demjson


def get_transcript_json(transcript_path):
    with open(transcript_path) as f:
        transcript = f.read()

    pattern = "window.__data__.transcriptList.push\( (.+?)\);"

    results = re.findall(pattern, transcript, re.DOTALL)
    for i, result in enumerate(results):
        results[i] = demjson.decode(result)

    with open("transcript.json", "w") as f:
        json.dump(results, f, indent=4)

    return results

if __name__ == "__main__":
    get_transcript_json("transcript.html")
