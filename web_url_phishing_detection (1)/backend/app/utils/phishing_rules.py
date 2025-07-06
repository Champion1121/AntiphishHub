
import re

def is_phishing_url(url):
    heuristics = [
        lambda u: len(u) > 75,
        lambda u: re.search(r"@|%|&|#", u),
        lambda u: re.search(r"https?://(?!www\.)", u),
        lambda u: u.count('.') > 3,
        lambda u: re.search(r"login|update|verify|secure|bank|account", u, re.IGNORECASE)
    ]
    score = sum(1 for rule in heuristics if rule(url))
    return score >= 3
