"""
Simple AI Chatbot
Handles: greetings, math, science facts, Pakistan history
Run: python chatbot.py
"""

import re
import math
import random


# KNOWLEDGE BASE


PAKISTAN_HISTORY = {
    "independence":     "Pakistan gained independence on 14 August 1947, after the partition of British India.",
    "founder":          "Muhammad Ali Jinnah (Quaid-e-Azam) is the founder of Pakistan. He served as its first Governor-General.",
    "capital":          "The capital of Pakistan is Islamabad. Before that, Karachi (1947–1958) and Rawalpindi (1958–1966) served as capitals.",
    "1965 war":         "The Indo-Pakistani War of 1965 lasted 17 days. It ended with the Tashkent Declaration brokered by the USSR.",
    "1971 war":         "The 1971 war led to the separation of East Pakistan, which became Bangladesh on 16 December 1971.",
    "constitution":     "Pakistan's current constitution was adopted on 14 August 1973 under Prime Minister Zulfikar Ali Bhutto.",
    "nuclear":          "Pakistan conducted nuclear tests (Chagai-I) on 28 May 1998, becoming the world's 7th nuclear state.",
    "ayub khan":        "Field Marshal Ayub Khan ruled Pakistan from 1958 to 1969 after a military coup. He introduced the 1962 constitution.",
    "bhutto":           "Zulfikar Ali Bhutto founded the PPP in 1967 and was PM from 1973–1977. He was executed in 1979 under Zia ul-Haq.",
    "zia ul haq":       "General Zia ul-Haq came to power in 1977 coup. He introduced Islamization policies and died in a plane crash in 1988.",
    "liaquat ali khan": "Liaquat Ali Khan was Pakistan's first Prime Minister. He was assassinated on 16 October 1951 in Rawalpindi.",
    "east pakistan":    "East Pakistan was the eastern wing of Pakistan from 1947 to 1971, home to the Bengali-majority population. It became Bangladesh.",
    "allama iqbal":     "Allama Iqbal is the national poet of Pakistan and the philosophical father of Pakistan. He died in 1938, before partition.",
    "partition":        "The 1947 partition of British India created two nations — India and Pakistan — and caused one of the largest mass migrations in history.",
}

SCIENCE_FACTS = {
    "gravity":          "Gravity is a fundamental force. On Earth, it accelerates objects at 9.8 m/s². Described by Newton's law and refined by Einstein's General Relativity.",
    "photosynthesis":   "Photosynthesis is the process by which plants convert CO₂ + H₂O + sunlight → glucose + oxygen.",
    "atom":             "An atom consists of a nucleus (protons + neutrons) surrounded by electrons. It's the basic unit of matter.",
    "dna":              "DNA (Deoxyribonucleic acid) carries genetic information. It has a double-helix structure discovered by Watson and Crick in 1953.",
    "speed of light":   "The speed of light in a vacuum is 299,792,458 m/s (≈3×10⁸ m/s). Nothing with mass can reach this speed.",
    "newton":           "Newton's 3 laws: (1) Inertia, (2) F=ma, (3) Every action has an equal and opposite reaction.",
    "einstein":         "Einstein's famous equation E=mc² states that energy equals mass times the speed of light squared.",
    "evolution":        "Evolution by natural selection, proposed by Charles Darwin in 1859, explains how species change over generations.",
    "periodic table":   "The periodic table organizes 118 known elements by atomic number. Created by Dmitri Mendeleev in 1869.",
    "black hole":       "A black hole is a region of spacetime where gravity is so strong that nothing — not even light — can escape.",
    "cell":             "The cell is the basic unit of life. Prokaryotes (bacteria) have no nucleus; eukaryotes (plants, animals) do.",
    "osmosis":          "Osmosis is the movement of water molecules from a region of low solute concentration to high, through a semipermeable membrane.",
    "electron":         "Electrons are negatively charged subatomic particles. They orbit the nucleus in energy levels/shells.",
    "big bang":         "The Big Bang is the prevailing cosmological theory that the universe began ~13.8 billion years ago from an extremely hot, dense state.",
}

HISTORY_ALIASES = {
    "jinnah":       "founder",
    "quaid":        "founder",
    "quaid-e-azam": "founder",
    "14 august":    "independence",
    "14th august":  "independence",
    "1947":         "independence",
    "1965":         "1965 war",
    "1971":         "1971 war",
    "bangladesh":   "1971 war",
    "iqbal":        "allama iqbal",
    "allama":       "allama iqbal",
    "liaquat":      "liaquat ali khan",
    "ayub":         "ayub khan",
    "zia":          "zia ul haq",
    "zulfikar":     "bhutto",
    "zulfiqar":     "bhutto",
    "ppp":          "bhutto",
    "chagai":       "nuclear",
    "tashkent":     "1965 war",
}

GREETINGS_IN  = ["hello", "hi", "hey", "salam", "assalam", "good morning", "good evening", "good afternoon", "what's up", "sup"]
GREETINGS_OUT = ["Hey! How can I help you today?", "Hello! Ask me about maths, science, or Pakistan history.", "Salam! What do you want to know?", "Hi there! I'm ready."]

FAREWELLS_IN  = ["bye", "goodbye", "exit", "quit", "see you", "later", "khuda hafiz"]
FAREWELLS_OUT = ["Goodbye! Come back anytime.", "Khuda Hafiz!", "See you later!", "Take care!"]

# ─────────────────────────────────────────────
# INTENT DETECTION
# ─────────────────────────────────────────────

