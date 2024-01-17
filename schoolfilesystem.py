"""
Libraries you may need:
import csv, collections, dictionary, (pandas as pd), urlopen, etc..

classes and Functions to implement
template class
class SchoolAssessmentSystem:
    
    def __init__(self):
        pass
    def process_file(self):            
        pass
    def transfer_data(self):
        pass
    def fetch_web_data(self):
        pass
    def analyze_content(self):
        pass
    def generate_summary(self):
        pass
        
Analyze content & display result area
Sample of Output:

School Assessment Summary Report:

1. Overall Performance of Student A:
   - Average score: 85.5
   - Top-performing class: Grade 10B

2. Subject-wise Analysis:
   - Mathematics: Improved by 10% compared to the last assessment.
   - Science: Consistent performance across all classes.

3. Notable Observations:
   - Grade 8A shows a significant improvement in English proficiency.

4. Web Data Insights:
   - Online participation: 95% of students accessed assessment resources online.

5. Recommendations:
   - Consider additional support for Grade 9B in Mathematics.

Report generated on: 2024-01-14
"""


import csv
import pandas as pd
import datetime
from urllib.request import urlopen
from urllib.error import HTTPError
from io import StringIO


class SchoolAssessmentSystem:
    def __init__(self):
        self.data = None

    def process_data(self, file_path):
        try:
            if file_path.endswith('.csv'):
                self.data = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                self.data = pd.read_excel(file_path)
            elif file_path.endswith('.txt'):
                with open(file_path, 'r') as file:
                    self.data = file.read()
            else:
                raise ValueError('Unsupported file format')
            return 'Data processed successfully'
        except FileNotFoundError:
            return 'File not found'
        except Exception as e:
            return f'Error processing data: {str(e)}'

    def assign_grade(self, percentage):
        if percentage >= 90:
            return 'A'
        elif 80 <= percentage < 90:
            return 'B'
        elif 70 <= percentage < 80:
            return 'C'
        elif 60 <= percentage < 70:
            return 'D'
        else:
            return 'F'

    def transfer_data(self, criteria='merge', data_from_another_source=None, output_filename='exported_data.csv', output_format='csv'):
        try:
            if criteria == 'merge' and data_from_another_source is not None:
                if isinstance(self.data, pd.DataFrame):
                    self.data = pd.concat(
                        [self.data, data_from_another_source], ignore_index=True)
                    return 'Data merged successfully'
                else:
                    raise ValueError('Unsupported data format for merging')
            elif criteria == 'export':
                if isinstance(self.data, pd.DataFrame):
                    if output_filename == 'csv':
                        self.data.to_csv(output_filename, index=False)
                    elif output_filename == 'excel':
                        self.data.to_excel(output_filename, index=False)
                    else:
                        raise ValueError(
                            'Unsupported output file format for exporting')
                    return f'Data exported successfully to {output_filename} in {output_format} format'
                else:
                    raise ValueError('Unsupported data format for exporting')
            else:
                raise ValueError('Invalid criteria')
        except Exception as e:
            return f'Error transferring data: {str(e)}'

    def fetch_web_data(self, url):
        try:
            response = urlopen(url)
            self.data = pd.read_csv(pd.io.common.StringIO(
                response.read().decode('utf-8')))
            return 'Web data fetched successfully'
        except HTTPError as e:
            return f'Error fetching web data: HTTP Error {e.code}: {e.reason}'
        except Exception as e:
            return f'Error fetching web data: {str(e)}'

    def analyze_content(self):
        if self.data is None:
            return 'No data to analyze. Please process data first.'
        try:
            numeric_data = self.data.select_dtypes(include='number')
            analysis_result = numeric_data.describe()
            return analysis_result
        except ValueError:
            return 'Data contains non-numeric values. Please process data again.'

    def generate_summary(self):
        if self.data is None:
            return 'No data to summarize. Please process data first.'
        try:
            data = self.analyze_content()
            summary_result = f"""
                School Assessment Summary Report:

                1. Overall Performance of Student A:
                - Average score: {data['Math']['mean']}
                - Top-performing class:

                2. Subject-wise Analysis:
                - Mathematics: Improved by compared to the last assessment.
                - Science: Consistent performance across all classes.

                3. Notable Observations:
                - Grade shows a significant improvement in English proficiency.

                4. Web Data Insights:
                - Online participation: 95% of students accessed assessment resources online.

                5. Recommendations:
                - Consider additional support for Grade 9B in Mathematics.

                Report generated on: 2024-01-14"""

            return summary_result
        except ValueError:
            return 'Data contains non-numeric values. Please process data again.'
        except Exception as e:
            return f'Error generating summary: {e}'


if __name__ == '__main__':
    school_system = SchoolAssessmentSystem()

    # Process data
    data_process = school_system.process_data('Classes/Class 10A Score.csv')
    print(f"Data Process Result:\n{data_process}")

    # Transfer data
    merged_data = school_system.transfer_data(
        criteria='export', data_from_another_source=pd.read_csv('Classes/Class 10A Score.csv'))
    print(f"Merge Result:\n{merged_data}")

    # Fetch web data
    web_data_result = school_system.fetch_web_data(
        'https://www.aupp.edu.kh/assessment')
    print(f"Web Data Result:\n{web_data_result}")

    # Analyze content
    analysis_result = school_system.analyze_content()
    print(f"Analysis Result:\n{analysis_result}")

    # Generate summary
    summary_result = school_system.generate_summary()
    print(f"{summary_result}")
