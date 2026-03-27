## Haiku Bot by Dopamine Studios

A specialized Discord bot built with `discord.py` on top of [Dopamine Framework](https://github.com/dopaminestudios/dopamine-framework) that silently monitors conversations to catch accidental poetry. When a user sends a message that fits the **5-7-5 syllable structure**, the bot formats it into a beautiful haiku embed.

---

### Features

* **Real-time Detection:** Processes incoming messages through an asynchronous worker queue to ensure zero lag in your chats.
* **Advanced Syllable Scoring:** Uses a multi-layered approach to count syllables:
    * **Custom Dictionary:** A local SQLite database for manual overrides.
    * **Linguistic Libraries:** Integration with `pronouncing` and `syllapy`.
    * **Slang Awareness:** Correctly handles common internet acronyms (lol, lmao, tbh, etc.).
    * **Algorithmic Fallback:** A robust regex-based heuristic for words not found in dictionaries.
* **Smart Cleaning:** Automatically filters out URLs, emojis, code blocks, and excessive character repetitions to prevent false positives.
* **Number Conversion:** Uses `inflect` to translate, for example, "42" into "forty two" for accurate syllable counting.

Additionally, since the bot is built on top of [Dopamine Framework](https://github.com/dopaminestudios/dopamine-framework), you get access to all its commands and features, including smart command syncing, owner dashboard (accessed through `/od`), and more.

---

### Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/dopaminestudios/haikubot.git
    cd haikubot
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Setup Environment:**

    Create a `.env` file in the root directory:
    ```env
    DISCORD_TOKEN=your_bot_token_here
    ```

4.  **Initialize Databases**
    Ensure a `databases/` folder exists in your root directory.

---

### Usage
Run the bot using:
```bash
python main.py
```

#### Commands
* `/haiku detection enable` – Turn on haiku monitoring for the current server (Requires Moderator permissions).
* `/haiku detection disable` – Turn off haiku monitoring.
* `!!view_haiku_word_count` – (Owner Only) Check the size of the syllable cache.
* `!!update_haiku_database` – (Owner Only) Manually add or correct a word's syllable count. Type a list of words with their syllable count in the following format: `word 1, anotherword 4, thing 1, letters 2`. 

...and all commands included in [Dopamine Framework](https://github.com/dopaminestudios/dopamine-framework).

---

### License & Attribution
This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0). This means if you modify the bot and run it as a service, you must share your modified source code under the same license.

The bot already mentions credit to **Dopamine Studios** in the message sent when the bot is invited to a server. **You must not remove the attribution** from that message.

---

<sub>This bot is a distilled version of [Dopamine](https://github.com/dopaminestudios/dopamine), the Giveaway, Moderation, and multi-purpose bot that includes the same Haiku detection feature. If you want to use this Haiku detection feature without self-hosting, invite Dopamine by [clicking here](https://top.gg/bot/1411266382380924938/invite).