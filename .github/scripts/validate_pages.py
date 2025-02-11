import os
import sys
import yaml

KB_ROOT = "knowledge-base"  # Adjust based on your repo structure

def validate_markdown(file_path):
	with open(file_path, "r", encoding="utf-8") as f:
		lines = f.readlines()

	# Extract front matter (between ---)
	if lines[0].strip() != "---":
		print(f"❌ {file_path}: Missing front matter start (`---`)")
		return False

	front_matter = []
	for line in lines[1:]:
		if line.strip() == "---":
			break
		front_matter.append(line)

	if not front_matter:
		print(f"❌ {file_path}: Empty or missing front matter")
		return False

	# Parse front matter as YAML
	try:
		meta = yaml.safe_load("\n".join(front_matter))
	except yaml.YAMLError as e:
		print(f"❌ {file_path}: Invalid YAML format - {e}")
		return False

	# Check for required keys
	if "layout" not in meta or "title" not in meta or "permalink" not in meta:
		print(f"❌ {file_path}: Missing required metadata (layout, title, or permalink)")
		return False

	# Validate permalink matches file structure
	relative_path = os.path.relpath(file_path, KB_ROOT)  # Get relative path
	relative_path = os.path.splitext(relative_path)[0]  # Remove .md extension
	expected_path = "/" + relative_path.replace("\\", "/") + "/"  # Convert to forward slashes & add trailing "/"

	# Debugging prints
	print(f"🔍 Debug: Checking {file_path}")
	print(f"   ➤ Expected permalink: `{expected_path}`")
	print(f"   ➤ Found permalink: `{meta['permalink']}`")

	if meta["permalink"] != expected_path:
		print(f"❌ {file_path}: Permalink mismatch! Expected `{expected_path}` but found `{meta['permalink']}`")
		return False

	print(f"✅ {file_path}: Passed validation!")
	return True

# Find all Markdown files in the repo
failed = False
for root, _, files in os.walk(KB_ROOT):
	for file in files:
		if file.endswith(".md"):
			full_path = os.path.join(root, file)
			if not validate_markdown(full_path):
				failed = True

sys.exit(1 if failed else 0)
