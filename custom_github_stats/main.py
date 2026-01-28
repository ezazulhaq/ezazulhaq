import os
import argparse
from client import GitHubClient
from stats import get_streak_stats, get_language_stats
from svg_gen import generate_streak_svg, generate_languages_svg

def main():
    parser = argparse.ArgumentParser(description="Generate GitHub Stats SVGs")
    parser.add_argument("--username", required=True, help="GitHub Username")
    parser.add_argument("--token", required=True, help="GitHub Personal Access Token")
    parser.add_argument("--output-dir", default="..", help="Directory to save the SVGs")

    args = parser.parse_args()

    client = GitHubClient(args.token)

    print(f"Fetching stats for {args.username}...")

    try:
        streak_stats = get_streak_stats(client, args.username)
        print("Streak stats fetched.")

        streak_svg = generate_streak_svg(streak_stats)
        with open(os.path.join(args.output_dir, "github-streak-stats.svg"), "w") as f:
            f.write(streak_svg)
        print("github-streak-stats.svg generated.")

        lang_stats = get_language_stats(client, args.username)
        print("Language stats fetched.")

        lang_svg = generate_languages_svg(lang_stats)
        with open(os.path.join(args.output_dir, "github-language-stats.svg"), "w") as f:
            f.write(lang_svg)
        print("github-language-stats.svg generated.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
