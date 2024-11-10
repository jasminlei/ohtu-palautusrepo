from rich.console import Console
from rich.table import Table
from player_stats import PlayerStats
from player_reader import PlayerReader

console = Console()


def main():
    seasons = [
        "2018-19",
        "2019-20",
        "2020-21",
        "2021-22",
        "2022-23",
        "2023-24",
        "2024-25",
    ]

    while True:
        console.print("Select season:")
        console.print(f"[magenta][{'/'.join(seasons)}][/magenta]", end="")
        season = input(": ")

        if season not in seasons:
            console.print(
                "[red]Invalid season, please select a valid season from above.[/red]"
            )
            continue
        break

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    nationalities = [
        "AUT",
        "CZE",
        "AUS",
        "SWE",
        "GER",
        "DEN",
        "SUI",
        "SVK",
        "NOR",
        "RUS",
        "CAN",
        "LAT",
        "BLR",
        "SLO",
        "USA",
        "FIN",
        "GBR",
    ]

    while True:
        console.print("Select nationality:")
        console.print(f"[magenta][{'/'.join(nationalities)}][/magenta]", end="")
        nationality = input(": ")

        if nationality not in nationalities:
            console.print(
                "[red]Invalid nationality, please select a valid nationality from above.[/red]"
            )
            continue

        players = stats.top_scorers_by_nationality(nationality)

        table = Table(title=f"Top scorers of {nationality} season {season}")
        table.add_column("name", style="cyan", justify="left")
        table.add_column("team", style="magenta", justify="center")
        table.add_column("goals", style="green", justify="center")
        table.add_column("assists", style="green", justify="center")
        table.add_column("points", style="green", justify="center")

        for player in players:
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.total_points()),
            )

        console.print(table)


if __name__ == "__main__":
    main()
