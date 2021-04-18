## Inspiration
After an entire year of school at Zoom university, we grew sick and tired of juggling listening to the professor's lecture and constantly
alt-tabbing to take notes on slides. Our solution aims to alleviate this issue by seamlessly generating context-aware summaries and keywords
during a live Zoom meeting from user marked timestamps. 

## What it does
Our current iteration is a bare bones prototype command line interface. To use our project the user must first record timestamps during the 
live meeting and then download the audio transcript later to generate the summaries. The steps are outlined below:

0. first install requirements.txt
```
pip install -r requirements.txt
```
1. Enter Zoom meeting and run:
```
python main.py
```
2. press cntl-shift-r to record the timestamp of an important concept
3. press cntl-shift-q to quit the program after your timestamps have been recorded. A folder called ts_recordings will contain your timestamp.txt 
file.
4. Wait for zoom recording to be released and then download the html file of the recording.
5. run
```
python summarize.py <timestamp.txt> <meeting.html>
```
6. Your summaries will be in output.txt!

## How we built it
The summarizing component of our project was powered with OpenAI's Davinci engine which generates a tl;dr of the text surrounding a timestamp.
Everything else including the command line argument parsing and data pre-processing and post-processing was built with python. 

## Challenges we ran into
Our initial idea was very ambitious and had to be scaled back to fit into the timeframe of one weekend. Instead of a full on GUI and live meeting
summary generation, we had to focus on making all of the components work together too. Also, OpenAI, while very impressive, does not work as well on spontaneous speech without proper syntax. We alleviated this problem by also including keywords in the output which is more deterministic. After further testing, we also discovered that there was also a lot of noise and occasionally mistranscribed audio in the Zoom audio transcription which resulted in some interesting outputs.

## Accomplishments that we're proud of
We are most proud of our idea of leveraging AI to help students like us struggling to adapt to the minor inconveniences of online school. We hope to inspire others to do the same for an increasingly virtual education environment. 

## What we learned
In doing research about how to choose text around a timestamp and how to summarize the chosen text, we learned a lot about what the current cutting edge NLP models are capable of. We also learned about the python packages used to stitch everything together, including time, parse, and sys.

## What's next for POGGERS AI
We want to add a user-friendly GUI, a speech-to-text module that will allow live summary generation to save users the trouble of having to wait for a recording to be released and then downloading an html file. We also hope to improve our text selection method, which currently does not rely on an ML model.
