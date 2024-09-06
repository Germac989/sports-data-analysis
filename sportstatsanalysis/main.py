import time
from soccerstatsexporter import SoccerStatsExporter

if __name__ == "__main__":
    # Initialize the class with a custom export directory
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    export_directory = ""  # Change this to your desired folder
    soccer_stats = SoccerStatsExporter(
        league="ENG-Premier League",
        season=2024,
        timestamp=timestamp,
        export_dir=export_directory)

    player_categories = [
        "standard", "keeper", "keeper_adv", "defense", "misc",
        "playing_time", "possession", "goal_shot_creation",
        "passing_types", "passing", "shooting"
    ]

    team_categories = [
        "standard", "keeper", "keeper_adv", "shooting", "passing",
        "passing_types", "goal_shot_creation", "defense",
        "possession", "playing_time", "misc"
    ]

    soccer_stats.export_player_stats(player_categories)
    soccer_stats.export_team_stats(team_categories)
