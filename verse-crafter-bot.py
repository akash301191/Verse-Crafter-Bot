import streamlit as st
from agno.agent import Agent
from agno.models.openai import OpenAIChat

def initialize_openai_model():
    try:
        api_key = st.session_state.openai_api_key
        return OpenAIChat(id='gpt-4o', api_key=api_key)
    except Exception as e:
        st.error(f"❌ Error initializing OpenAI Model: {e}")
        return None

def render_poetry_preferences():
    # Split layout into three evenly balanced columns
    col1, col2, col3 = st.columns(3)

    # 📌 Column 1: Poem Intent
    with col1:
        st.subheader("📝 Poem Intent")

        poem_type = st.selectbox(
            "What kind of poem would you like?",
            [
                "Romantic", "Reflective", "Motivational", "Melancholic", "Nature inspired",
                "Humorous", "Narrative", "Abstract", "Spiritual", "Celebratory",
                "Farewell", "Gratitude", "Inspirational", "Apology", "Friendship", "Mystical"
            ]
        )

        theme = st.text_input(
            "What is the central theme or subject?",
            placeholder="e.g., lost love, forest at dawn, resilience"
        )

        recipient = st.text_input(
            "Who is the poem for? (optional)",
            placeholder="e.g., myself, a friend, a loved one"
        )

    # 📌 Column 2: Mood & Structure
    with col2:
        st.subheader("🎨 Mood & Structure")

        mood = st.selectbox(
            "Choose a tone or mood for the poem",
            [
                "Hopeful", "Wistful", "Dark and deep", "Playful", "Calm and serene", "Passionate",
                "Mysterious", "Joyful", "Lonely", "Nostalgic", "Empowering", "Dreamy", "Heartbroken",
                "Melancholic", "Angry", "Curious", "Grateful", "Philosophical", "Whimsical", "Sacred",
                "Bittersweet", "Surreal", "Flirty", "Romantic", "Satirical", "Ironic", "Reflective", "Introspective"
            ]
        )

        structure = st.selectbox(
            "Choose a poem structure",
            ["Free Verse", "Rhyming Couplets", "Haiku", "Limerick", "Sonnet", "Acrostic", "Surprise Me"]
        )

        length = st.selectbox(
            "Preferred poem length",
            [
                "Very Short (3–5 lines)", "Short (6–10 lines)", "Medium (11–15 lines)",
                "Long (16–25 lines)", "Very Long (26–40 lines)", "Extended (41–60 lines)", "Epic (60+ lines)"
            ]
        )

        length_mapping = {
            "Very Short (3–5 lines)": (3, 5),
            "Short (6–10 lines)": (6, 10),
            "Medium (11–15 lines)": (11, 15),
            "Long (16–25 lines)": (16, 25),
            "Very Long (26–40 lines)": (26, 40),
            "Extended (41–60 lines)": (41, 60),
            "Epic (60+ lines)": (60, 100)
        }

    # 📌 Column 3: Customization
    with col3:
        st.subheader("✨ Customization")

        wants_title = st.radio(
            "Would you like a title to be generated?",
            ["Yes", "No, I’ll provide one"], index=0, horizontal=True
        )

        custom_title = None
        if wants_title == "No, I’ll provide one":
            custom_title = st.text_input("Enter your preferred title (optional)")

        keywords = st.text_input(
            "Any words or phrases you'd like included? (optional)",
            placeholder="e.g., moonlight, echo, distant hills"
        )

        mimic_poet = st.selectbox(
            "Mimic the style of a famous poet? (optional)",
            [
                "None", "William Shakespeare", "Robert Frost", "Emily Dickinson", "Langston Hughes",
                "Rumi", "Sylvia Plath", "Pablo Neruda", "Maya Angelou", "John Keats", "William Wordsworth"
            ]
        )

        wants_explanation = st.radio(
            "Would you like a summary or explanation of the poem?",
            ["Yes", "No"], index=1, horizontal=True
        )

    # 📘 Poem Structure Guide (expander at bottom)
    with st.expander("📘 Learn more about poem structures with examples"):
        c1, c2, c3, c4, c5, c6 = st.columns(6)

        with c1:
            st.markdown("**Free Verse**")
            st.markdown("*No rules. Just natural flow.*")
            st.markdown("> I walk alone where no path lies,  \n> The wind decides my destination.")

        with c2:
            st.markdown("**Rhyming Couplets**")
            st.markdown("*Pairs of lines with rhyming ends (AABB).*")
            st.markdown("> The stars above begin to gleam,  \n> While I drift into a dream.")

        with c3:
            st.markdown("**Haiku**")
            st.markdown("*3 lines, nature-themed, 5-7-5.*")
            st.markdown("> Winter whispers low  \n> Beneath the quiet snowfall  \n> Dreams begin to glow.")

        with c4:
            st.markdown("**Limerick**")
            st.markdown("*5-line poem, humorous, AABBA rhyme.*")
            st.markdown("> A cat with a love for ballet,  \n> Danced gracefully every day...")

        with c5:
            st.markdown("**Sonnet**")
            st.markdown("*14 lines, classic rhyme, romantic.*")
            st.markdown("> Your smile, a spark.  \n> My world turns bright.")

        with c6:
            st.markdown("**Acrostic**")
            st.markdown("*First letter of each line spells a word.*")
            st.markdown("> **H**olding hope in every night,  \n> **E**ven when we lose the light.")

        st.markdown("**Surprise Me**")
        st.markdown("*Let the Bot randomly choose a poetic form for you — perfect if you're feeling curious or adventurous!*")

    # 🧠 Final output
    return {
        "poem_type": poem_type,
        "theme": theme,
        "recipient": recipient,
        "mood": mood,
        "structure": structure,
        "length": length,
        "length_range": length_mapping[length],
        "custom_title": custom_title,
        "keywords": keywords,
        "wants_explanation": wants_explanation,
        "mimic_poet": mimic_poet
    }

