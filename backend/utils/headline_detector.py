def detect_headline(text):

    lines = text.split("\n")

    lines = [l.strip() for l in lines if l.strip()]

    if not lines:
        return "Headline not detected", ""

    headline = max(lines[:5], key=len)

    article = " ".join(lines[1:])

    return headline, article