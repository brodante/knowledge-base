---
name: " Pull request template"
about: PR request template.
title: ''
labels: enhancement, feature-requested, good first issue
assignees: ''

---

---
title: "[PR] <Short Descriptive Title>"
labels: ["pull request"]
---

## 📌 Summary

<!-- Provide a brief summary of the changes introduced in this PR. -->

## 🔍 Changes

<!-- List the major changes in this PR, such as new pages, updates to existing pages, or fixes. -->

- [ ] Added a new knowledge base page: `<Page Title>`  
- [ ] Updated an existing page: `<Page Title>`  
- [ ] Fixed formatting, typos, or broken links  
- [ ] Other: `<Describe the change>`

## ✅ Validation Checklist

- [ ] The new page follows the required front matter format:
  ```yaml
  ---
  layout: default
  title: "Page Title"
  permalink: /path/to/page/
  ---
  ```
- [ ] The `permalink` matches the file's location in the repository.
- [ ] The content follows the contribution guidelines (`CONTRIBUTING.md`).
- [ ] I have run the validation script (`.github/scripts/validate_pages.py`) and fixed any reported issues.

## 🔗 Related Issues

<!-- If this PR addresses any existing issues, link them here. -->
Fixes #ISSUE_ID  

## 💡 Additional Notes

<!-- Add any additional context, screenshots, or considerations. -->
