import arcade


class Game(arcade.Window):
    def on_draw(self) -> bool | None:
        self.clear((255, 255, 255))

if __name__ == '__main__':
    window =  Game()
    arcade.run()