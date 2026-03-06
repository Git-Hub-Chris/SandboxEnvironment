# Sandbox Environment

[![Dependency Review](https://github.com/Git-Hub-Chris/SandboxEnvironment/actions/workflows/dependency-review.yml/badge.svg)](https://github.com/Git-Hub-Chris/SandboxEnvironment/actions/workflows/dependency-review.yml)
[![Dependabot Updates](https://github.com/Git-Hub-Chris/SandboxEnvironment/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/Git-Hub-Chris/SandboxEnvironment/actions/workflows/dependabot/dependabot-updates)
[![Scorecard supply-chain security](https://github.com/Git-Hub-Chris/SandboxEnvironment/actions/workflows/scorecards.yml/badge.svg?branch=Main)](https://github.com/Git-Hub-Chris/SandboxEnvironment/actions/workflows/scorecards.yml)
[![CodeQL Advanced](https://github.com/Git-Hub-Chris/SandboxEnvironment/actions/workflows/codeql.yml/badge.svg?branch=Main)](https://github.com/Git-Hub-Chris/SandboxEnvironment/actions/workflows/codeql.yml)
[![Copilot code review](https://github.com/Git-Hub-Chris/SandboxEnvironment/actions/workflows/copilot-pull-request-reviewer/copilot-pull-request-reviewer/badge.svg)](https://github.com/Git-Hub-Chris/SandboxEnvironment/actions/workflows/copilot-pull-request-reviewer/copilot-pull-request-reviewer)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/11860/badge)](https://www.bestpractices.dev/projects/11860)
![Static Badge](https://img.shields.io/badge/GitHub-Sandbox%20Environment-yellow?style=flat&logo=Github&logoColor=yellow&labelColor=gray)
[![codecov](https://codecov.io/gh/Git-Hub-Chris/SandboxEnvironment/graph/badge.svg?token=U98YVITK4Y)](https://codecov.io/gh/Git-Hub-Chris/SandboxEnvironment)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18821551.svg)](https://doi.org/10.5281/zenodo.18821551)

## Introduction

A versatile and secure sandbox environment designed for experimentation, testing, and development. This multi-purpose repository serves as a playground for exploring new technologies.

The 'SandboxEnvironment' provides a structured space for safely testing APIs, tools, and workflows without impacting production systems. It integrates modern DevOps practices — including automated CI/CD pipelines, dependency management, and supply-chain security scanning — to demonstrate best practices in repository maintenance.

Key areas covered in this sandbox include:

- **AI-assisted development** — integration with large language model APIs such as Claude and LM Studio for development and testing workflows.
- **Security tooling** — CodeQL static analysis, OpenSSF Scorecard, Dependabot automated dependency updates, and secret scanning via pre-commit hooks.
- **Cross-platform sandboxing** — references and resources for Linux, macOS, and Windows sandbox environments.
- **Open research** — archiving and DOI minting via Zenodo to make outputs citable and accessible.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Git
- Docker (optional, for containerized development)

### Installation (Optional)

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Git-Hub-Chris/SandboxEnvironment.git
   cd SandboxEnvironment
   ```

2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   # Or for development with extra tools:
   pip install -e ".[dev]"
   ```

### Running Tests

Run the test suite with pytest:

```bash
pytest -v
```

Run tests with coverage:

```bash
pytest --cov=. --cov-report=term-missing
```

### Code Quality

Check code formatting with Black:

```bash
black --check .
# Or format automatically:
black .
```

Run linting with Ruff:

```bash
ruff check .
```

### Docker Usage

Build and run tests in Docker:

```bash
docker-compose run test
```

Interactive development environment:

```bash
docker-compose run dev
```

For more Docker details, see [DOCKER.md](DOCKER.md).

## Configuration

The repository includes a `Phi-4.prompt.yml` configuration file for testing with Microsoft Phi-4 language model integration, providing model parameters and system prompts for AI-assisted development workflows.

## Software testing

### Claude API

<https://platform.claude.com/docs/en/api/overview>

### LM Studio API

<https://lmstudio.ai/docs/developer/rest>

### Visual Studio Code API

<https://code.visualstudio.com/api/references/vscode-api>

### ORCID Sandbox

<https://sandbox.orcid.org/0009-0002-9214-7327>

### Local Contexts Hub Sandbox

<https://sandbox.localcontextshub.org/dashboard/>

### Linux Sandbox

<https://labex.io/tutorials/linux-online-linux-terminal-and-playground-372915>

### MacOS Sandbox

<https://developer.apple.com/documentation/xcode/configuring-the-macos-app-sandbox>

### Windows Sandbox

<https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/>

## Acknowledgements

A special thank you to these organizations for providing the digital resources necessary to help create this repository. Enjoy the sandbox.

- **[GitHub](https://github.com)** — repository hosting, GitHub Actions CI/CD, Dependabot, CodeQL security scanning, and GitHub Copilot.
- **[Zenodo](https://zenodo.org)** — open-access archiving and DOI minting for research outputs.
- **[OpenSSF](https://openssf.org)** — Open Source Security Foundation Best Practices badge and Scorecard supply-chain security tooling.
- **[Anthropic](https://www.anthropic.com)** — Claude API for AI-assisted development and testing.
- **[LM Studio](https://lmstudio.ai)** — local large language model inference API for development and testing.
- **[Local Contexts](https://localcontexts.org)** — Open to Collaborate Notice, supporting Indigenous data sovereignty and ethical collaboration.

![Open_To_Collaborate](https://github.com/user-attachments/assets/940c11b1-bf4e-449c-9e2a-51ef4528e0ad)
