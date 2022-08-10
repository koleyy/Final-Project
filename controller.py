from PyQt5.QtWidgets import *
from view import Ui_MainWindow


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        """
        Function sets up all variables to be used throughout the controller
        :param args: None
        :param kwargs: None
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.credit = 0
        self.gpa = 0

        self.add_credits = 0
        self.total_credits = 0

        self.grade = ''
        self.grade_points = 0
        self.total_grade_points = 0

        self.button_calculate.clicked.connect(lambda: self.calculate())

    def calculate(self) -> None:
        """
        Function takes the input from text_credits and text_grade,
        adds these values to the total_credits and grade_points respectfully
        :return: None
        """
        try:
            # calculates new gpa to be presented on the gui
            self.add_credits = float(self.text_credits.toPlainText().strip())

            self.grade = self.text_grade.toPlainText().strip().upper()

            if self.add_credits > 0:
                if self.grade == 'A+' or self.grade == 'A':
                    self.grade_points = 4 * self.add_credits
                elif self.grade == 'A-':
                    self.grade_points = 3.67 * self.add_credits
                elif self.grade == 'B+':
                    self.grade_points = 3.33 * self.add_credits
                elif self.grade == 'B':
                    self.grade_points = 3 * self.add_credits
                elif self.grade == 'B-':
                    self.grade_points = 2.67 * self.add_credits
                elif self.grade == 'C+':
                    self.grade_points = 2.33 * self.add_credits
                elif self.grade == 'C':
                    self.grade_points = 2 * self.add_credits
                elif self.grade == 'C-':
                    self.grade_points = 1.67 * self.add_credits
                elif self.grade == 'D+':
                    self.grade_points = 1.33 * self.add_credits
                elif self.grade == 'D':
                    self.grade_points = 1 * self.add_credits
                elif self.grade == 'D-':
                    self.grade_points = 0.67 * self.add_credits
                elif self.grade == 'F':
                    self.grade_points = 0
                else:
                    raise ValueError
            else:
                if self.grade == 'A+' or self.grade == 'A' or self.grade == 'A-':
                    pass
                elif self.grade == 'B+' or self.grade == 'B' or self.grade == 'B-':
                    pass
                elif self.grade == 'C+' or self.grade == 'C' or self.grade == 'C-':
                    pass
                elif self.grade == 'D+' or self.grade == 'D' or self.grade == 'D-':
                    pass
                elif self.grade == 'F':
                    pass
                else:
                    raise ValueError

            if self.add_credits < 0:
                raise ValueError
            else:
                self.total_credits = self.total_credits + self.add_credits

            if self.add_credits > 0:
                self.total_grade_points = self.total_grade_points + self.grade_points

            if self.total_credits > 0:
                self.gpa = f'{(self.total_grade_points / self.total_credits):.2f}'
            else:
                self.gpa = f'No Credits'

            print(f'Total Grade Points: {self.total_grade_points}')
            print(f'Total Credits: {self.total_credits}')
            print(f'GPA: {self.gpa}')

            # takes values and alters the GPA on the gui
            self.label_gpa_value.setText(self.gpa)

            # clears all previous input
            self.text_grade.setText('')
            self.text_credits.setText('')

        except (ValueError, TypeError):
            print('oh no')
            msg = QMessageBox()
            msg.setText('Credits should be a positive number\nGrade should be a valid letter')
            msg.setWindowTitle("Invalid Data")
            msg.exec_()

            self.text_grade.setText('')
            self.text_credits.setText('')
