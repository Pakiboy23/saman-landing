"""
Hand-authored "gold" outputs: what correct extraction looks like on each
fixture. This is the bar. You can read these with `harness.py --show` to judge
quality before ever wiring an API key.

The key thing to notice: every vague item has amount=null, vague=true, and its
original_phrase preserved. Every code-switched name is mapped. Spoken numbers
("ek pyaaz" -> 1) are kept as real amounts.
"""

GOLD = {
    "karahi": {
        "title": "Chicken Karahi",
        "attribution": None,
        "ingredients": [
            {"ingredient": "chicken (bone-in)", "original_phrase": "ek kilo chicken, with bones", "amount": 1, "unit": "kg", "vague": False},
            {"ingredient": "oil", "original_phrase": "oil, thoda zyada, andaza se", "amount": None, "unit": None, "vague": True},
            {"ingredient": "onion", "original_phrase": "ek pyaaz", "amount": 1, "unit": "each", "vague": False},
            {"ingredient": "tomato", "original_phrase": "do tamatar", "amount": 2, "unit": "each", "vague": False},
            {"ingredient": "ginger garlic paste", "original_phrase": "adrak lehsun ka paste, ek chamach", "amount": 1, "unit": "tbsp", "vague": False},
            {"ingredient": "turmeric", "original_phrase": "haldi just a little, andaza se", "amount": None, "unit": None, "vague": True},
            {"ingredient": "salt", "original_phrase": "namak apne hisaab se", "amount": None, "unit": None, "vague": True},
            {"ingredient": "red chili", "original_phrase": "laal mirch thori si, jitni tu kha sake", "amount": None, "unit": None, "vague": True},
            {"ingredient": "cilantro", "original_phrase": "dhaniya, fresh wala", "amount": None, "unit": None, "vague": True},
        ],
        "steps": [
            "Heat oil until hot.",
            "Add chopped onion and tomato, and ginger garlic paste.",
            "Add chicken with turmeric, salt, and red chili.",
            "Cook until the oil rises to the top.",
            "Finish with fresh cilantro.",
        ],
        "notes": "Bone-in chicken tastes better. Chili to your own tolerance.",
    },
    "daal": {
        "title": "Masoor Daal",
        "attribution": None,
        "ingredients": [
            {"ingredient": "masoor daal (red lentils)", "original_phrase": "ek cup masoor daal", "amount": 1, "unit": "cup", "vague": False},
            {"ingredient": "water", "original_phrase": "do cup ke karib, andaza se", "amount": None, "unit": None, "vague": True},
            {"ingredient": "turmeric", "original_phrase": "haldi half teaspoon", "amount": 0.5, "unit": "tsp", "vague": False},
            {"ingredient": "salt", "original_phrase": "namak thora", "amount": None, "unit": None, "vague": True},
            {"ingredient": "ghee", "original_phrase": "ghee garam kar", "amount": None, "unit": None, "vague": True},
            {"ingredient": "cumin", "original_phrase": "zeera daal", "amount": None, "unit": None, "vague": True},
            {"ingredient": "onion", "original_phrase": "ek pyaaz golden tak fry kar", "amount": 1, "unit": "each", "vague": False},
            {"ingredient": "garlic", "original_phrase": "lehsun ke do tukde", "amount": 2, "unit": "clove", "vague": False},
            {"ingredient": "cilantro", "original_phrase": "dhaniya upar se", "amount": None, "unit": None, "vague": True},
        ],
        "steps": [
            "Rinse the lentils well.",
            "Add water until the daal is just submerged, with turmeric and salt.",
            "Boil until soft, roughly twenty minutes.",
            "For the tarka: heat ghee, add cumin, fry onion until golden, add garlic.",
            "Pour tarka over the daal and garnish with cilantro.",
        ],
        "notes": None,
    },
    "biryani": {
        "title": "Chicken Biryani",
        "attribution": None,
        "ingredients": [
            {"ingredient": "basmati rice", "original_phrase": "chawal, basmati, do cup", "amount": 2, "unit": "cup", "vague": False},
            {"ingredient": "chicken", "original_phrase": "chicken aadha kilo", "amount": 0.5, "unit": "kg", "vague": False},
            {"ingredient": "onion", "original_phrase": "pyaaz teen, patle kaat ke, brown kar lena", "amount": 3, "unit": "each", "vague": False},
            {"ingredient": "yogurt", "original_phrase": "dahi ek cup", "amount": 1, "unit": "cup", "vague": False},
            {"ingredient": "ginger garlic paste", "original_phrase": "ginger garlic paste", "amount": None, "unit": None, "vague": True},
            {"ingredient": "biryani masala", "original_phrase": "biryani masala ek packet ya andaza se agar khula hai", "amount": None, "unit": None, "vague": True},
            {"ingredient": "tomato", "original_phrase": "tamatar do", "amount": 2, "unit": "each", "vague": False},
            {"ingredient": "potato", "original_phrase": "aloo bhi daal sakti hai, do char tukde", "amount": None, "unit": None, "vague": True},
            {"ingredient": "saffron milk", "original_phrase": "saffron milk upar agar hai toh", "amount": None, "unit": None, "vague": True},
        ],
        "steps": [
            "Soak the basmati rice.",
            "Brown the sliced onions well; this matters.",
            "Cook chicken with yogurt, ginger garlic paste, biryani masala, and tomato.",
            "Add potatoes if you like.",
            "Layer and cook on dum over low flame until fragrant.",
            "Top with saffron milk if available.",
        ],
        "notes": "Browning the onions well is important. Potato and saffron are optional.",
    },
    "sabzi": {
        "title": "Aloo Gobi",
        "attribution": None,
        "ingredients": [
            {"ingredient": "cauliflower", "original_phrase": "ek gobi, kaat ke", "amount": 1, "unit": "each", "vague": False},
            {"ingredient": "potato", "original_phrase": "do teen aloo, cube kar ke", "amount": None, "unit": None, "vague": True},
            {"ingredient": "oil", "original_phrase": "tel mein", "amount": None, "unit": None, "vague": True},
            {"ingredient": "cumin", "original_phrase": "zeera daal", "amount": None, "unit": None, "vague": True},
            {"ingredient": "onion", "original_phrase": "pyaaz ek", "amount": 1, "unit": "each", "vague": False},
            {"ingredient": "ginger", "original_phrase": "adrak thora", "amount": None, "unit": None, "vague": True},
            {"ingredient": "turmeric", "original_phrase": "haldi, andaza se", "amount": None, "unit": None, "vague": True},
            {"ingredient": "coriander powder", "original_phrase": "dhaniya powder, andaza se", "amount": None, "unit": None, "vague": True},
            {"ingredient": "salt", "original_phrase": "namak, andaza se", "amount": None, "unit": None, "vague": True},
            {"ingredient": "tomato", "original_phrase": "tamatar ek", "amount": 1, "unit": "each", "vague": False},
            {"ingredient": "garam masala", "original_phrase": "garam masala chutki bhar", "amount": None, "unit": None, "vague": True},
            {"ingredient": "green chili", "original_phrase": "hari mirch agar teekha chahiye", "amount": None, "unit": None, "vague": True},
            {"ingredient": "cilantro", "original_phrase": "dhaniya garnish", "amount": None, "unit": None, "vague": True},
        ],
        "steps": [
            "Cut the cauliflower and cube the potatoes.",
            "Heat oil, add cumin, then onion and a little ginger.",
            "Add turmeric, coriander powder, and salt to taste.",
            "Add tomato, then the potato and cauliflower.",
            "Cover and cook until soft.",
            "Finish with a pinch of garam masala, green chili if you want heat, and cilantro.",
        ],
        "notes": "Season by feel; she expects you know the amounts by now.",
    },
    "kheer": {
        "title": "Kheer",
        "attribution": None,
        "ingredients": [
            {"ingredient": "milk", "original_phrase": "doodh ek liter, full cream", "amount": 1, "unit": "liter", "vague": False},
            {"ingredient": "rice", "original_phrase": "chawal mutthi bhar", "amount": None, "unit": None, "vague": True},
            {"ingredient": "sugar", "original_phrase": "cheeni apne taste se", "amount": None, "unit": None, "vague": True},
            {"ingredient": "cardamom", "original_phrase": "elaichi do teen, kuchli hui", "amount": None, "unit": None, "vague": True},
            {"ingredient": "almonds and pistachios", "original_phrase": "badam pista upar se garnish, andaza se", "amount": None, "unit": None, "vague": True},
        ],
        "steps": [
            "Use full cream milk or the taste won't come through.",
            "Rinse the rice.",
            "Boil the milk, add rice, and cook on low heat, stirring so it doesn't burn.",
            "Add sugar to taste and crushed cardamom.",
            "Garnish with almonds and pistachios.",
            "Chill before serving; it tastes better cold.",
        ],
        "notes": "Takes a long time and needs patience. She uses less sugar than standard.",
    },
}
