"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with inheritance structure and method overriding concepts
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    def __init__(self, name, health, strength, magic):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        self.weapon = None

    def attack(self, target):
        weapon_bonus = self.weapon.damage_bonus if self.weapon else 0
        damage = max(5, self.strength + weapon_bonus)  # *** FIX: always >= 5 ***
        print(f"{self.name} attacks {target.name} for {damage} physical damage.")
        target.take_damage(damage)
        
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. (Health now: {self.health})")
        
    def display_stats(self):
        print(f"Name: {self.name}")
        print(f" Health: {self.health}")
        print(f" Strength: {self.strength}")
        print(f" Magic: {self.magic}")
        if self.weapon:
            print(f" Weapon: {self.weapon.name} (+{self.weapon.damage_bonus} dmg)")
        else:
            print(f" Weapon: None")


class Player(Character):
    def __init__(self, name, character_class, health, strength, magic):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        
    def display_stats(self):
        super().display_stats()
        print(f" Class: {self.character_class}")
        print(f" Level: {self.level}")
        print(f" Experience: {self.experience}")


class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, "Warrior", 120, 15, 5)
        
    def attack(self, target):
        weapon_bonus = self.weapon.damage_bonus if self.weapon else 0
        damage = max(5, self.strength + 5 + weapon_bonus)  # *** FIX ***
        print(f"{self.name} (Warrior) slashes {target.name} for {damage} damage.")
        target.take_damage(damage)
        
    def power_strike(self, target):
        weapon_bonus = self.weapon.damage_bonus if self.weapon else 0
        damage = max(5, self.strength * 2 + 10 + weapon_bonus)
        print(f"{self.name} uses Power Strike on {target.name} for {damage} damage!")
        target.take_damage(damage)


class Mage(Player):
    def __init__(self, name):
        super().__init__(name, "Mage", 80, 8, 20)
        
    def attack(self, target):
        weapon_bonus = self.weapon.damage_bonus if self.weapon else 0
        damage = max(5, self.magic + weapon_bonus)  # *** FIX ***
        print(f"{self.name} (Mage) casts a spell at {target.name} for {damage} magic damage.")
        target.take_damage(damage)
        
    def fireball(self, target):
        weapon_bonus = self.weapon.damage_bonus if self.weapon else 0
        damage = max(5, self.magic * 2 + 8 + weapon_bonus)
        print(f"{self.name} hurls a Fireball at {target.name} for {damage} damage!")
        target.take_damage(damage)


class Rogue(Player):
    def __init__(self, name):
        super().__init__(name, "Rogue", 90, 12, 10)
        
    def attack(self, target):
        weapon_bonus = self.weapon.damage_bonus if self.weapon else 0
        is_crit = random.randint(1, 10) <= 3
        base = self.strength + weapon_bonus

        if is_crit:
            damage = max(5, base * 2)   # *** FIX ***
            print(f"{self.name} (Rogue) performs a CRITICAL attack on {target.name} for {damage} damage!")
        else:
            damage = max(5, base)       # *** FIX ***
            print(f"{self.name} (Rogue) quickly strikes {target.name} for {damage} damage.")

        target.take_damage(damage)
        
    def sneak_attack(self, target):
        weapon_bonus = self.weapon.damage_bonus if self.weapon else 0
        damage = max(5, (self.strength + weapon_bonus) * 2 + 5)
        print(f"{self.name} performs a Sneak Attack on {target.name} for {damage} damage!")
        target.take_damage(damage)


class Weapon:
    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus
        
    def display_info(self):
        print(f"Weapon: {self.name} (Damage Bonus: +{self.damage_bonus})
# ----------------------------- Testing --------------------------------------
if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")

    # Make one of each
    w = Warrior("Galahad")
    m = Mage("Merlin")
    r = Rogue("Robin")

    print("\n--- Stats ---")
    w.display_stats()
    m.display_stats()
    r.display_stats()

    print("\n--- Attacks ---")
    dummy = Character("Dummy", 100, 0, 0)
    for c in [w, m, r]:
        c.attack(dummy)
        dummy.health = 100

    print("\n--- Special Abilities ---")
    w.power_strike(dummy)
    m.fireball(dummy)
    r.sneak_attack(dummy)

    print("\n--- Weapons ---")
    sword = Weapon("Iron Sword", 10)
    sword.display_info()

    print("\n--- Battle Test ---")
    fight = SimpleBattle(w, m)
    fight.fight()


# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # TODO: Create one of each character type
    # warrior = Warrior("Sir Galahad")
    # mage = Mage("Merlin")
    # rogue = Rogue("Robin Hood")
    
    # TODO: Display their stats
    # print("\n📊 Character Stats:")
    # warrior.display_stats()
    # mage.display_stats()
    # rogue.display_stats()
    
    # TODO: Test polymorphism - same method call, different behavior
    # print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    # dummy_target = Character("Target Dummy", 100, 0, 0)
    # 
    # for character in [warrior, mage, rogue]:
    #     print(f"\n{character.name} attacks the dummy:")
    #     character.attack(dummy_target)
    #     dummy_target.health = 100  # Reset dummy health
    
    # TODO: Test special abilities
    # print("\n✨ Testing Special Abilities:")
    # target1 = Character("Enemy1", 50, 0, 0)
    # target2 = Character("Enemy2", 50, 0, 0)
    # target3 = Character("Enemy3", 50, 0, 0)
    # 
    # warrior.power_strike(target1)
    # mage.fireball(target2)
    # rogue.sneak_attack(target3)
    
    # TODO: Test composition with weapons
    # print("\n🗡️ Testing Weapon Composition:")
    # sword = Weapon("Iron Sword", 10)
    # staff = Weapon("Magic Staff", 15)
    # dagger = Weapon("Steel Dagger", 8)
    # 
    # sword.display_info()
    # staff.display_info()
    # dagger.display_info()
    
    # TODO: Test the battle system
    # print("\n⚔️ Testing Battle System:")
    # battle = SimpleBattle(warrior, mage)
    # battle.fight()
    
    print("\n✅ Testing complete!")
