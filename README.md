#🌸 AI Emotion Response Demo | Self-Doubt Theme

A gentle experiment focused on the theme of self-doubt, designed to offer a bit of comfort during low moments using simple keyword-based matching.

This is a lightweight AI emotion response demo, with future plans to evolve into a more intelligent emotional recognition and support system.

⸻

🧠 Features
	•	Emotion statement matching via keywords
	•	Gentle, randomized responses to help you through emotional lows
	•	Uses a local Excel file as the emotional response database
	•	Simple interaction: enter your feeling → get a response → exit anytime

⸻

📂 Project Structure

AI-self-doubt-Demo-1/
│
├── src/
│   └── aiLogic2.py          # Main logic: keyword matching & response output
│
├── emotion_responses.xlsx   # Keyword-response database (included in repo)
│
└── README.md                # Project description



⸻

📄 Data File Description

emotion_responses.xlsx contains two columns:

Keywords (separated by commas)	Response
procrastination, anxiety, failure	It’s okay to take things slow—you’re already trying your best.

	•	Each row represents a combination of emotion keywords and its corresponding gentle response
	•	Supports user input matching multiple keywords; system will randomly return one matching response

⸻

🚀 Quick Start
	1.	Install dependencies

pip install pandas openpyxl

	2.	Run the program

python src/aiLogic2.py

You will see this prompt:

Welcome to the Smart Response System 💗 Type “exit” to leave anytime.
Tell me how you’re feeling. For example: “I feel anxious lately” or “I’m afraid of not being enough”…

⸻

💬 Sample Dialogue

You: I always procrastinate
→ Response: It’s okay to take things slow—you’re already trying your best.

You: I’m afraid I’m not good enough
→ Response: You deserve to be loved, even if you don’t believe it right now.

You: exit
→ Response: Thank you for opening up. Let’s talk again next time~ 🌙

⸻

🔮 Roadmap
	•	✅ Improve matching logic (more flexible natural language understanding)
	•	🔧 Refactor to modular backend for easier frontend/API integration
	•	🌐 Provide API endpoints for web/mobile apps
	•	🧠 Explore emotion recognition using NLP/deep learning
	•	🎨 Build GUI version for enhanced user experience

⸻

💡 Why This Project

Not every moment has someone there to listen—but you still deserve to be heard.
This is just a small experiment, hoping to bring a bit of gentleness when you need it the most.

⸻

❤️ License

MIT License

