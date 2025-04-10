# Verse Crafter Bot

Verse Crafter Bot is a creative Streamlit application that composes personalized poems shaped by your mood, theme, and style. Whether you're feeling wistful, romantic, curious, or reflective, this bot helps you turn thoughts into elegant verses in seconds. Powered by [Agno](https://github.com/agno-agi/agno) and OpenAI’s GPT-4o model, it delivers beautifully formatted poems and optional explanations — making poetry creation as intuitive as journaling.

## Folder Structure

```
verse-crafter-bot/
├── verse-crafter-bot.py
├── README.md
└── requirements.txt
```

- **verse-crafter-bot.py**: The main Streamlit application.
- **requirements.txt**: A list of all required Python packages.
- **README.md**: This documentation file.

## Features

- **Poetry Customization Interface**  
  Choose your poem's tone, structure, length, and theme. Optionally specify a title, recipient, stylistic inspiration (like Rumi or Dickinson), and key words to include.

- **Dynamic Structure Selection**  
  Select from poetic forms such as Free Verse, Haiku, Rhyming Couplets, Sonnets, and more — or choose "Surprise Me" for random creativity.

- **Mimic Famous Poets (Optional)**  
  Add an artistic twist by having your poem emulate the style of legendary poets like Shakespeare, Frost, Angelou, and others.

- **Markdown-Formatted Output**  
  Each poem begins with a title (e.g., `**The Rising Fog**`) and is optionally followed by an interpretation section.

- **Instant Downloads**  
  Save your poem and its explanation as a `.txt` file with a single click.

- **Sleek, Guided UI**  
  An organized layout with tooltips and expanders ensures an intuitive and enjoyable writing experience — even for first-time poets.

## Prerequisites

- Python 3.11 or higher  
- An OpenAI API key (get yours [here](https://platform.openai.com/account/api-keys))

## Installation

1. **Clone the repository** (or download it):
   ```bash
   git clone https://github.com/akash301191/Verse-Crafter-Bot.git
   cd Verse-Crafter-Bot
   ```

2. **(Optional) Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate        # On macOS/Linux
   # or
   venv\Scripts\activate           # On Windows
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run verse-crafter-bot.py
   ```

2. **Open your browser** to the local URL shown in the terminal (usually `http://localhost:8501`).

3. **Interact with the app**:
   - Enter your OpenAI API key when prompted.
   - Fill out your poem preferences including tone, style, and length.
   - (Optional) Specify a custom title, keywords, recipient, or a poet to mimic.
   - Click the **Craft My Verse** button.
   - View your poem (and explanation if requested).
   - Download the result as a `.txt` file for sharing or safekeeping.

## Code Overview

- **`main`**: Orchestrates the app flow — from collecting inputs and calling the model to rendering and downloading the final result.
- **`render_poetry_preferences`**: Renders the three-column form with poem intent, mood/structure, and personalization settings.
- **`generate_poem`**: Uses a guided instruction set to generate a poem and optional explanation via a GPT-4o agent.
- **`initialize_openai_model`**: Authenticates and loads the OpenAI model using the user-provided API key.

## Contributions

Contributions are welcome! Feel free to fork the repository, improve the code, and open a pull request. Please ensure that your changes follow the existing style and include any necessary documentation or tests.