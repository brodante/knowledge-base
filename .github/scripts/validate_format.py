import os
import yaml

REQUIRED_FIELDS = {"layout", "title", "permalink"}
errors = []

def is_valid_page(file_path):
	with open(file_path, "r", encoding="utf-8") as f:
		content = f.read()

	# Ensure front matter exists
	if not content.startswith("---"):
		errors.append(f"❌ {file_path}: Missing front matter.")
		return False

	# Extract front matter
	try:
		front_matter = yaml.safe_load(content.split("---")[1])
	except yaml.YAMLError:
		errors.append(f"❌ {file_path}: Invalid YAML in front matter.")
		return False

	# Check required fields
	if not REQUIRED_FIELDS.issubset(front_matter.keys()):
		errors.append(f"❌ {file_path}: Missing required fields {REQUIRED_FIELDS}.")
		return False

	# Validate permalink matches file path
	expected_path = front_matter["permalink"].strip("/")
	actual_path = os.path.splitext(file_path.replace("\\", "/"))[0].strip("./")
	
	if expected_path != actual_path:
		errors.append(f"❌ {file_path}: Permalink mismatch. Expected '{expected_path}', found '{actual_path}'.")
		return False

	return True

def main():
	markdown_files = []
	for root, _, files in os.walk("."):
		for file in files:
			if file.endswith(".md"):
				markdown_files.append(os.path.join(root, file))

	all_valid = all(is_valid_page(file) for file in markdown_files)

	if not all_valid:
		print("\n".join(errors))
		exit(1)

	print("✅ All pages follow the required format.")
	exit(0)

if __name__ == "__main__":
	main()
