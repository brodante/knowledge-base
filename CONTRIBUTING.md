# Contributing to Dante's Knowledge Base

Thank you for your interest in contributing to **Dante's Knowledge Base**! This guide will help you get started and ensure that your contributions align with the project's structure and quality standards.

## 🚀 Getting Started
1. **Fork the Repository**: Click the "Fork" button on the repository page to create your own copy.
2. **Clone Your Fork**: Run the following command to clone your fork locally:
   ```sh
   git clone https://github.com/brodante/knowledge-base.git
   cd knowledge-base
   ```
3. **Set Up Upstream Remote**: Add the original repository as an upstream remote:
   ```sh
   git remote add upstream https://github.com/brodante/knowledge-base.git
   ```
4. **Create a New Branch**: Always create a new branch for your contributions:
   ```sh
   git checkout -b feature/my-new-page
   ```

## 📄 Contribution Guidelines
- Contributions should be **factual, well-structured, and properly formatted**.
- Ensure your pages include a **front matter** section with:
  ```yaml
  ---
  layout: default
  title: "Page Title"
  permalink: /path/to/page/
  ---
  ```
- The `permalink` must match the relative file path inside the repository.
- Place your file in the correct directory based on its topic.
- Use **Markdown (.md)** for all content.

## ✅ Submitting a Pull Request (PR)
1. **Commit Your Changes**: Follow a meaningful commit message format:
   ```sh
   git commit -m "Add: [Short description of change]"
   ```
2. **Push Your Branch**:
   ```sh
   git push origin feature/my-new-page
   ```
3. **Open a Pull Request**:
   - Go to the original repo: [Dante's Knowledge Base](https://github.com/brodante/knowledge-base)
   - Click **New Pull Request**.
   - Select your fork and branch, then submit the PR.

## 🔍 Validation & Automated Checks
- The repository uses an **automated validation script** to check formatting.
- If your PR fails validation, check the logs in the **GitHub Actions** tab.
- Fix any issues and update your PR accordingly.

## 💡 Best Practices
- Write **clear and concise** explanations.
- Use **code blocks** where applicable.
- Ensure proper **spelling and grammar**.
- Reference sources where necessary.

## 💬 Need Help?
If you have any questions or need clarification, feel free to **open a discussion** or contact the maintainers.

Happy contributing! 🚀

