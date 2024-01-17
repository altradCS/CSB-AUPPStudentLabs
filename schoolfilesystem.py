
import pandas as pd

class SchoolSystem:
    def __init__(self):
        self.data = None

    def process_file(self, file_path):
        """
        Opens and reads the content of the specified file.
        Supports CSV, Excel, and plain text formats.
        Extracts assessment information, student scores, and other relevant details.
        """
        try:
            if file_path.endswith('.csv'):
                self.data = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                self.data = pd.read_excel(file_path)
            elif file_path.endswith('.txt'):
                with open(file_path, 'r') as file:
                    self.data = file.read()
            else:
                raise ValueError("Unsupported file format")
        except Exception as e:
            print(f"Error processing file: {e}")

    def analyze_content(self):
        """
        Analyzes assessment data to identify the top student who has the highest score.
        Finds their improvement on "Midterm Criteria and Homework".
        """
        try:
            if isinstance(self.data, pd.DataFrame):
                # Print column names for debugging
                print("Column Names:", self.data.columns)

                # Assuming columns 'Student', 'Midterm Criteria', 'Homework' are present in the dataset
                top_student = self.data.loc[self.data['Final'].idxmax(), 'Student Name']
                initial_score = self.data.loc[self.data['Student Name'] == top_student, 'Midterm 1'].values[0]
                final_score = self.data.loc[self.data['Student Name'] == top_student, 'Midterm 2'].values[0]

                improvement = final_score - initial_score

                print(f"Top Student: {top_student}")
                print(f"Initial Score on Midterm 1: {initial_score}")
                print(f"Final Score on Midterm 2: {final_score}")
                print(f"Improvement: {improvement}")
            else:
                raise ValueError("No valid data for analysis.")
        except Exception as e:
            print(f"Error analyzing content: {e}")


try:

    file_path = r"C:\Users\HP\Desktop\Aupp\Spring 2024\Computer Science B\Schoolfilesystem\Exam_Grade_Entry_Form2024-01-16_21_44_05.csv"
    school_system = SchoolSystem()
    school_system.process_file(file_path)

    # Content analysis
    school_system.analyze_content()

except Exception as e:
    print(f"An unexpected error occurred: {e}")
