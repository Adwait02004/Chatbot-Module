A conversational AI chatbot module integrated into the company dashboard, powered by Ollama (Phi3:mini) and built with Flask and responsive JavaScript frontend.

Table of Contents
1)Features
2)Technology Stack
3)Architecture
4)Installation
5)Usage
6)Challenges & Solutions
7)Future Plans


Features
1)Natural, context-aware conversations using Phi3:mini model via Ollama
2)Real-time Q&A with instant typing feedback and animation
3)Scroll management for long chats, manual override for reviewing history
4)Input disabling during bot response for smooth experience
5)Seamless integration as a dashboard widget

Technology Stack
Ollama with Phi3:mini model
Python Flask (Backend REST API)
HTML/CSS/JavaScript (Frontend chat UI)
Company dashboard integration (iframe or widget)

Architecture
text
User → Dashboard Chat Widget → Flask API (/get) → Ollama (Phi3:mini)
          ↑                                              ↓
  Typing Animation, Scroll Logic      Model Response streamed via REST
  
Installation
Clone the repo
git clone <repo-url>

Set up Python environment
cd <project-folder>
python -m venv venv
Linux: source venv/bin/activate      # On Windows: venv\Scripts\activate


Install Ollama and pull model
pip install flask ollama
ollama pull phi3:mini

Run Flask server
python app.py
Open dashboard and access chatbot widget

Usage
Type messages in the chat box and interact with the bot.
Scrolling is enabled during message generation for reviewing previous chats.
Integrate frontend as iframe/widget in the dashboard HTML.

Challenges & Solutions
Model load delay: Skipped preloading; backend calls model on-demand
Scroll issues during typing: Implemented user scroll detection to avoid forced auto-scroll
Slow UI for long responses: Added typing animation and chunked display

Future Plans
Add streaming API endpoint for real-time token-wise responses
Multi-model support via Ollama
Dashboard analytics and voice interaction



