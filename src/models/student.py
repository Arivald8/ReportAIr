from dataclasses import dataclass

@dataclass
class Student:
    # Main
    student_id: int = None
    name: str = None
    year: int = None
    level: str = None
    participation: str = None
    punctuality: str = None
    behaviour: str = None
    homework: str = None
    homework_imp: str = None
    best_achievement: str = None
    area_to_improve: str = None
    additional_comments: str = None
    reports_row_id: int = None

    # Custom
    level_custom: str = None
    participation_custom: str = None
    punctuality_custom: str = None
    behaviour_custom: str = None
    homework_custom: str = None
    homework_imp_custom: str = None
    best_achievement_custom: str = None
    area_to_improve_custom: str = None
    
    # Bools
    level_tick: int = None
    participation_tick: int = None
    punctuality_tick: int = None
    behaviour_tick: int = None
    homework_tick: int = None
    homework_imp_tick: int = None
    best_achievement_tick: int = None
    area_to_improve_tick: int = None
    additional_comments_tick: int = None