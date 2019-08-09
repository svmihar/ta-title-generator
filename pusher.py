import os 
from datetime import datetime

pre_message = f'[AUTO GENERATED] {datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}'

os.system('git add .')

# c_m = input('commit message: \n>')
c_m = False
if c_m: 
    os.system(f"git commit -m '{c_m}'")
else: 
    os.system(f'git commit -m "{pre_message}"')

os.system('drive add_remote')
# os.system('git push origin master')
# os.system('git push mirror master')


# drive = input('do you want to upload to google drive y/n? (default is n)')
# if drive.lower() == 'y': 
#     os.system('drive add_remote')
# else: 
#     print('you\'re done')