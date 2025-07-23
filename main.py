#!/usr/bin/env python3
"""
Grimoire Madness - Un gioco multiplayer turn-based con maghi
"""

import json
import os
import random
import time
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum

from src.core.game_engine import GameEngine
from src.core.player import Player
from src.core.wizard import Wizard
from src.core.spells import SpellManager
from src.core.combat import CombatSystem
from src.core.utils import Colors, clear_screen, get_player_input

def main():
    """Funzione principale del gioco"""
    clear_screen()
    print(f"{Colors.CYAN}=" * 60)
    print(f"{Colors.YELLOW}        🧙‍♂️ GRIMOIRE MADNESS 🧙‍♀️")
    print(f"{Colors.CYAN}=" * 60)
    print(f"{Colors.WHITE}Un gioco di combattimento magico turn-based!")
    print(f"{Colors.CYAN}=" * 60)
    print()
    
    game = GameEngine()
    game.run()

if __name__ == "__main__":
    main()
