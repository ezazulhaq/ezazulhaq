# Custom GitHub Stats Generator

This project allows you to generate your own GitHub stats images (Streak Stats and Top Languages) locally, similar to services like `github-readme-streak-stats` and `github-readme-stats`.

## Services Explained

The original badges in the `README.md` use third-party services:

1.  **GitHub Readme Streak Stats**: Uses GitHub's GraphQL API to fetch your contribution calendar and calculates your current and longest streak of consecutive days with contributions.
2.  **GitHub Readme Stats**: Analyze your repositories to calculate the total size of code written in each language and displays the top languages.

## How to use this Custom Service

This custom implementation is a Python script that you can run to generate SVG images containing the same data.

### Prerequisites

1.  **Python 3**: Ensure Python is installed.
2.  **GitHub Personal Access Token (PAT)**: You need a token to access the GitHub API.
    -   Go to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens).
    -   Generate a new token (classic).
    -   Select scopes: `repo` (for private repos) or just public access, and `read:user`.

### Installation

1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

Run the script with your username and token:

```bash
python main.py --username YOUR_USERNAME --token YOUR_GITHUB_TOKEN
```

This will generate two files in the current directory:
-   `github-streak-stats.svg`
-   `github-language-stats.svg`

### Automating with GitHub Actions

You can set up a GitHub Action to run this script daily and commit the generated SVGs to your repository, so your profile stays up to date automatically.
