import dota2gsi
import glob
import csv
import pprint

class Dota2Analy:
    
    def __init__(self, funname="dota2"):
        self.funname = funname
        
        self.data_file_list = glob.glob("./datasets/*.csv")
        print(self.data_file_list)
        
        self.data_name_dict = {}
        
        
        for file_path in self.data_file_list:
            data_name_list = []
            with open(file_path) as f:
                reader = csv.reader(f)
                for row in reader:
                    data_name_list.extend(row)
                # data_name_list.append(f.read())
                print(data_name_list)
                self.data_name_dict[file_path.split("\\")[-1].split(".csv")[0]] = data_name_list
                # print(l)
        
        pprint.pprint(self.data_name_dict)

    def _handle_state(self, last_state, state):
        # Use nested gets to safely extract data from the state
        hero_name = state.get('hero', {}).get('name')
        health_percent = state.get('hero', {}).get('health_percent')
        max_health = state.get('hero', {}).get('max_health')
        max_health = state.get('hero', {}).get('max_health')
        health = state.get('hero', {}).get('health')
        level = state.get('hero', {}).get('level')
        mana = state.get('hero', {}).get('mana')
        mana_percent = state.get('hero', {}).get('mana_percent')
        gold = state.get('player', {}).get('gold')
        xpm = state.get('player', {}).get('xpm')
        
        clock_time = state.get('map', {}).get('clock_time')
        
        # If the attributes exist, print them
        if health_percent and max_health:
            health = int(max_health * health_percent/100)
            # print(f"{hero_name}'s current health: {health}/{max_health}")
            print("{}:{}, {}:{}, {}:{}, {}:{},  {}:{},  {}:{}, ".format("clock_time", clock_time, "health", health, "gold", gold, "mana", mana, "level", level, "xpm", xpm))
            
    def run(self):
        server = dota2gsi.Server(ip='0.0.0.0', port=3000)
        server.on_update(self._handle_state)
        server.start()

if __name__ == '__main__':
    D2A = Dota2Analy()
    D2A.run()