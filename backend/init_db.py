#!/usr/bin/env python3
"""
Database initialization script
Run this to create tables and seed data
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal, create_tables
from app.seed_data import seed_exercises

def init_database():
    """Initialize database with tables and seed data"""
    print("Creating database tables...")
    create_tables()
    
    print("Seeding common exercises...")
    db = SessionLocal()
    try:
        seed_exercises(db)
        print("Database initialization completed!")
    except Exception as e:
        print(f"Error during initialization: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    init_database()
