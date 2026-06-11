"""
Five realistic phone-call recipe transcripts.

These mimic how a desi parent actually transmits a recipe by phone:
- code-switched (Urdu/Hindi/Punjabi + English)
- vague measurements ("andaza se", "a fistful", "till it smells right")
- no step numbers, rambling, asides
- some real numbers mixed in ("ek pyaaz", "do tamatar")

The whole point of the test: the extractor must keep the vague ones vague
(amount = null) and never invent a gram count, while still mapping
code-switched ingredient names for the grocery list.
"""

FIXTURES = [
    {
        "id": "karahi",
        "title_hint": "Chicken Karahi",
        "transcript": (
            "Beta listen, chicken karahi bahut easy hai. Tu pehle ek kilo "
            "chicken le le, boneless nahi, with bones, taste better hota hai. "
            "Phir oil daal, thoda zyada, andaza se, jab tak garam ho jaye. "
            "Ek pyaaz, do tamatar, kaat ke. Adrak lehsun ka paste, ek chamach. "
            "Haldi just a little, andaza se, namak apne hisaab se. Laal mirch "
            "thori si, jitni tu kha sake. Cook karte raho jab tak oil upar "
            "aa jaye. Last mein dhaniya daal dena, fresh wala. Bas ho gaya."
        ),
    },
    {
        "id": "daal",
        "title_hint": "Masoor Daal",
        "transcript": (
            "Daal toh tu bana hi sakti hai akeli. Ek cup masoor daal dho le "
            "achi tarah. Paani daal, do cup ke karib, andaza se, daal doob "
            "jaye bas. Haldi half teaspoon, namak thora. Ubaalne do jab tak "
            "soft na ho jaye, maybe twenty minutes. Phir tarka: ghee garam "
            "kar, zeera daal, ek pyaaz golden tak fry kar, lehsun ke do "
            "tukde. Daal pe daal de. Dhaniya upar se. Khatam."
        ),
    },
    {
        "id": "biryani",
        "title_hint": "Chicken Biryani",
        "transcript": (
            "Biryani thora time leti hai par mushkil nahi. Chawal le, basmati, "
            "do cup, bhigo de pehle. Chicken aadha kilo. Pyaaz teen, patle "
            "kaat ke, brown kar lena achi tarah, yeh important hai. Dahi ek "
            "cup, ginger garlic paste, biryani masala ek packet ya andaza se "
            "agar khula hai. Tamatar do. Aloo bhi daal sakti hai agar pasand "
            "hai, do char tukde. Layer kar ke dum pe rakh dena, low flame, "
            "till khushboo aaye. Saffron milk upar agar hai toh."
        ),
    },
    {
        "id": "sabzi",
        "title_hint": "Aloo Gobi",
        "transcript": (
            "Aloo gobi roz ka khana hai. Ek gobi, kaat ke. Do teen aloo, "
            "cube kar ke. Tel mein zeera daal, phir pyaaz ek, adrak thora. "
            "Haldi, dhaniya powder, namak, sab andaza se daal de tu ab tak "
            "seekh gayi hogi. Tamatar ek. Aloo gobi daal, dhak ke pakao till "
            "soft. Garam masala chutki bhar last mein. Hari mirch agar teekha "
            "chahiye. Dhaniya garnish."
        ),
    },
    {
        "id": "kheer",
        "title_hint": "Kheer",
        "transcript": (
            "Kheer toh sweet hai meetha, easy. Doodh ek liter, full cream "
            "lena, warna taste nahi aata. Chawal mutthi bhar, dho ke. Doodh "
            "ubaal, chawal daal, dheemi aanch pe pakao stirring karte raho "
            "warna jal jayega, long time lagta hai patience chahiye. Cheeni "
            "apne taste se, main thori kam daalti hun. Elaichi do teen, "
            "kuchli hui. Badam pista upar se garnish, andaza se. Thanda "
            "kar ke khao, better lagta hai."
        ),
    },
]
