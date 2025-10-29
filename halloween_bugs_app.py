# halloween_bugs_app.py
import streamlit as st
from openai import OpenAI
import hashlib
import base64
from pathlib import Path
from PIL import Image
import io

# -------- CONFIG --------
CACHE_DIR = Path("image_cache")
CACHE_DIR.mkdir(exist_ok=True)

# ---- API KEY ----
client = OpenAI(api_key="replace with your key")  # <--

# -------- STREAMLIT PAGE SETUP --------
st.set_page_config(
    page_title="🐞 Bug Morph Lab",
    layout="centered",
    page_icon="🔬"
)

# -------- MAGIC CSS --------
st.markdown(
    """
    <style>
    body { 
        background-color: #fff8f5;
        font-family: 'Comic Sans MS', 'Chalkboard', 'Arial', sans-serif;
    }
    h1 {
        color: #5c2a9d;
        font-size: 48px;
        text-align: center;
        margin-bottom: 0.1em;
    }
    .stButton>button {
        background-color: #ffd6e8;
        color: #5c2a9d;
        border-radius: 12px;
        border: none;
        font-size: 20px;
        padding: 0.8em 1.2em;
        margin: 0.3em;
        transition: all 0.2s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        width: 140px;
    }
    .stButton>button:hover {
        background-color: #f5b8d0;
        transform: scale(1.05);
        box-shadow: 0 6px 10px rgba(0,0,0,0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------- HEADER --------
st.markdown("<h1>🔬🐛 Bug Morph Lab</h1>", unsafe_allow_html=True)
st.write("<p style='text-align:center; font-size:18px;'>Create your own magical Halloween bug poster!</p>", unsafe_allow_html=True)

# -------- USER OPTIONS --------
bugs = ["Ladybug", "Butterfly", "Beetle", "Spider", "Moth", "Firefly",
        "Caterpillar", "Dragonfly", "Bumblebee", "Grasshopper",
        "Praying Mantis", "Snail", "Cricket", "Doodlebug"]
characters = ["Witch", "Vampire", "Ghost", "Pumpkin", "Mummy", "Skeleton", "Zombie"]
backgrounds = ["Spooky night", "Graveyard", "Fall leaves", "Pumpkin patch"]
styles = ["Cartoon / Whimsical", "Semi-realistic / Detailed"]

# -------- STEP-BY-STEP SELECTION --------
st.write("### Step 1: Choose a bug")
selected_bug = st.radio("Select your bug:", bugs, horizontal=True)

st.write("### Step 2: Choose a Halloween character")
selected_character = st.radio("Select your character:", characters, horizontal=True)

st.write("### Step 3: Choose a background theme")
selected_background = st.radio("Select the background:", backgrounds, horizontal=True)

st.write("### Step 4: Choose an art style")
selected_style = st.radio("Select the art style:", styles, horizontal=True)

# -------- CREATIVE NAMES & FACTS --------
creative_names = {
    ("Butterfly", "Vampire"): "Count Flutter",
    ("Ladybug", "Witch"): "Lady Hex",
    ("Spider", "Ghost"): "Spooky Spinner"
}
default_name = creative_names.get((selected_bug, selected_character), f"{selected_character} {selected_bug}")
character_name = st.text_input("Give your creature a name:", default_name)

fun_facts = {
    "Ladybug": "Ladybugs can eat up to 5,000 aphids in their lifetime, making them tiny Halloween heroes!",
    "Butterfly": "Some butterflies taste with their feet, spooky or cool!",
    "Beetle": "Beetles have hard shells that protect them, like tiny Halloween armor!",
    "Spider": "Spiders can spin silk stronger than steel of the same thickness!",
    "Moth": "Some moths are nocturnal, flying around at night like Halloween ghosts!",
    "Firefly": "Fireflies glow in the dark, perfect for Halloween magic!",
    "Caterpillar": "Caterpillars transform into butterflies, a magical Halloween metamorphosis!",
    "Dragonfly": "Dragonflies can fly forwards and backwards, a Halloween aerial trick!",
    "Bumblebee": "Bumblebees buzz around flowers, tiny Halloween bees!",
    "Grasshopper": "Grasshoppers can jump over 20 times their body length, Halloween acrobatics!",
    "Praying Mantis": "Praying mantises have spooky triangle heads and precise hunting moves!",
    "Snail": "Snails carry their homes on their back, like little Halloween shells!",
    "Cricket": "Crickets chirp at night, Halloween music from nature!",
    "Doodlebug": "Doodlebugs dig tunnels underground, Halloween explorers!"
}
fact = fun_facts.get(selected_bug, "")

# -------- PROMPT BUILDER (hidden) --------
def build_prompt(bug, character, background, character_name, fact, style):
    style_prompt = "cute, whimsical, soft pastel colors, kid-friendly" if style.startswith("Cartoon") \
        else "semi-realistic, detailed, soft lighting, Halloween-themed"
    prompt_text = (
        f"A {style_prompt} Halloween poster illustration of '{character_name}', "
        f"a {character} {bug}, set in a {background}. "
        f"Include at the top the title 'Bug Morph Lab' with clear spacing from edges, "
        f"in the center the name '{character_name}' in slightly larger letters, "
        f"and at the bottom the fun fact: '{fact}' in a smaller but readable font. "
        f"Ensure all text is fully visible inside a 1024x1024 square with safe margins, "
        f"no cropping, clean composition, and a fun, child-friendly Halloween style."
    )

    # Hidden debug print
    print("DEBUG PROMPT:", prompt_text)
    return prompt_text

# -------- CACHING & IMAGE GENERATION --------
def cached_image(prompt_text):
    key = hashlib.sha256(prompt_text.encode("utf-8")).hexdigest()
    path = CACHE_DIR / f"{key}.png"
    if path.exists():
        return path
    resp = client.images.generate(
        model="gpt-image-1",
        prompt=prompt_text,
        size="1024x1024",
        n=1
    )
    b64 = resp.data[0].b64_json
    if not b64:
        raise RuntimeError("No image returned from API.")
    img_bytes = base64.b64decode(b64)
    path.write_bytes(img_bytes)
    return path

# -------- GENERATE BUTTON --------
if st.button("✨ Generate my magical creature ✨"):
    if not character_name.strip():
        st.warning("Please give your bug a name!")
    else:
        prompt = build_prompt(selected_bug, selected_character, selected_background, character_name, fact, selected_style)
        with st.spinner("Summoning your magical creature..."):
            try:
                img_path = cached_image(prompt)
                img = Image.open(img_path)
                st.image(img, caption=f"{character_name}", use_container_width=True)

                buf = io.BytesIO()
                img.save(buf, format="PNG")
                st.download_button(
                    "💾 Download Poster",
                    data=buf.getvalue(),
                    file_name=f"{character_name}.png"
                )
            except Exception as e:
                st.error(f"Could not generate image: {e}")
