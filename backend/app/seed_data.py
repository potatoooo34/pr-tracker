"""
Seed data for common exercises
"""
from sqlalchemy.orm import Session
from .models import Exercise

COMMON_EXERCISES = [
    # Upper Body
    {"name": "Bench Press", "muscle_group": "Chest"},
    {"name": "Incline Bench Press", "muscle_group": "Chest"},
    {"name": "Decline Bench Press", "muscle_group": "Chest"},
    {"name": "Dumbbell Press", "muscle_group": "Chest"},
    {"name": "Push-ups", "muscle_group": "Chest"},
    {"name": "Dips", "muscle_group": "Chest"},
    {"name": "Pull-ups", "muscle_group": "Back"},
    {"name": "Chin-ups", "muscle_group": "Back"},
    {"name": "Lat Pulldown", "muscle_group": "Back"},
    {"name": "Bent-over Row", "muscle_group": "Back"},
    {"name": "T-Bar Row", "muscle_group": "Back"},
    {"name": "Seated Row", "muscle_group": "Back"},
    {"name": "Overhead Press", "muscle_group": "Shoulders"},
    {"name": "Lateral Raises", "muscle_group": "Shoulders"},
    {"name": "Front Raises", "muscle_group": "Shoulders"},
    {"name": "Rear Delt Flyes", "muscle_group": "Shoulders"},
    {"name": "Bicep Curls", "muscle_group": "Biceps"},
    {"name": "Hammer Curls", "muscle_group": "Biceps"},
    {"name": "Preacher Curls", "muscle_group": "Biceps"},
    {"name": "Tricep Dips", "muscle_group": "Triceps"},
    {"name": "Close-grip Bench Press", "muscle_group": "Triceps"},
    {"name": "Tricep Pushdowns", "muscle_group": "Triceps"},
    
    # Lower Body
    {"name": "Squat", "muscle_group": "Legs"},
    {"name": "Front Squat", "muscle_group": "Legs"},
    {"name": "Bulgarian Split Squat", "muscle_group": "Legs"},
    {"name": "Lunges", "muscle_group": "Legs"},
    {"name": "Leg Press", "muscle_group": "Legs"},
    {"name": "Romanian Deadlift", "muscle_group": "Legs"},
    {"name": "Stiff Leg Deadlift", "muscle_group": "Legs"},
    {"name": "Leg Curls", "muscle_group": "Legs"},
    {"name": "Leg Extensions", "muscle_group": "Legs"},
    {"name": "Calf Raises", "muscle_group": "Legs"},
    {"name": "Seated Calf Raises", "muscle_group": "Legs"},
    
    # Full Body
    {"name": "Deadlift", "muscle_group": "Full Body"},
    {"name": "Sumo Deadlift", "muscle_group": "Full Body"},
    {"name": "Power Clean", "muscle_group": "Full Body"},
    {"name": "Clean and Jerk", "muscle_group": "Full Body"},
    {"name": "Snatch", "muscle_group": "Full Body"},
    {"name": "Kettlebell Swings", "muscle_group": "Full Body"},
    {"name": "Burpees", "muscle_group": "Full Body"},
    {"name": "Thrusters", "muscle_group": "Full Body"},
    
    # Core
    {"name": "Plank", "muscle_group": "Core"},
    {"name": "Side Plank", "muscle_group": "Core"},
    {"name": "Russian Twists", "muscle_group": "Core"},
    {"name": "Mountain Climbers", "muscle_group": "Core"},
    {"name": "Dead Bug", "muscle_group": "Core"},
    {"name": "Hollow Body Hold", "muscle_group": "Core"},
    {"name": "L-sit", "muscle_group": "Core"},
    {"name": "Dragon Flag", "muscle_group": "Core"},
]

def seed_exercises(db: Session):
    """Seed the database with common exercises"""
    for exercise_data in COMMON_EXERCISES:
        # Check if exercise already exists
        existing = db.query(Exercise).filter(
            Exercise.name == exercise_data["name"],
            Exercise.user_id.is_(None)  # Global exercises have user_id = None
        ).first()
        
        if not existing:
            exercise = Exercise(
                name=exercise_data["name"],
                muscle_group=exercise_data["muscle_group"],
                user_id=None  # Global exercise
            )
            db.add(exercise)
    
    db.commit()
    print(f"Seeded {len(COMMON_EXERCISES)} common exercises")
