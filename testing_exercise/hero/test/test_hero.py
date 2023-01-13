from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("hero1", 5, 50, 20)
        self.enemy_hero = Hero("hero2", 3, 60, 30)

    def test_attrs_are_set(self):
        self.assertEqual("hero1", self.hero.username)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(50, self.hero.health)
        self.assertEqual(20, self.hero.damage)

    def test_battle_when_usernames_are_equal_should_return_exception(self):
        self.enemy_hero.username = "hero1"
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_battle_when_hero_health_is_0_should_return_value_error(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_battle_when_enemy_hero_health_is_zero(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(f"You cannot fight hero2. He needs to rest", str(context.exception))

    def test_battle_when_draw(self):
        player_damage = self.hero.damage * self.hero.level
        enemy_hero_damage = self.enemy_hero.damage * self.enemy_hero.level

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(-40, self.hero.health)
        self.assertEqual(-40, self.enemy_hero.health)
        self.assertEqual("Draw", result)

    def test_battle_when_enemy_hero_looses(self):
        self.hero.health = 100
        player_damage = self.hero.damage * self.hero.level
        enemy_hero_damage = self.enemy_hero.damage * self.enemy_hero.level

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(6, self.hero.level)
        self.assertEqual(15, self.hero.health)
        self.assertEqual(25, self.hero.damage)
        self.assertEqual(-40, self.enemy_hero.health)
        self.assertEqual("You win", result)

    def test_battle_when_hero_looses(self):
        self.enemy_hero.health = 110
        player_damage = self.hero.damage * self.hero.level
        enemy_hero_damage = self.enemy_hero.damage * self.enemy_hero.level

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(4, self.enemy_hero.level)
        self.assertEqual(15, self.enemy_hero.health)
        self.assertEqual(35, self.enemy_hero.damage)
        self.assertEqual(-40, self.hero.health)

        self.assertEqual("You lose", result)

    def test_string_representation_should_return_message(self):
        message = f"Hero {self.hero.username}: {self.hero.level} lvl\nHealth: {self.hero.health}\nDamage: {self.hero.damage}\n"
        self.assertEqual(message, str(self.hero))








if __name__ == '__main__':
    main()