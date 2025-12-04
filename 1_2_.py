import re
import os

input_filename = "1_/1_1_.txt"
output_filename = "1_/1_2_.txt"

if not os.path.exists(input_filename):
    print(f"Error: File '{input_filename}' not found!")
    exit(1)

with open(input_filename, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Processing: {input_filename}")

# === Loop 1: Replace \n\n0 → \n\nb (repeat until none left) ===
while True:
    new_content, count = re.subn(r'\n\n0', '\n\nb', content)
    if count == 0:
        break
    content = new_content
    print(f"Loop 1: Replaced {count} occurrence(s) of '\\n\\n0' → '\\n\\nb'")

# === Loop 2: Remove all 0, 1, 2 digits ===
removed_count = len(re.findall(r'[012]', content))
content = re.sub(r'[012]', '', content)
print(f"Loop 2: Removed {removed_count} digits (0,1,2)")

# === Final: Collapse blank lines BUT preserve leading newline if exists ===
print("Final step: Collapsing blank lines (but keep leading \\n if present)...")

# Check if file originally started with a newline
starts_with_newline = content.startswith('\n')

# Replace any sequence of 2+ newlines with exactly ONE newline
content = re.sub(r'\n{2,}', '\n', content)

# If it started with \n, make sure it still does (re-add if stripped)
if starts_with_newline and not content.startswith('\n'):
    content = '\n' + content

# Optional: ensure it ends with exactly one newline (standard)
if content and content[-1] != '\n':
    content += '\n'
elif content.count('\n') > 1 and content.endswith('\n\n'):
    content = content.rstrip('\n') + '\n'  # normalize trailing

with open(output_filename, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Done! → Saved as {output_filename}")
print(f"   Preserved leading blank line: {'Yes' if content.startswith('\n') else 'No'}")