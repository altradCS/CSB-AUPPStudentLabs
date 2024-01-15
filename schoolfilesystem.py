import csv
import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError


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
            analysis_result = numeric_data.describe().to_string()
            return analysis_result
        except ValueError:
            return 'Data contains non-numeric values. Please process data again.'

    def generate_summary(self):
        if self.data is None:
            return 'No data to summarize. Please process data first.'
        try:
            numeric_data = self.data.select_dtypes(include='number')
            summary = {
                'Mean': numeric_data.mean().to_dict(),
                'Median': numeric_data.median().to_dict()
            }
            return summary
        except ValueError:
            return 'Data contains non-numeric values. Please process data again.'
        except Exception as e:
            return f'Error generating summary: {e}'


# Example usage
school_system = SchoolAssessmentSystem()

# Process data
data_process = school_system.process_data('test.csv')
print(f"Data Process Result:\n{data_process}")

# Transfer data
merged_data = school_system.transfer_data(
    criteria='merge', data_from_another_source=pd.read_csv('data.csv'))
print(f"Merge Result:\n{merged_data}")

# Fetch web data
web_data_result = school_system.fetch_web_data(
    'https://www.aupp.edu.kh/assessment')
print(f"Web Data Result:\n{web_data_result}")

# Analyze content
analysis_result = school_system.analyze_content()
print(f"Analysis Result:\n{analysis_result}")

# Generate summary
summary = school_system.generate_summary()
print(f"Summary Result:\n{summary}")
