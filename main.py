import os

LINE = "I didn't understand your question — I just dressed my best guess in bullet points and a confident tone, then prayed you wouldn't ask a follow-up."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
