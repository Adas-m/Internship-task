import csv
import logging as log

############################### LOGGER SET UP #####################################
###################################################################################
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
log.basicConfig(filename = "Solution.log", format = LOG_FORMAT, filemode = 'w')
logger = log.getLogger()
###################################################################################

class CSVRead:
    # Constructor - creates a CSVReader object and uses the read() method.
    def __init__(self, csv_file_path):
        try:
            self.csv_file = csv.reader(open(csv_file_path))
        except Exception as e:
            print(e)
        self.read()

    # This method iterates over the file using CSVReader, and stores the data as a tuple of elements.
    # It also uses a logger to log the necessary information into a .log file.
    def read(self):
        self.data = []
        # I use next() to skip the header row.
        next(self.csv_file)
        for index, row in enumerate(self.csv_file):
            self.data.append(row)
            # Check whether every data item in a row is empty.
            if row.count('') == len(row):
                logger.warning(f'Row number {index} doesn\'t contain any data')
                continue
            # Check if any of the required fields are empty.
            if row[2] == '' or row[3] == '' or row[4] == '' or row[6] == '' or row[9] == '':
                logger.warning(f'Row number {index} contains an empty required field.')
                continue
            # Check if any row contains less fields than expected.
            if len(row) < 10:
                logger.warning(f'Row number {index} contains less fields than expected.')
        self.data = tuple(self.data)

    # A simple getter method.
    def get_data(self):
        return self.data