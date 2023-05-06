from helpers.controller import Controller


def main():
    """Main entry point of the application."""
    controller = Controller()
    controller.app.mainloop()


if __name__ == "__main__":
    main()
