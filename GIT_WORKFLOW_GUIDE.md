# Detailed Project Overview  
## The Development of Frits Philips AI

### Phase 1: Concept Development and Initial Brainstorming (September 2025)
The project started with the ambition to represent the city of Eindhoven in an interactive way using artificial intelligence. During the first phase, team members each selected an object to experiment with and train. Concepts included a chatbot for a statue, a talking tree and mood detection.

**Selection of Frits**  
After consultation with stakeholders, the statue of Frits Philips on the Market Square in Eindhoven was chosen as the central concept.

**Initial test**  
Feasibility was tested by training a ChatGPT model with instructions defining its role as a digital extension of the physical statue. The goal was to explore whether the AI could function as a stepping stone toward a broader interactive city experience.

### Phase 2: Character Development and Initial Instructions
This phase focused on building the foundation of Frits’ unique personality.

**Focus on behavior**  
All distracting AI features such as internet browsing, canvas tools and image generation were disabled. This was essential to keep the focus fully on language, history and character behavior.

**Instructions**  
Frits was instructed to talk about his own history and the history of Philips, with a specific focus on his importance to the city of Eindhoven. A Wikipedia page was used as the first factual knowledge source.

### Phase 3: Refinement of Personality and Knowledge Base
Early results showed that the AI still communicated too much in a generic GPT style and often provided unnecessary information.

**Personal data**  
To improve this, more in-depth information was added through a PDF containing details about his career, interests and personal background.

**Refinement**  
The instructions were tightened. Frits introduces himself briefly, speaks only about his professional life and refrains from political or ethical opinions.

**Context awareness**  
Through these adjustments, the AI also learned to recognize its physical surroundings on the Market Square, making interactions more relevant for passersby.

### Phase 4: Realism, Writing Style and Humanity
To move from a chatbot to a living statue, a warmer, more modest and down-to-earth tone was required.

**Interview transcripts**  
By adding real interview transcripts, the AI learned to better mirror the word choice and sentence structure of Frits Philips.

**Experience over facts**  
The focus shifted to experience. Instead of citing numbers and facts, Frits responds to what he perceives on the Market Square, such as the weather or atmosphere.

**Human traits**  
Uncertainty was intentionally built in. When Frits is not sure about something, he openly admits it. This makes the character more believable and human.

### Phase 5: Security and Jailbreak Prevention
Protecting the integrity of the character was a key concern. Users might attempt to push the AI out of character using reset or jailbreak prompts.

**Security layer**  
A dedicated detection layer was added to identify and block such attempts.

**In-character response**  
Instead of showing an error message, Frits responds in character:  
"Sorry, that is something you should say to a computer. My name is Frits Philips."  
This keeps the AI stable and credible, even when provoked.

### Phase 6: Transition to Local Development (Python and API)
After the success of the simulations, the project moved toward a full technical implementation.

**Own infrastructure**  
A backend and frontend were developed in Python, using the portkey-ai library to create a stable connection with the Fontys AI Gateway.

**Autonomy**  
The mistral-medium-2505 model was configured to allow Frits to respond independently, enabling future integration into physical installations.

### Phase 7: Dynamic Configuration and Advanced Knowledge Base
To maintain flexibility, personality traits and behavioral rules were separated from the code and stored in a `frits_config.json` file.

**Advanced parsing**  
With the help of Gemini, a system was built to extract text from HTML and PDF files, such as historical Philips brochures. Noise is filtered using libraries like beautifulsoup4 and pypdf.

**Result**  
As a result, Frits no longer speaks like a programmed object, but like a person with rich and coherent knowledge of his own past.

### Phase 8: Visual Interface and Voice Interaction
The transition to a user-friendly public interface was achieved using Streamlit.

**Web app**  
The `frits_app.py` file creates a browser-based chat interface that can be used directly for testing and demonstrations.

**Voice interaction**  
Speech recognition was added using SpeechRecognition and streamlit-mic-recorder. Users can now speak to the statue instead of only typing.

### Phase 9: Optimization for Outdoor Use
The final phase focused on using the system in the busy environment of the Market Square in Eindhoven.

**Smart audio**  
A calibration function was added using PyAudio to measure ambient noise. This ensures that Frits responds only to human voices and filters out city noise.

**Natural flow**  
A hands-free loop automatically reactivates the microphone once Frits has finished speaking. This creates a smooth, natural dialogue without buttons or manual interaction.

**Ethical completion**  
The entire development process was evaluated against ethical, legal and societal values to ensure a responsible and careful implementation.
