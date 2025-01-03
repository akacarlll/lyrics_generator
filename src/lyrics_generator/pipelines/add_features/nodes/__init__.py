from lyrics_generator.pipelines.add_features.nodes._get_genre import add_genre_column
from lyrics_generator.pipelines.add_features.nodes._get_year import add_release_year_column
from lyrics_generator.pipelines.add_features.nodes._get_length_lyrics import add_lyrics_stats
from lyrics_generator.pipelines.add_features.nodes._divide_genre import divide_genre




__all__ = ["add_genre_column", "add_release_year_column", "add_lyrics_stats", "divide_genre"]
