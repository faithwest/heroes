from datetime import datetime
from models import db, Power, Hero, Hero_Power

def seed_powers():
    powers_data = [
        {"name": "super strength", "description": "gives the wielder super-human strengths"},
        {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
        {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
        {"name": "elasticity", "description": "can stretch the human body to extreme lengths"},
    ]

    for power_info in powers_data:
        power = Power(**power_info, created_at=datetime.now(), updated_at=datetime.now())
        db.session.add(power)

def seed_heroes():
    heroes_data = [
        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
        {"name": "Janet Van Dyne", "super_name": "The Wasp"},
        {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
        {"name": "Carol Danvers", "super_name": "Captain Marvel"},
        {"name": "Jean Grey", "super_name": "Dark Phoenix"},
        {"name": "Ororo Munroe", "super_name": "Storm"},
        {"name": "Kitty Pryde", "super_name": "Shadowcat"},
        {"name": "Elektra Natchios", "super_name": "Elektra"},
    ]

    for hero_info in heroes_data:
        hero = Hero(**hero_info, created_at=datetime.now(), updated_at=datetime.now())
        db.session.add(hero)

def seed_hero_power():
    strengths = ["Strong", "Weak", "Average"]

    heroes = Hero.query.all()

    for hero in heroes:
        for _ in range(1, 4):
            power = Power.query.order_by(db.func.random()).first()
            hero_power = Hero_Power(
                hero_id=hero.id,
                power_id=power.id,
                strength=strengths[db.func.random() % 3],
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
            db.session.add(hero_power)

def seed_database():
    seed_powers()
    seed_heroes()
    seed_hero_power()

    db.session.commit()

if __name__ == "__main__":
    from app import app  # Assuming your Flask app is in the 'app' module
    with app.app_context():
        db.create_all()
        seed_database()
