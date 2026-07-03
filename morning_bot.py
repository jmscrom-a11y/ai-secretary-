import datetime, ollama, subprocess
def main():
    data = subprocess.run(['python3', 'competitor_summary.py'], capture_output=True, text=True).stdout
    dt = datetime.datetime.now().strftime("%Y-%m-%d")
    sp = f"You are an elite Executive Assistant. Format: 1. Title ({dt}) 2. Executive Summary 3. Key Highlights 4. Strategic Insight. Tone: Professional business Korean."
    res = ollama.generate(model="qwen2.5-coder:14b", prompt=data or "No data", system=sp, options={"temperature": 0.3, "num_predict": 1500})["response"]
    print(res)
    subprocess.run(['python3', 'telegram_send.py', res])
if __name__ == "__main__": main()

