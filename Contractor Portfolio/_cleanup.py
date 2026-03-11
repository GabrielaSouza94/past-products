"""
Cleanup script: replace DevSavant with 'the contractor' and strip emojis.
"""

import os
import re

PORTFOLIO_DIR = os.path.dirname(os.path.abspath(__file__))

DEVSAVANT_REPLACEMENTS = [
    ("DevSavant Applied Engineering", "The Contractor"),
    ("DevSavant - Product Engineering", "The Contractor"),
    ("DevSavant Product Engineering", "The Contractor"),
    ("DevSavant's", "The contractor's"),
    ("DevSavant", "The Contractor"),
    ("devsavant", "the contractor"),
    ("Devsavant", "The Contractor"),
]

EMOJI_PATTERN = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map
    "\U0001F1E0-\U0001F1FF"  # flags
    "\U0001F900-\U0001F9FF"  # supplemental symbols
    "\U0001FA00-\U0001FA6F"  # chess symbols
    "\U0001FA70-\U0001FAFF"  # symbols extended-A
    "\U00002702-\U000027B0"  # dingbats
    "\U000024C2-\U0001F251"  # enclosed characters
    "\U0000FE0F"             # variation selector
    "\U0000200D"             # zero width joiner
    "\U00002600-\U000026FF"  # misc symbols (but preserve some)
    "\U00002B50"             # star
    "\U00002B05-\U00002B07"  # arrows
    "\U00002934-\U00002935"  # arrows
    "\U00003030"             # wavy dash
    "\U0000303D"             # part alternation mark
    "\U00003297"             # circled ideograph congratulation
    "\U00003299"             # circled ideograph secret
    "\U0000200B"             # zero width space
    "]+",
    flags=re.UNICODE,
)

# Characters we want to KEEP (not emojis):
# → (U+2192) - right arrow, used in flow descriptions
# — (U+2014) - em dash
# – (U+2013) - en dash
# " " (U+201C, U+201D) - curly quotes
# ' ' (U+2018, U+2019) - curly apostrophes
# … (U+2026) - ellipsis
# ← ↑ ↓ (U+2190-U+2193) - directional arrows
# • (U+2022) - bullet
# × (U+00D7) - multiplication sign
# ≥ ≤ (comparison operators)

def strip_emojis(text: str) -> str:
    return EMOJI_PATTERN.sub("", text)


def process_files():
    count = 0
    for root, dirs, files in os.walk(PORTFOLIO_DIR):
        dirs[:] = [d for d in dirs if not d.startswith('_') and not d.startswith('.')]
        for fname in files:
            if not fname.endswith('.md'):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                original = f.read()

            content = original

            for old, new in DEVSAVANT_REPLACEMENTS:
                content = content.replace(old, new)

            content = strip_emojis(content)

            if content != original:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                print(f"  Updated: {os.path.relpath(fpath, PORTFOLIO_DIR)}")
            else:
                print(f"  No changes: {os.path.relpath(fpath, PORTFOLIO_DIR)}")

    print(f"\nDone. {count} files updated.")


if __name__ == '__main__':
    process_files()
