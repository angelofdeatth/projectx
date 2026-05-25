from game import Game


def main():
    print("Запуск игры Змейка...")
    print("Управление: стрелки или WASD")
    print("Q - выход, R - рестарт (после проигрыша)")

    game = Game(width=20, height=15, cell_size=30)
    game.run()


if __name__ == "__main__":
    main()