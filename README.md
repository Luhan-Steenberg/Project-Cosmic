# Project-Cosmic


## Virtual Environments
I have included 3.12.3-requirements.txt to simplify setting up the correct virtual environment. You need to setup the virtual environment on your devices through the following commands: 

```powershell
python -m venv 3.12.3
./3.12.3/bin/Activate.ps1
python -m pip install -r 3.12.3-requirements.txt
```

## Style Guidelines
| Entity | Naming Style | Example | Notes |
| :--- | :--- | :--- | :--- |
| **Classes** | `CapitalizedWords` | `MyClass`, `HTTPServer` | Also known as CapWords or CamelCase. Capitalize all letters of acronyms. |
| **Type Variables** | `CapitalizedWords` | `AnyStr`, `T` | Prefer short names. |
| **Functions** | `lower_case_with_underscores` | `calculate_total()` | |
| **Variables** | `lower_case_with_underscores` | `user_age`, `total` | |
| **Constants** | `UPPER_CASE_WITH_UNDERSCORES` | `MAX_OVERFLOW` | Usually defined at the module level. |
| **Methods & Instance Variables** | `lower_case_with_underscores` | `get_status()`, `current_state` | Use `self` for the first argument of instance methods, and `cls` for class methods. |
| **Modules** | Short, all-lowercase | `my_module.py` | Underscores can be used if they improve readability. |

# Advanced functionality
- Some sounds are implemented
- Improved graphics
- Leaderboard & High score screen with names
- Progressively harder levels
    - Infinite mode
- Multiplayer/Additional shooter
- Special "Boss enemy" - On level 10
    - Enemy counterattack
- Hit points
- Pause function (press escape)


# Work Distribution
Luhan
- Gamestate & gameflow (I had a vision of how it works)
- Aliens
    - Boss alien
- Multiplayer
- 

Jovan
- Players
- Health systems
- Visuals

Francois
- Screens
- Bullet management code 
- Explosions
