import dota2gsi
import glob
import csv
import pprint
import pandas as pd
import os
from datetime import datetime as dt
import json
from loguru import logger

pd.set_option('display.max_columns', 5)

class Dota2Analy:
    
    def __init__(self, funname="dota2"):
        self.funname = funname
        
        ##############################################
        # setting param
        #
        tdatetime = dt.now()
        self.log_dir    = "logs"
        self.tstr       = tdatetime.strftime('%Y%m%d_%H%M%S')
        self.tag        = "v2"
        self.save_dir   = "{}/{}/{}".format(self.log_dir, self.tag, self.tstr) 
        self.time_offset = 80
        
        os.makedirs(self.save_dir, exist_ok=True)
        

    def _realtime_handle_state2(self, last_state, state):

        ##############################################
        # save timestamp
        #
        dt_now = dt.now()
        tstr       = dt_now.strftime('%Y%m%d_%H%M%S')
        save_file_path = "{}/{}.json".format(self.save_dir, tstr)
        
        ##############################################
        # logger
        #
        logger.info(save_file_path)
        
        ##############################################
        # save json
        #
        with open(save_file_path, 'w') as f:
            json.dump(state, f, indent=4)
        
    def run(self):
        server = dota2gsi.Server(ip='0.0.0.0', port=3000)
        server.on_update(self._realtime_handle_state2)
        server.start()

if __name__ == '__main__':
    D2A = Dota2Analy()
    D2A.run()