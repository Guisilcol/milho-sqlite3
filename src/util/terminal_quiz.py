import inquirer as inq

class TerminalQuiz:
    def __init__(self) -> None:
        raise NotImplementedError("This class is not meant to be instantiated.")

    @staticmethod
    def ask_yes_or_no(question: str, default: bool = True) -> bool:
        answer = inq.prompt([inq.Confirm("answer", message=question, default=default)], raise_keyboard_interrupt=True)
        return answer["answer"]

    @staticmethod
    def ask_for_string(question: str, default: str = "", autocomplete: list = []) -> str:
        answer = inq.prompt([inq.Text("answer", message=question, default=default, autocomplete=autocomplete)], raise_keyboard_interrupt=True)
        return answer["answer"]

    @staticmethod
    def ask_for_integer(question: str, default: int = 0) -> int:
        while True:
            answer = inq.prompt([inq.Text("answer", message=question, default=str(default))], raise_keyboard_interrupt=True)
            if not str(answer["answer"]).isnumeric():
                continue
            
            return int(answer["answer"])

    @staticmethod
    def ask_for_float(question: str, default: float = 0.0) -> float:
        while True:
            answer = inq.prompt([inq.Text("answer", message=question, default=str(default))], raise_keyboard_interrupt=True)
            if not str(answer["answer"]).isnumeric():
                continue

            return float(answer["answer"])

    @staticmethod
    def ask_for_list(question: str, choices: list, default: str = "") -> str:
        answer = inq.prompt([inq.List("answer", message=question, choices=choices, default=default)], raise_keyboard_interrupt=True)
        return answer["answer"]

    @staticmethod
    def ask_for_checkbox(question: str, choices: list, default: list = []) -> list:
        answer = inq.prompt([inq.Checkbox("answer", message=question, choices=choices, default=default)], raise_keyboard_interrupt=True)
        return answer["answer"]