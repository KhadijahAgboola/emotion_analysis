# Simple scoring logic (to simulate Excel formula)
def get_emotion(enjoyment, excitement, power):
    if enjoyment > 70 and excitement > 70 and power > 70:
        return "Euphoric", "Channel this energy into creative action", [
            "Start a new personal project today.",
            "Write down your big idea and make a 3-step plan."
        ]
    elif enjoyment < 30 and power < 30:
        return "Anxious", "Predictability, permission to be imperfect", [
            "Make a version 1.0 with low risk to get started.",
            "Remind yourself that it’s okay to be messy."
        ]
    else:
        return "Neutral", "Reflection and grounding", [
            "Take 10 minutes to journal your thoughts.",
            "Do a grounding breathing exercise."
        ]
