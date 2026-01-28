from datetime import datetime, timedelta

def get_streak_stats(client, username):
    query = """
    query($userName:String!) {
      user(login: $userName){
        createdAt
        contributionsCollection {
          contributionCalendar {
            totalContributions
            weeks {
              contributionDays {
                contributionCount
                date
              }
            }
          }
        }
      }
    }
    """
    variables = {"userName": username}
    result = client.run_query(query, variables)

    user_data = result.get("data", {}).get("user")
    if not user_data:
        raise ValueError(f"User {username} not found or data not available.")

    calendar = user_data["contributionsCollection"]["contributionCalendar"]
    weeks = calendar["weeks"]

    dates = []
    for week in weeks:
        for day in week["contributionDays"]:
            dates.append((day["date"], day["contributionCount"]))

    dates.sort(key=lambda x: x[0])

    current_streak = 0
    longest_streak = 0

    today = datetime.now().date()
    # Check if we need to account for timezones, but GitHub dates are usually UTC based or local to the user if specified.
    # The API returns dates as strings "YYYY-MM-DD".

    # Iterate backwards for current streak
    # If today has no contribution, check yesterday. If yesterday has contribution, streak starts.
    # If today has contribution, streak starts today.

    # Let's convert strings to date objects
    date_map = {d[0]: d[1] for d in dates}

    temp_streak = 0
    # Calculate longest streak
    for date_str, count in dates:
        if count > 0:
            temp_streak += 1
        else:
            if temp_streak > longest_streak:
                longest_streak = temp_streak
            temp_streak = 0
    # Final check
    if temp_streak > longest_streak:
        longest_streak = temp_streak

    # Calculate current streak
    # Check today
    today_str = today.strftime("%Y-%m-%d")
    yesterday = today - timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y-%m-%d")

    # If today has contribution, we start counting backwards from today
    # If today has no contribution, but yesterday does, we start counting backwards from yesterday
    # If neither, streak is 0.

    check_date = today
    if date_map.get(today_str, 0) == 0:
        if date_map.get(yesterday_str, 0) == 0:
            current_streak = 0
        else:
            check_date = yesterday

    if date_map.get(check_date.strftime("%Y-%m-%d"), 0) > 0:
        current_streak = 0
        while True:
            d_str = check_date.strftime("%Y-%m-%d")
            if date_map.get(d_str, 0) > 0:
                current_streak += 1
                check_date = check_date - timedelta(days=1)
            else:
                break

    return {
        "total_contributions": calendar["totalContributions"],
        "current_streak": current_streak,
        "longest_streak": longest_streak
    }

def get_language_stats(client, username):
    query = """
    query($userName:String!) {
      user(login: $userName){
        repositories(first: 100, ownerAffiliations: [OWNER], isFork: false, orderBy: {field: PUSHED_AT, direction: DESC}) {
          nodes {
            name
            languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
              edges {
                size
                node {
                  color
                  name
                }
              }
            }
          }
        }
      }
    }
    """
    variables = {"userName": username}
    result = client.run_query(query, variables)

    user_data = result.get("data", {}).get("user")
    if not user_data:
        raise ValueError(f"User {username} not found or data not available.")

    repos = user_data["repositories"]["nodes"]

    lang_stats = {}
    total_size = 0

    for repo in repos:
        for edge in repo["languages"]["edges"]:
            size = edge["size"]
            name = edge["node"]["name"]
            color = edge["node"]["color"]

            if name not in lang_stats:
                lang_stats[name] = {"size": 0, "color": color}
            lang_stats[name]["size"] += size
            total_size += size

    # Calculate percentage
    final_stats = []
    for name, data in lang_stats.items():
        percentage = (data["size"] / total_size) * 100
        final_stats.append({
            "name": name,
            "color": data["color"],
            "percentage": percentage,
            "size": data["size"]
        })

    final_stats.sort(key=lambda x: x["size"], reverse=True)
    return final_stats[:5] # Top 5 languages