def detect_intent(text: str) -> str:
    t = text.lower().strip()

    if any(g in t for g in GREETINGS_IN):
        return "greeting"
    if any(f in t for f in FAREWELLS_IN):
        return "farewell"

    # Math: must have digits AND operators (or explicit math commands without history context)
    history_keywords_quick = ["pakistan", "jinnah", "war", "constitution", "independence",
                               "partition", "bhutto", "zia", "iqbal", "ayub", "liaquat",
                               "quaid", "bangladesh", "nuclear", "tashkent", "chagai"]
    is_history_context = any(k in t for k in history_keywords_quick)

    if not is_history_context:
        if re.search(r'[\d]+.*[\+\-\*\/\^]|[\+\-\*\/\^].*[\d]+', t):
            return "math"
        if any(w in t for w in ["calculate", "compute", "solve", "equals", "square root", "sqrt", "factorial"]):
            if re.search(r'\d', t):
                return "math"
        # "what is 12 * 4" — math only if operator present alongside digits
        if "what is" in t and re.search(r'\d+\s*[\+\-\*\/\^]\s*\d+', t):
            return "math"

    # Pakistan history keywords
    history_keywords = ["pakistan", "jinnah", "independence", "partition", "bhutto", "zia", "1947",
                        "1965", "1971", "constitution", "nuclear", "iqbal", "ayub", "liaquat",
                        "quaid", "bangladesh", "east pakistan", "tashkent", "chagai"]
    if any(k in t for k in history_keywords):
        return "history"

    # Science keywords
    science_keywords = ["science", "physics", "biology", "chemistry", "atom", "dna", "cell",
                        "gravity", "light", "energy", "force", "evolution", "photosynthesis",
                        "element", "electron", "neutron", "proton", "molecule", "big bang",
                        "einstein", "newton", "black hole", "osmosis", "periodic"]
    if any(k in t for k in science_keywords):
        return "science"

    return "unknown"


# HANDLERS


def handle_greeting():
    return random.choice(GREETINGS_OUT)

def handle_farewell():
    return random.choice(FAREWELLS_OUT)

def safe_eval_math(expression: str) -> str:
    """Safely evaluate a math expression using only allowed names."""

    # Clean up natural language phrases
    expr = expression.lower()
    expr = re.sub(r'(calculate|compute|solve|what is|equals|the|of|=)', '', expr)
    expr = expr.replace("^", "**")
    expr = expr.replace("sqrt", "math.sqrt")
    expr = expr.replace("factorial", "math.factorial")
    expr = expr.replace("sin", "math.sin")
    expr = expr.replace("cos", "math.cos")
    expr = expr.replace("tan", "math.tan")
    expr = expr.replace("log", "math.log")
    expr = expr.replace("pi", str(math.pi))
    expr = expr.strip()

    # Whitelist: only allow safe characters
    if not re.match(r'^[\d\s\.\+\-\*\/\(\)math\.sqrtfactorialsincologtanpie]+$', expr):
        return "Sorry, I can only evaluate simple math expressions like '2 + 3 * 4' or 'sqrt(16)'."

    allowed = {"math": math, "__builtins__": {}}
    try:
        result = eval(expr, allowed)  # noqa: S307
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Division by zero!"
    except Exception:
        return "Couldn't parse that expression. Try something like: '12 * 4 + 7' or 'sqrt(144)'."

def handle_math(user_input: str) -> str:
    return safe_eval_math(user_input)

def handle_history(user_input: str) -> str:
    t = user_input.lower()
    # Check aliases first (e.g. "jinnah" → "founder")
    for alias, key in HISTORY_ALIASES.items():
        if alias in t:
            return PAKISTAN_HISTORY.get(key, "")
    # Direct key match
    for key, answer in PAKISTAN_HISTORY.items():
        if key in t:
            return answer
    # Word-level fuzzy match
    for key, answer in PAKISTAN_HISTORY.items():
        if any(word in t for word in key.split()):
            return answer
    topics = ", ".join(PAKISTAN_HISTORY.keys())
    return f"I know about these Pakistan history topics: {topics}.\nTry asking about one of them!"

def handle_science(user_input: str) -> str:
    t = user_input.lower()
    for key, answer in SCIENCE_FACTS.items():
        if key in t:
            return answer
    for key, answer in SCIENCE_FACTS.items():
        if any(word in t for word in key.split()):
            return answer
    topics = ", ".join(SCIENCE_FACTS.keys())
    return f"I know about these science topics: {topics}.\nTry asking about one of them!"

def handle_unknown():
    return ("I'm not sure about that. I can help with:\n"
            "  • Greetings\n"
            "  • Maths  (e.g. '15 * 4 + 7', 'sqrt(81)')\n"
            "  • Science  (e.g. 'What is DNA?', 'Tell me about gravity')\n"
            "  • Pakistan History  (e.g. 'Who is Jinnah?', '1971 war')")


# MAIN ROUTER


def get_response(user_input: str) -> str:
    intent = detect_intent(user_input)
    if   intent == "greeting": return handle_greeting()
    elif intent == "farewell": return handle_farewell()
    elif intent == "math":     return handle_math(user_input)
    elif intent == "history":  return handle_history(user_input)
    elif intent == "science":  return handle_science(user_input)
    else:                      return handle_unknown()


# CHAT LOOP


def main():
    print("=" * 50)
    print("  AI Chatbot  |  type 'bye' to exit")
    print("=" * 50)
    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nJarvis: Goodbye!")
            break

        if not user_input:
            continue

        response = get_response(user_input)
        print(f"Jarvis: {response}")

        if detect_intent(user_input) == "farewell":
            break

if __name__ == "__main__":
    main()
