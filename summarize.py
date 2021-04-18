import sys
import parse
import summary

def get_selected_text(a, b):
    return ["lmao", "hi"]

def main():
    if len(sys.argv) != 3:
        raise Exception("Usage: python summarize.py <timestamp_file> <transcript_file>")

    _, timestamp_path, transcript_path = sys.argv
    transcript_json = parse.get_transcript_json(transcript_path)
    selected_texts = get_selected_text(timestamp_path, transcript_json)

    key_points = []
    for selected_text in selected_texts:
        key_point = [summary.get_summary(selected_text), summary.get_keywords(selected_text)]
        key_points.append(key_point)

    with open("output.txt", "w") as f:
        for i in range(0, len(selected_texts)):
            f.write("Selected Texts:\n")
            f.write(selected_texts[i])
            f.write("\n\n")
            f.write("Summary:\n")
            f.write(key_points[i][0])
            f.write("\nKeywords:\n")
            f.write(key_points[i][1])
            f.write("\n\n")

if __name__ == '__main__':
    main()
