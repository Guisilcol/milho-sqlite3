import sys
import traceback

class ApplicationFlow:
    "This class is responsible for handling the application flow."

    @staticmethod
    def exit_application_successfully():
        print("Exiting...")
        sys.exit(0)

    @staticmethod
    def exit_application_with_error():
        print("A fatal error has occurred: ")
        print(traceback.format_exc())
        print("Exiting...")
        sys.exit(1)

    @staticmethod
    def print_returning_to_menu():
        print("\nReturning to menu...")

    @staticmethod
    def print_traceback():
        print(traceback.format_exc())
