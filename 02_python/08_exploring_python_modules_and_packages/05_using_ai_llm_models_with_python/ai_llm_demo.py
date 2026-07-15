# =============================================================================
# 08 - Exploring Python Modules and Packages
# =============================================================================
# Topic        : Using AI LLM Models with Python
# File         : 05_using_ai_llm_models_with_python/ai_llm_demo.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================
#
# This file ties together everything from this class:
#   - pip installing third-party packages (google-genai, python-dotenv)
#   - reading an API key using the os module (built-in)
#   - calling an external service and handling the JSON-like response
#
# ── STEP 0: pip install what is needed ───────────────────────────────────────
#   pip install google-genai python-dotenv
#
#
# ── THE #1 RULE OF WORKING WITH API KEYS ────────────────────────────────────
# An API key should never be written directly into a .py file, like this:
#
#       client = genai.Client(api_key="AIzaSyC...actualSecretKey...")   # Incorrect
#
# Why this matters:
#   - The moment this file is pushed with `git push`, the key becomes public.
#   - Automated bots scan GitHub continuously, specifically looking for
#     leaked API keys.
#   - Anyone who finds it can use the key, run up charges on the account it
#     belongs to, or get it flagged and revoked for abuse.
#
# The fix: keep the key in a ".env" file that is never committed to git,
# and load it into the program at runtime using environment variables.
#
#   1. Create a file called ".env" (see .env.example in this same folder)
#      GEMINI_API_KEY=the_real_key_here
#
#   2. Confirm ".env" is listed in .gitignore so git never tracks it.
#
#   3. Load it in Python using python-dotenv + os.environ (shown below).
# =============================================================================

import os
from dotenv import load_dotenv

load_dotenv()   # Reads the ".env" file and loads its values into os.environ

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("No API key found. Copy .env.example to .env and add a real key.")
else:
    from google import genai

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Explain what a Python module is, in exactly two sentences.",
    )

    print(response.text)
    # Expected output: a short two-sentence explanation of Python modules,
    # generated live by the model (wording will vary on each run).


# =============================================================================
# Key Takeaways
# =============================================================================
# - LLM SDKs (google-genai, openai, anthropic, etc.) are pip packages like
#   any other — install them, import them, call their functions.
# - Every LLM provider requires an API key to identify and bill the account.
# - Secrets (API keys, passwords, tokens) should always be loaded from
#   environment variables or a .env file — never hardcoded into a .py file.
# - .env should be added to .gitignore before the first commit.
# - If a key is ever accidentally exposed (committed, pasted in chat,
#   screenshotted), it should be revoked and regenerated immediately in the
#   provider's dashboard — treated exactly like a leaked password.
# =============================================================================
