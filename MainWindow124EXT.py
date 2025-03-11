import sys
import pandas as pd
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem  # Correct import

from excercise_124.ui.MainWindow124 import Ui_MainWindow


class MainWindow124EXT(QMainWindow, Ui_MainWindow):  # Use QMainWindow directly
    def __init__(self):
        super().__init__()  # No need for additional arguments
        self.setupUi(self)  # Initialize the UI components

        # Load initial data
        self.df = pd.read_csv('SampleData2.csv')
        print(self.df)

        # Connect button actions to methods
        self.pushButton.clicked.connect(self.export_all_data)
        self.pushButton_2.clicked.connect(self.filter_by_birthday)
        self.pushButton_3.clicked.connect(self.export_top_3_oldest)
        self.pushButton_4.clicked.connect(self.filter_tester_role)
        self.pushButton_5.clicked.connect(self.count_by_role)

        # Display data in the table
        self.display_data(self.df)

    def display_data(self, df):
        """Display the DataFrame in the QTableWidget"""
        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(df.columns)

        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(df.iat[row, col])))

    def export_all_data(self):
        """Export all employee data to the console"""
        print(self.df)

    def filter_by_birthday(self):
        """Filter employees born in 2001"""
        filtered_data = self.df[self.df['Dob'].str.contains('2001')]
        print("\nEmployees born in 2001:")
        print(filtered_data)

    def export_top_3_oldest(self):
        """Export the top 3 employees with the oldest age"""
        self.df['Dob'] = pd.to_datetime(self.df['Dob'], format='%d/%m/%Y')
        sorted_df = self.df.sort_values(by='Dob').head(3)
        print("\nTop 3 Employees with the oldest age:")
        print(sorted_df)

    def filter_tester_role(self):
        """Filter employees with Tester role"""
        testers = self.df[self.df['Role'] == 'Tester']
        print("\nEmployees with Tester role:")
        print(testers)

    def count_by_role(self):
        """Count the number of employees by role"""
        role_count = self.df['Role'].value_counts()
        print("\nNumber of Employees by Role:")
        print(role_count)


# Main function to run the application
def main():
    app = QApplication(sys.argv)  # Use QApplication correctly
    window = MainWindow124EXT()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
