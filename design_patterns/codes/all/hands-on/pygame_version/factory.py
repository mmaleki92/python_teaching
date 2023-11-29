import pygame

class Enemy:
    def render(self, screen):
        pass

class Ghost(Enemy):
    def render(self, screen):
        # Render ghost on screen
        pass

class Goblin(Enemy):
    def render(self, screen):
        # Render goblin on screen
        pass

class EnemyFactory:
    @staticmethod
    def create_enemy(type):
        if type == "ghost":
            return Ghost()
        elif type == "goblin":
            return Goblin()
        else:
            raise ValueError("Unknown Enemy Type")

# Usage Example
enemy = EnemyFactory.create_enemy("ghost")
# enemy.render(screen) in the game loop
