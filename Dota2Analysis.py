import dota2gsi
import glob
import csv
import pprint
import pandas as pd
from datetime import datetime as dt

pd.set_option('display.max_columns', 5)

class Dota2Analy:
    
    def __init__(self, funname="dota2"):
        self.funname = funname
        
        tdatetime = dt.now()
        self.tstr = tdatetime.strftime('%Y%m%d-%H%M%S')
        
        self.df_data_base = pd.DataFrame({})
        
        datasets_path = "datasets"
        data_file_list = glob.glob(datasets_path + "/*.csv")
        
        # --------------------------------------
        self.data_dict = {}
        for file_path in data_file_list:
            df_data = pd.read_csv(file_path)
            self.data_dict[df_data.columns[0]] = list(df_data[df_data.columns[0]].values)
            
        

    def state2df(self, state):

        df_list = []
        for data_kind_name in self.data_dict.keys():
            #print("===================")
            #print(data_kind_name)

            data_name_list = []
            data_value_list = []

            for data_name in self.data_dict[data_kind_name]:
                #print("--------------------")
                #print(data_name)
                data_name_list.append(data_name)
                data_value = state.get(data_kind_name, {}).get(data_name)
                #print(data_value)
                data_value_list.append(data_value)

            #df_data = pd.Dataframe(data_value_list)
            df_data = pd.DataFrame(data_value_list).T
            df_data.columns = data_name_list
            #print(df_data)
            df_list.append(df_data)

        df_merge = pd.concat(df_list, axis=1)
        #print(df_merge)
        return df_merge

    def _realtime_handle_state2(self, last_state, state):
        # Use nested gets to safely extract data from the state
        df_state = self.state2df(state)
        
        if df_state['clock_time'].values[-1]:
            self.df_data_base = pd.concat([self.df_data_base, df_state])
            
            if(self.df_data_base['clock_time'].values[-1] % 30 == 0):
                print("===================")
                print(self.df_data_base['clock_time'].values[-1])
                print(self.df_data_base.tail(5))
                self.df_data_base.to_csv('log_{}.csv'.format(self.tstr))
        
    def run(self):
        server = dota2gsi.Server(ip='0.0.0.0', port=3000)
        server.on_update(self._realtime_handle_state2)
        server.start()

if __name__ == '__main__':
    D2A = Dota2Analy()
    D2A.run()