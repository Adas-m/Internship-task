from CSVRead import CSVRead
import datetime

##### TASK 1 - Retrieve the customer with the earliest check in date.###############################################
def retreive_earliest_checkin(csvreader: CSVRead):
    earliest_date = datetime.datetime.max
    person_name = ''
    for index, row in enumerate(csvreader.get_data()):
        try:
            date = datetime.datetime.strptime(row[6], "%d/%m/%Y")
            if date < earliest_date:
                earliest_date = date
                person_name = f'{row[0]} {row[1]}'
        except Exception as e:
            csvreader.logger.error(f'Wrong date format or empty date field, for row number {index+1}')
    return person_name

##### TASK 2 - Retrieve the customer with the latest check in date.###############################################
def retreive_latest_checkin(csvreader: CSVRead):
    latest_date = datetime.datetime.min
    person_name = ''
    for index, row in enumerate(csvreader.get_data()):
        try:
            date = datetime.datetime.strptime(row[6], "%d/%m/%Y")
            if date > latest_date:
                latest_date = date
                person_name = f'{row[0]} {row[1]}'
        except Exception as e:
            csvreader.logger.error(f'Wrong date format or empty date field, for row number {index+1}')
    return person_name

##### TASK 3 - Retrieve a list of customer’s full names ordered alphabetically.###############################################
def retreive_customers_names(csvreader: CSVRead):
    customers_names = [f'{row[0]} {row[1]}' for row in csvreader.get_data() if row[0] != '' and row[1] != '']
    customers_names.sort()
    return customers_names

##### TASK 4 - Retrieve a list of the companies user’s jobs ordered alphabetically.###############################################
def retreive_companies_users_jobs(csvreader: CSVRead):
    jobs = [row[7] for row in csvreader.get_data() if row[7] != '']
    jobs.sort()
    return jobs


##### TESTING #####
x = CSVRead('Sample test file - Sheet1.csv')
print(retreive_latest_checkin(x))
