def generate_streak_svg(stats):
    svg_template = f"""
    <svg width="495" height="195" viewBox="0 0 495 195" xmlns="http://www.w3.org/2000/svg">
      <style>
        .header {{ font: 600 18px 'Segoe UI', Ubuntu, Sans-Serif; fill: #0891b2; }}
        .stat {{ font: 800 32px 'Segoe UI', Ubuntu, Sans-Serif; fill: #ffffff; }}
        .label {{ font: 400 14px 'Segoe UI', Ubuntu, Sans-Serif; fill: #ffffff; }}
        .bg {{ fill: #1c1917; }}
        .border {{ stroke: #E4E2E2; stroke-opacity: 0.5; }}
      </style>
      <rect x="0.5" y="0.5" rx="4.5" width="494" height="194" class="bg" />

      <g transform="translate(25, 35)">
        <text x="0" y="0" class="header">Current Streak</text>
        <text x="0" y="40" class="stat">{stats['current_streak']}</text>
        <text x="0" y="60" class="label">days</text>
      </g>

      <g transform="translate(185, 35)">
        <text x="0" y="0" class="header">Total Contributions</text>
        <text x="0" y="40" class="stat">{stats['total_contributions']}</text>
        <text x="0" y="60" class="label">commits</text>
      </g>

      <g transform="translate(350, 35)">
        <text x="0" y="0" class="header">Longest Streak</text>
        <text x="0" y="40" class="stat">{stats['longest_streak']}</text>
        <text x="0" y="60" class="label">days</text>
      </g>
    </svg>
    """
    return svg_template

def generate_languages_svg(languages):
    # Calculate total height based on number of languages
    # But for simplicity, we will stick to a fixed size and list top 5

    height = 220
    width = 300

    lang_items = ""
    y_offset = 40

    for lang in languages:
        name = lang['name']
        percent = f"{lang['percentage']:.1f}%"
        color = lang['color']
        width_bar = lang['percentage'] * 1.5 # Scale factor

        lang_items += f"""
        <g transform="translate(25, {y_offset})">
            <text x="0" y="10" style="font: 600 14px 'Segoe UI', Ubuntu, Sans-Serif; fill: #ffffff;">{name}</text>
            <text x="220" y="10" style="font: 400 14px 'Segoe UI', Ubuntu, Sans-Serif; fill: #9ca3af;">{percent}</text>
            <rect x="0" y="20" width="{width_bar}" height="8" rx="4" fill="{color}" />
        </g>
        """
        y_offset += 35

    svg_template = f"""
    <svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
      <style>
        .header {{ font: 600 18px 'Segoe UI', Ubuntu, Sans-Serif; fill: #0891b2; }}
        .bg {{ fill: #1c1917; }}
      </style>
      <rect x="0.5" y="0.5" rx="4.5" width="{width-1}" height="{height-1}" class="bg" />
      <text x="25" y="25" class="header">Most Used Languages</text>
      {lang_items}
    </svg>
    """
    return svg_template
