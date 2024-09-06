import soccerdata as sd
import pandas as pd
import time
import os


class SoccerStatsExporter:
    def __init__(self, league, season, timestamp=None, export_dir=None):
        self.fbref = sd.FBref(leagues=league, seasons=season)
        self.timestamp = timestamp if timestamp else time.strftime("%Y%m%d-%H%M%S")
        self.export_dir = export_dir if export_dir else os.getcwd()  # Default to current working directory
        pd.set_option('display.max_rows', None)

    def export_stats(self, stat_type, entity="player", category="standard"):
        if entity == "player":
            stats = self.fbref.read_player_season_stats(stat_type=category)
        elif entity == "team":
            stats = self.fbref.read_team_season_stats(stat_type=category, opponent_stats=False)
        else:
            raise ValueError("Entity must be either 'player' or 'team'.")

        stats = stats.reset_index(drop=False)
        filename = f"{entity}_season_stats_{category}_{self.timestamp}.csv"
        filepath = os.path.join(self.export_dir, filename)
        stats.to_csv(filepath, index=False)
        print(f"Exported {entity} {category} stats to {filepath}")

    def export_player_stats(self, categories):
        for category in categories:
            self.export_stats(stat_type="player", entity="player", category=category)

    def export_team_stats(self, categories):
        for category in categories:
            self.export_stats(stat_type="team", entity="team", category=category)

