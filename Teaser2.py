#using Pandas dataframe 
import pandas as pd

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',
            'Laura', 'Kelvin', 'Jonas'], 'score': [12.5, 9, 16.5, 'np.nan', 9, 20, 14.5, 
            'np.nan', 8, 19], 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 'quality': ['yes',
            'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
e = pd.DataFrame(exam_data)
print (e)

