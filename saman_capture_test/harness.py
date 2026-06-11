#!/usr/bin/env python3
"""
Saman Pantry — recipe capture test harness.

The load-bearing wall of the Option B reposition is the voice/paste ->
structured-recipe extraction. This harness proves (or kills) it.

USAGE
  python3 harness.py --show       Read the hand-authored gold outputs. No key.
  python3 harness.py --run        Call a real model on every fixture and score.
  python3 harness.py --run --model claude-opus-4-20250514

PASS CONDITION (the only thing that matters)
  1. invented_numbers == 0   (vague input must never produce a number)
  2. high phrase preservation (her words survive)
  3. high code-switch mapping (haldi -> turmeric, etc.)

If (1) is anything but 0, you are on Path B for this week's submission,
no matter how good the rest looks.
"""

import argparse
import json
import os
import sys

from fixtures import FIXTURES
from gold import GOLD
from extraction import SYSTEM_PROMPT, build_user_prompt

DEFAULT_MODEL = "claude-sonnet-4-5"

# Vagueness cues. If any appear in an ingredient's original_phrase, a real
# number in `amount` is a RULE 1 violation (invented precision).
VAGUE_CUES = [
    "andaza", "thora", "thori", "thoda", "mutthi", "chutki", "fistful",
    "handful", "to taste", "apne hisaab", "apne taste", "just a little",
    "agar", "garam kar", "upar se", "garnish", "se daal", "jitni",
]

# Minimum code-switch mappings we expect the model to resolve for the list.
EXPECTED_MAPPINGS = {
    "haldi": "turmeric", "pyaaz": "onion", "zeera": "cumin", "jeera": "cumin",
    "lehsun": "garlic", "adrak": "ginger", "tamatar": "tomato",
    "dhaniya": ["cilantro", "coriander"], "chawal": "rice", "doodh": "milk",
    "cheeni": "sugar", "elaichi": "cardamom", "namak": "salt",
    "gobi": "cauliflower", "aloo": "potato", "dahi": "yogurt",
}


def show():
    for fx in FIXTURES:
        g = GOLD[fx["id"]]
        print("=" * 70)
        print(f"{g['title']}  ({fx['id']})")
        print("=" * 70)
        print("\nTranscript:")
        print("  " + fx["transcript"])
        print("\nGold ingredients:")
        for ing in g["ingredients"]:
            amt = "—" if ing["amount"] is None else f"{ing['amount']} {ing['unit'] or ''}".strip()
            flag = "  [VAGUE]" if ing["vague"] else ""
            print(f"  {ing['ingredient']:<24} {amt:<10}{flag}")
            print(f"      ↳ \"{ing['original_phrase']}\"")
        print()


def score_recipe(result: dict, fx_id: str):
    """Return per-recipe metrics dict."""
    invented = 0
    invented_items = []
    preserved = 0
    total = 0
    mapped = 0
    mappable = 0

    transcript_lower = next(f["transcript"] for f in FIXTURES if f["id"] == fx_id).lower()

    for ing in result.get("ingredients", []):
        total += 1
        phrase = (ing.get("original_phrase") or "").lower()
        amount = ing.get("amount", None)

        # RULE 1: vague cue present but a number was produced => invented
        is_vague_phrase = any(cue in phrase for cue in VAGUE_CUES)
        if is_vague_phrase and amount is not None:
            invented += 1
            invented_items.append(ing.get("ingredient", "?"))

        # RULE 2: original phrase is non-empty and actually echoes the source
        if phrase.strip():
            # crude check: at least one content word of the phrase is in transcript
            words = [w for w in phrase.split() if len(w) > 2]
            if any(w in transcript_lower for w in words):
                preserved += 1

        # RULE 3: code-switch mapping
        eng = (ing.get("ingredient") or "").lower()
        for src, tgt in EXPECTED_MAPPINGS.items():
            if src in phrase:
                mappable += 1
                targets = tgt if isinstance(tgt, list) else [tgt]
                if any(t in eng for t in targets):
                    mapped += 1
                break

    return {
        "invented": invented,
        "invented_items": invented_items,
        "preserved": preserved,
        "total": total,
        "mapped": mapped,
        "mappable": mappable,
    }


def run(model: str):
    try:
        import anthropic
    except ImportError:
        print("Install the SDK first:  pip install anthropic --break-system-packages")
        sys.exit(1)

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Set your key first:  export ANTHROPIC_API_KEY=sk-ant-...")
        sys.exit(1)

    client = anthropic.Anthropic()
    totals = {"invented": 0, "preserved": 0, "total": 0, "mapped": 0, "mappable": 0}

    for fx in FIXTURES:
        print("=" * 70)
        print(f"{fx['title_hint']}  ({fx['id']})  via {model}")
        print("=" * 70)
        try:
            resp = client.messages.create(
                model=model,
                max_tokens=2000,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": build_user_prompt(fx["transcript"])}],
            )
            raw = "".join(b.text for b in resp.content if b.type == "text").strip()
            raw = raw.replace("```json", "").replace("```", "").strip()
            result = json.loads(raw)
        except json.JSONDecodeError:
            print("  FAILED to parse JSON. Raw output:\n", raw[:500])
            continue
        except Exception as e:
            print(f"  API error: {e}")
            continue

        m = score_recipe(result, fx["id"])
        for k in totals:
            totals[k] += m[k]

        verdict = "OK" if m["invented"] == 0 else f"!! {m['invented']} INVENTED"
        print(f"  ingredients: {m['total']}")
        print(f"  invented numbers: {m['invented']}   {verdict}")
        if m["invented_items"]:
            print(f"    offenders: {', '.join(m['invented_items'])}")
        print(f"  phrase preserved: {m['preserved']}/{m['total']}")
        print(f"  code-switch mapped: {m['mapped']}/{m['mappable']}")
        print()

    print("#" * 70)
    print("TOTALS")
    print("#" * 70)
    pres = f"{totals['preserved']}/{totals['total']}" if totals["total"] else "n/a"
    mapp = f"{totals['mapped']}/{totals['mappable']}" if totals["mappable"] else "n/a"
    print(f"  TOTAL invented numbers : {totals['invented']}   <-- must be 0")
    print(f"  phrase preservation    : {pres}")
    print(f"  code-switch mapping    : {mapp}")
    print()
    if totals["invented"] == 0:
        print("  WALL HOLDS. Extraction did not invent precision. Path B is viable")
        print("  on these fixtures. Now test it on a REAL transcript before betting.")
    else:
        print("  WALL CRACKS. The model invented numbers from vague input.")
        print("  Tune the prompt and rerun, or ship Path B (tracker) this week.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--show", action="store_true", help="read gold outputs, no API key")
    ap.add_argument("--run", action="store_true", help="call a real model and score")
    ap.add_argument("--model", default=DEFAULT_MODEL, help="model string to call")
    args = ap.parse_args()

    if args.show:
        show()
    elif args.run:
        run(args.model)
    else:
        ap.print_help()
