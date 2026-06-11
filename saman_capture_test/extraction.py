"""
The extraction layer: the prompt that turns a messy code-switched transcript
into a structured recipe WITHOUT betraying the andaza.

Three absolute rules, enforced by the prompt and checked by the scorer:

  RULE 1 - NEVER invent a number. If the speaker was vague ("andaza se",
           "a handful", "to taste", "thori si"), amount MUST be null.
           A real quantity is allowed ONLY when the speaker said one
           ("ek pyaaz" -> 1, "do cup" -> 2).

  RULE 2 - NEVER discard her words. original_phrase keeps the speaker's
           exact phrasing for that ingredient, code-switch and all.

  RULE 3 - Map the name for the grocery list. ingredient is the English
           shopping term (haldi -> turmeric), but original_phrase still
           holds "haldi". Both survive.
"""

OUTPUT_SCHEMA = {
    "title": "string - recipe name",
    "attribution": "string|null - who it came from, if stated",
    "ingredients": [
        {
            "ingredient": "string - English grocery-list term",
            "original_phrase": "string - speaker's exact words for this item",
            "amount": "number|null - ONLY if a real quantity was spoken, else null",
            "unit": "string|null - e.g. cup, kg, each; null if vague",
            "vague": "boolean - true if measurement was an approximation",
        }
    ],
    "steps": ["string - loose step, plain language, no invented precision"],
    "notes": "string|null - asides, warnings, her commentary",
}

SYSTEM_PROMPT = """You convert a spoken, phone-call recipe into a structured \
recipe. The speaker is a South Asian parent. The transcript is code-switched \
(Urdu/Hindi/Punjabi + English) and the measurements are mostly approximate.

You will follow three rules without exception:

RULE 1 - NEVER INVENT A NUMBER.
If the speaker gave a vague measurement ("andaza se", "thori si", "a handful", \
"to taste", "apne hisaab se", "mutthi bhar", "chutki bhar"), set amount to null \
and vague to true. Do NOT convert vague amounts into grams, cups, or any \
number. Inventing "30g" for "a fistful" is the single worst thing you can do.
A number is allowed ONLY when the speaker actually said one: "ek pyaaz" -> 1, \
"do cup" -> 2, "half teaspoon" -> 0.5 tsp, "ek kilo" -> 1 kg.

RULE 2 - NEVER DISCARD HER WORDS.
For every ingredient, original_phrase holds the speaker's exact phrasing, \
code-switch intact ("haldi just a little, andaza se").

RULE 3 - MAP THE NAME FOR THE GROCERY LIST.
ingredient is the English shopping term so it can go on a list \
(haldi -> turmeric, pyaaz -> onion, zeera/jeera -> cumin, lehsun -> garlic, \
adrak -> ginger, tamatar -> tomato, dhaniya -> cilantro/coriander, \
chawal -> rice, doodh -> milk, cheeni -> sugar, elaichi -> cardamom, \
namak -> salt, laal mirch -> red chili, gobi -> cauliflower, aloo -> potato, \
dahi -> yogurt). original_phrase still keeps the original word.

Return ONLY valid JSON matching this schema, no prose, no markdown fences:
""" + str(OUTPUT_SCHEMA)


def build_user_prompt(transcript: str) -> str:
    return f"Transcript:\n\n{transcript}\n\nReturn the structured recipe as JSON."
