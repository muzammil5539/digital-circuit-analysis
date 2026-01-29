# Contributing to Digital Circuit Analysis

Thank you for your interest in contributing to the Digital Circuit Analysis project! We welcome contributions from the community.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Pull Requests](#pull-requests)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Message Guidelines](#commit-message-guidelines)

## Code of Conduct

This project adheres to a code of conduct that all contributors are expected to follow. Please be respectful and constructive in all interactions.

## How Can I Contribute?

### Reporting Bugs

If you find a bug, please create an issue on GitHub with the following information:

- **Clear title and description**: Explain what the bug is
- **Steps to reproduce**: List the exact steps to reproduce the issue
- **Expected behavior**: Describe what you expected to happen
- **Actual behavior**: Describe what actually happened
- **Environment**: Include your Python version, OS, and any relevant dependencies
- **Circuit file**: If applicable, attach the circuit file that caused the issue

### Suggesting Enhancements

We welcome suggestions for new features or improvements. When suggesting an enhancement:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the suggested enhancement
- **Explain why this enhancement would be useful** to most users
- **List any similar features** in other projects, if applicable

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the coding standards below
3. **Test your changes** thoroughly
4. **Update documentation** if you've changed functionality
5. **Write clear commit messages** following our guidelines
6. **Submit a pull request** with a comprehensive description of changes

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/muzammil5539/digital-circuit-analysis.git
   cd digital-circuit-analysis
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application to verify setup:
   ```bash
   python src/main.py
   ```

## Coding Standards

- **Python Style Guide**: Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- **Docstrings**: Use docstrings for all public modules, functions, classes, and methods
- **Type Hints**: Add type hints where appropriate to improve code clarity
- **Comments**: Write clear, concise comments explaining complex logic
- **Naming Conventions**:
  - Use `snake_case` for functions and variables
  - Use `PascalCase` for class names
  - Use `UPPER_CASE` for constants

## Commit Message Guidelines

Write clear and meaningful commit messages:

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests when applicable
- For complex changes, provide a detailed description after the first line

### Example Commit Messages

```
Add support for XOR gate in circuit analysis

- Implement XOR gate delay calculation
- Update circuit parser to recognize XOR type
- Add XOR gate to visualization
- Include test cases for XOR circuits

Fixes #123
```

## Questions?

If you have questions about contributing, feel free to open an issue with the "question" label.

Thank you for contributing to Digital Circuit Analysis! 🚀
