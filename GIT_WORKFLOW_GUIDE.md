# Git Workflow Guide for Students

This guide explains how to work with Git and GitHub for this research project. It's designed to help students understand and follow best practices for collaborative development.

## 🌳 Branch Structure

Our repository uses a **protected branch workflow** with the following structure:

```
main (protected)
├── development (main development branch)
    ├── feature/student-name-feature-description
    ├── feature/another-feature
    └── bugfix/fix-description
```

### Branch Descriptions

- **`main`**: Production-ready code. **Protected** - no direct pushes allowed
- **`development`**: Integration branch for ongoing development work
- **`feature/*`**: Individual feature branches created from `development`
- **`bugfix/*`**: Bug fix branches created from `development`

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Research-Group-IxD/convai-eindhoven-governance.git
cd convai-eindhoven-governance
```

### 2. Set Up Your Development Environment
```bash
# Switch to development branch
git checkout development

# Make sure you have the latest changes
git pull origin development
```

## 📝 Development Workflow

### Step 1: Create a Feature Branch
Always create a new branch for your work. Use descriptive names:

```bash
# Create and switch to a new feature branch
git checkout -b feature/your-name-descriptive-feature-name

# Examples:
git checkout -b feature/sarah-add-video-carousel
git checkout -b feature/mike-update-citation-format
git checkout -b bugfix/lisa-fix-mobile-layout
```

### Step 2: Make Your Changes
Work on your feature, making regular commits with clear messages:

```bash
# Stage your changes
git add .

# Commit with a descriptive message
git commit -m "Add responsive video carousel component

- Implemented mobile-friendly video player
- Added touch gesture support
- Updated CSS for better mobile experience"
```

### Step 3: Push Your Branch
```bash
# Push your feature branch to GitHub
git push origin feature/your-name-descriptive-feature-name
```

### Step 4: Create a Pull Request
1. Go to the GitHub repository
2. Click "Compare & pull request" (GitHub will show this after you push)
3. Set the base branch to `development` (not `main`)
4. Fill out the pull request template:
   - **Title**: Brief description of your changes
   - **Description**: What you changed and why
   - **Testing**: How you tested your changes

### Step 5: Code Review & Merge
- Wait for review from project maintainers
- Address any feedback by making additional commits
- Once approved, your changes will be merged into `development`

## 🔄 Keeping Your Branch Updated

While working on long-running features, regularly sync with the development branch:

```bash
# Switch to development branch
git checkout development

# Pull latest changes
git pull origin development

# Switch back to your feature branch
git checkout feature/your-feature-name

# Merge development into your branch
git merge development
```

## 📚 Common Git Commands Cheat Sheet

### Checking Status
```bash
git status                    # See current status
git branch                    # List local branches
git branch -r                 # List remote branches
git log --oneline            # See commit history
```

### Working with Changes
```bash
git add filename             # Stage specific file
git add .                    # Stage all changes
git commit -m "message"      # Commit with message
git push origin branch-name  # Push to remote branch
```

### Branch Management
```bash
git checkout branch-name     # Switch to existing branch
git checkout -b new-branch   # Create and switch to new branch
git branch -d branch-name    # Delete local branch (after merge)
git push origin --delete branch-name  # Delete remote branch
```

## ⚠️ Important Rules

### 🚫 DON'T:
- **Never push directly to `main`** - it's protected and will be rejected
- Don't work directly on the `development` branch for your features
- Don't force push (`git push --force`) to shared branches
- Don't commit large binary files without checking with maintainers

### ✅ DO:
- Always create feature branches from `development`
- Write clear, descriptive commit messages
- Test your changes before creating a pull request
- Ask for help if you're unsure about something

## 🆘 Troubleshooting Common Issues

### "Your branch is behind origin/development"
```bash
git checkout development
git pull origin development
git checkout your-feature-branch
git merge development
```

### "Merge conflict"
1. Open the conflicted files
2. Look for conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
3. Resolve conflicts by choosing the correct code
4. Remove conflict markers
5. Stage and commit the resolved files:
```bash
git add .
git commit -m "Resolve merge conflict"
```

### "I committed to the wrong branch"
If you committed to `development` instead of a feature branch:
```bash
# Create a new branch from current state
git checkout -b feature/your-feature-name

# Go back to development
git checkout development

# Reset development to match remote
git reset --hard origin/development
```

### "I need to undo my last commit"
```bash
# Undo last commit but keep changes
git reset --soft HEAD~1

# Undo last commit and discard changes (be careful!)
git reset --hard HEAD~1
```

## 🎯 Best Practices for Students

### Commit Messages
Use the format: `Type: Brief description`

**Types:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Formatting, missing semi colons, etc.
- `refactor:` Code restructuring
- `test:` Adding tests

**Examples:**
```bash
git commit -m "feat: Add mobile navigation menu"
git commit -m "fix: Resolve carousel autoplay issue on iOS"
git commit -m "docs: Update installation instructions"
```

### Pull Request Descriptions
Always include:
- **What** you changed
- **Why** you made the change
- **How** to test the changes
- Screenshots (for UI changes)

### Code Review
When reviewing others' code:
- Be constructive and helpful
- Explain why you suggest changes
- Ask questions if something is unclear
- Approve when you're satisfied with the changes

## 🔗 Useful Resources

- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Interactive Git Tutorial](https://learngitbranching.js.org/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

## 💬 Getting Help

If you're stuck:
1. Check this guide first
2. Search for your error message online
3. Ask a teammate or project maintainer
4. Create an issue in the repository with the `help wanted` label

Remember: Everyone makes mistakes with Git. The important thing is to learn from them and ask for help when needed!

---

*This guide is part of the Research Group IxD project template. For questions about this workflow, contact the project maintainers.*
