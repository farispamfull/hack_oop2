from game import Game

game = Game()
game.generate_set_of_characters(5)
game.generate_set_of_items(5)
print(game.show_items()+'\n')
print(game.show_characters()+'\n')
