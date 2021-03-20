from game import Game

game = Game()
game.generate_set_of_characters(12)
game.generate_set_of_items(10)
game.give_items()
game.play()
game.anounce_results()
