class GameStats:
    """Track statistics for aliens invasion"""

    def __init__(self, ai_settings):
        """Initialize statics"""
        self.ai_settings = ai_settings
        # Start game in an inactive state
        self.game_active = False

        self.score = 0
