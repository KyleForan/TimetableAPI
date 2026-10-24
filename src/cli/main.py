from textual.app import App, ComposeResult
from textual.widgets import Welcome


class QuestionApp(App[str]):

    def compose(self) -> ComposeResult:
        yield Welcome()

    def on_button_pressed(self) -> None:
        self.exit()


def main() -> None:
    app = QuestionApp()
    x = app.run()
