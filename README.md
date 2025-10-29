# 🐞 Bug Morph Lab

**Bug Morph Lab** is an interactive web app that transforms real insect species into creative, AI-generated Halloween characters.  
Built with **Streamlit** and **OpenAI’s image generation API**, this project combines entomology, AI, and education to inspire curiosity about biodiversity in a fun, visual way.  

---

## ✨ Features
- 🎨 Generate AI illustrations of insects as themed characters (e.g., superheroes, Halloween creatures).  
- 🪲 Include scientific names, creative names, and fun facts.  
- ⚡ Simple web interface powered by Streamlit.  
- 🧠 Encourages STEM learning through art and AI.  

---

## 🧠 Tech Stack
- **Python 3.10+**  
- **Streamlit**  
- **OpenAI API**  
- **Pillow**, **Requests**, **OS**, **JSON**

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Skvalicharla/bug-morph-lab.git
cd bug-morph-lab
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Add your OpenAI API key
Create a file named `.env` in the project root and add:
```
OPENAI_API_KEY=your_api_key_here
```

> ⚠️ **Important:** Make sure `.env` is included in your `.gitignore` file so your API key remains private.

### 4️⃣ Run the app
```bash
streamlit run app.py
```

---

## 📁 File Structure
```
bug-morph-lab/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Dependencies
├── .env                  # Your private API key (not uploaded)
├── .gitignore            # Ignore sensitive and temp files
└── README.md             # Project documentation
```

---

## 📸 Preview
*(Add a screenshot or sample generated image here)*  
Example:  
> “A dragonfly morphed into a vampire with glowing wings and fangs.”

---

## 📜 License
Licensed under the **MIT License** – see the [LICENSE](./LICENSE) file for details.  
You’re free to use and adapt this for educational or creative purposes with credit to **Sruthi**.

---


## 💬 Acknowledgements
- 🧠 **OpenAI** — for image generation  
- ⚙️ **Streamlit** — for the web app framework  
- 🪲 Inspired by real-world entomology and curiosity-driven learning  
