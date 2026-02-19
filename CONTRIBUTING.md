# Contributing to SandboxEnvironment

Thank you for your interest in contributing to the SandboxEnvironment project! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please review our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before participating. We are committed to providing a welcoming and inclusive environment for all contributors.

## Getting Started

### Prerequisites

- Git installed and configured
- GitHub account
- Familiarity with this sandbox environment (review [README.md](README.md))

### Setting Up Your Development Environment

1. **Fork the repository** on GitHub
2. **Clone your fork locally**:
   ```bash
   git clone https://github.com/your-username/SandboxEnvironment.git
   cd SandboxEnvironment
   ```

3. **Create a branch** for your work:
   ```bash
   git checkout -b feature/your-feature-name
   ```
   or
   ```bash
   git checkout -b fix/your-bug-fix
   ```

4. **Make your changes** following the guidelines below

## Contribution Types

### Reporting Issues

- **Search first**: Check if the issue already exists
- **Provide details**: Include steps to reproduce, expected behavior, and actual behavior
- **Environment info**: Specify OS, relevant software versions, and configurations
- **Use templates**: Follow the bug report template when available

### Submitting Code Changes

1. **Keep changes focused**: Each PR should address one feature or fix
2. **Write clear commit messages**:
   ```
   Short description (50 characters or less)
   
   More detailed explanation if necessary, wrapped at 72 characters.
   Include issue numbers like "Fixes #123" if applicable.
   ```

3. **Follow coding standards**:
   - Use the provided `.editorconfig` for consistent formatting
   - Follow existing code style in the repository
   - Keep the codebase clean and maintainable

4. **Test your changes**:
   - Verify your changes work as intended
   - Check for any breaking changes
   - Run pre-commit hooks: `pre-commit run --all-files`

5. **Update documentation**:
   - Update README.md if behavior changes
   - Add comments for complex logic
   - Update CHANGELOG.md if applicable

### Documentation Improvements

- Fix typos and clarifications
- Improve examples
- Enhance existing documentation
- Add missing information

## Pull Request Process

1. **Before submitting**:
   - Rebase on the latest `Main` branch
   - Ensure all tests pass
   - Verify `.editorconfig` compliance

2. **Create your PR**:
   - Use the pull request template if available
   - Write a clear title and description
   - Reference related issues using `#issue-number`
   - Link to any relevant discussions

3. **During review**:
   - Be open to feedback
   - Request changes if needed
   - Respond to maintainer comments promptly

4. **After approval**:
   - Maintainers will merge your PR
   - Your contribution will be acknowledged

## Coding Guidelines

### General Principles

- Write clear, readable code
- Add comments for complex sections
- Keep functions/methods focused and single-purpose
- Avoid introducing unnecessary dependencies

### Pre-commit Hooks

This repository uses pre-commit hooks to maintain code quality:

```bash
# Run pre-commit hooks
pre-commit run --all-files

# Install hooks for automatic checks on commit
pre-commit install
```

Hooks check for:
- Secret leaks (gitleaks)
- Trailing whitespace
- End-of-file fixes

## Commit Message Guidelines

Follow the conventional commit format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**: feat, fix, docs, style, refactor, perf, test, chore

**Example**:
```
feat(sandbox): add new testing capability

This adds a new feature that enables developers to...

Fixes #42
```

## Licensing

By contributing to this repository, you agree that your contributions will be licensed under the same license as the project ([MIT License](LICENSE)).

## Questions or Need Help?

- Open an issue with your question
- Check existing issues and discussions
- Contact the maintainers through GitHub discussions

## Recognition

Contributors are valued members of our community! Thank you for helping improve SandboxEnvironment.

---

**Last Updated**: February 2026

