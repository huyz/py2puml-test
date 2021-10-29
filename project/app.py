from project.util import hello_from_util

class App:
    def run(self) -> None:
        print("project/app.py")
        hello_from_util()

if __name__ == '__main__':
    app = App()
    app.run()
