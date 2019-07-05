import datetime, requests, time
import pandas as pd

from .helper import states, crime_types, data_types
class StateReport:
    final_data = {}
    def __init__(self, year='', filename=''):
        if year == '':
            year = str(datetime.datetime.now().year)
        else:
            year = str(year)
        self.raw_data_url= f"https://www.ic3.gov/media/annualreport/{year}State/stats?s="
        self.states = states
        self.crime_types = crime_types
        self.filetime = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M")
        self.filename = filename
        print(f"Url is {self.raw_data_url}")
    
    def populate_state_data(self, data):
        state_data = {}
        state_data[data_types[0]] = dict(zip(self.crime_types, data[0][0] + data[0][1]))
        state_data[data_types[1]] = dict(zip(self.crime_types, data[0][2] + data[0][3]))
        state_data[data_types[2]] = dict(zip(self.crime_types, data[0][4] + data[0][5]))
        state_data[data_types[3]] = dict(zip(self.crime_types, data[0][6] + data[0][7]))
        return state_data
    
    def run(self, parse_sleep=.1):
        print("Starting to parse...")
        # Initial call to print 0% progress
        length = len(self.states)
        self.printProgressBar(0, length, prefix = 'Progress:', suffix = 'Complete', length = length)
        try:
            r = requests.get(self.raw_data_url+str(1))
        except:
            pass
        for i,v in enumerate(states, 1):
            r = requests.get(self.raw_data_url+str(i))
            if r.ok:
                data = r.json()
                self.final_data[v] = self.populate_state_data(data)
                time.sleep(parse_sleep)
                self.printProgressBar(i + 1, length, prefix = 'Progress:', suffix = 'Complete', length = length)
            else:
                print("r.ok", r.ok)
                assert False, "Couldn't get response from server try running url with hand"
            break
        print("Finished parsing...")
        print("You can access raw data with final_data or Extract using extract")
        
    def extract(self, sheeted=True, to=''):
        """
            Create excel file
            sheeted: If true create new sheet for every country
            to: XLSX, CSV, XLS 
        """       
        if to == '':
            to = 'xlsx'
        print(f"Extracting file... [sheeted={sheeted}|to={to}]")
        if sheeted: #write xlsx anyway
            filename = self.filetime + '.xlsx'
            writer = pd.ExcelWriter(filename, engine='xlsxwriter')
            for state,d in self.final_data.items():
                # states.append(state)
                df = pd.DataFrame.from_dict(d)
                if len(state) >= 31:
                    state = state[:30]
                df.to_excel(writer, sheet_name=state)
            writer.save()
            print(f"Extracted sheeted to {filename}")
        else: #grouped
            states = []
            frames = []
            filename = self.filetime + '.' + to
            for state,d in self.final_data.items():
                states.append(state)
                frames.append(pd.DataFrame.from_dict(d))
            country_based = pd.concat(frames, keys=states)
            if to == 'xlsx':
                country_based.to_excel(filename, engine='xlsxwriter')
            elif to == 'csv':
                country_based.to_csv(filename)
            print(f"Extracted to {filename}")
    
    def printProgressBar (self, iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
        # Print New Line on Complete
        if iteration == total: 
            print()

            
