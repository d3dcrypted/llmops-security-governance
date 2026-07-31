from dataclasses import dataclass
import re

@dataclass(frozen=True)
class Decision:
    allowed: bool
    redacted_text: str
    reasons: tuple[str, ...]

def inspect(text: str) -> Decision:
    reasons = []
    redacted = re.sub(r"\b[\w.+-]+@[\w.-]+\.\w+\b", "[REDACTED_EMAIL]", text)
    if redacted != text: reasons.append("email_redacted")
    if re.search(r"ignore\s+(all\s+)?previous\s+instructions", text, re.I):
        reasons.append("prompt_injection_pattern")
    return Decision("prompt_injection_pattern" not in reasons, redacted, tuple(reasons))