def generate_poem(openai_model, user_preferences: dict) -> str:
    """
    Generate a personalized poem using the given OpenAI model and user preferences.
    Returns markdown-formatted string with a poem and optional explanation.
    """

    # Required parameters
    poem_type = user_preferences["poem_type"]
    theme = user_preferences["theme"]
    mood = user_preferences["mood"]
    structure = user_preferences["structure"]
    length_range = user_preferences["length_range"]

    # Optional parameters
    recipient = user_preferences["recipient"]
    custom_title = user_preferences["custom_title"]
    keywords = user_preferences["keywords"]
    wants_explanation = user_preferences["wants_explanation"] == "Yes"
    mimic_poet = user_preferences["mimic_poet"]

    # Compose instruction lines
    instructions = [
        "Compose a personalized poem using the following preferences.",
        f"Poem type: {poem_type}. Structure: {structure}. Tone: {mood}.",
        f"Theme or subject: {theme}.",
        f"Line count should be between {length_range[0]} and {length_range[1]}.",
        "The poem must begin with a markdown-formatted title using the format: ### <Title>",
    ]

    # Optional additions
    if recipient:
        instructions.append(f"The poem is for: {recipient}.")
    if keywords:
        instructions.append(f"Include these words or ideas: {keywords}.")
    if mimic_poet != "None":
        instructions.append(f"Try to mimic the poetic style of {mimic_poet}.")
    if custom_title:
        instructions.append(f"Use this title exactly: ### {custom_title}")
    else:
        instructions.append("You must generate a poetic title and place it in markdown as: ### <Title>")

    if wants_explanation:
        instructions.append("After the poem, add a short explanation (2–4 lines) under the markdown heading '### 📖 Explanation'.")
    else:
        instructions.append("Do not include any explanation. Only return the poem with its title.")

    instructions.append("Format everything using clean markdown.")

    # Run the agent
    poem_agent = Agent(
        name="Verse Crafter",
        role="Composes customized poems based on emotion, structure, and creative intent",
        model=openai_model,
        instructions=instructions
    )

    response = poem_agent.run("")  # No user message; context lives in instructions

    return response.content.strip()


def main() -> None:
    # Page config
    st.set_page_config(page_title="Verse Crafter Bot", page_icon="📝", layout="wide")

    # Custom styling
    st.markdown(
        """
        <style>
        .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }
        div[data-testid="stTextInput"] {
            max-width: 1200px;
            margin-left: auto;
            margin-right: auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Header and intro
    st.markdown("<h1 style='font-size: 2.5rem;'>📝 Verse Crafter Bot</h1>", unsafe_allow_html=True)
    st.markdown(
        "Welcome to Verse Crafter Bot — a creative Streamlit tool that composes personalized poems shaped by your mood, theme, and style, helping you turn thoughts into beautiful verse.",
        unsafe_allow_html=True
    )

    # Get OpenAI API Key
    openai_api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        help="Don't have an API key? Get one [here](https://platform.openai.com/account/api-keys)."
    )

    if openai_api_key:
        st.session_state.openai_api_key = openai_api_key
        st.success("✅ API key updated!")

    st.markdown("---")

    user_preferences = render_poetry_preferences()
    st.markdown("---")

    if st.button("✍️ Craft My Verse"):
        if not hasattr(st.session_state, "openai_api_key"):
            st.error("Please provide your OpenAI API key.")
        else:
            openai_model = initialize_openai_model()
            with st.spinner("Crafting your personalized poem ..."):
                poem = generate_poem(openai_model, user_preferences)
                st.session_state.poem = poem  # Store result

    if "poem" in st.session_state: 
        st.markdown(st.session_state.poem)

        st.download_button(
            label="📥 Download Verse",
            data=st.session_state.poem,
            file_name="verse_crafter_output.txt",
            mime="text/plain"
        )        

if __name__ == "__main__": 
    main()