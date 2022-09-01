## Dota2 解析プログラム

### Import


```python
import dota2gsi
```

### Demo program

まずはDota2と接続していることを確認．

```python
def demo_handle_state(last_state, state):
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
server = dota2gsi.Server(ip='0.0.0.0', port=3000)
server.on_update(demo_handle_state)
server.start()

```

    DotA 2 GSI server listening on 0.0.0.0:3000 - CTRL+C to stop
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    clock_time:2887, health:1020, gold:1, mana:375,  level:7,  xpm:72, 
    Server stopped.
    

### Read data name file

#### Create data id csv

detaのIDリストのファイルを作成します．

```bash
player
assists
camps_stacked
deaths
denies
gold
gold_reliable
gold_unreliable
gpm
hero_damage
kill_list:victimid_#
kill_streak
kills
last_hits
net_worth
pro_name
runes_activated
support_gold_spent
wards_destroyed
wards_placed
wards_purchased
xpm
```

#### Glob file

csv ファイルを探索します．

```python
import glob
import pandas as pd

datasets_path = "datasets"
data_file_list = glob.glob(datasets_path + "/*.csv")
```

ファイル一覧です．

```python
data_file_list
```
```bash
    ['datasets\\hero.csv', 'datasets\\player.csv']
```

#### Read file

CSVファイルを読み込みます．

```python
for file_path in data_file_list:
    df_data = pd.read_csv(file_path)
    
    print("---------------------")
    print(df_data.head(5))
```

```bash
    ---------------------
                   hero
    0             alive
    1             break
    2      buyback_cost
    3  buyback_cooldown
    4          disarmed
    ---------------------
              player
    0        assists
    1  camps_stacked
    2         deaths
    3         denies
    4           gold
```

### dataframe2dict

DataFrameを辞書型に変形します．

```python
data_dict = {}

for file_path in data_file_list:
    df_data = pd.read_csv(file_path)
    
    data_dict[df_data.columns[0]] = list(df_data[df_data.columns[0]].values)
```


変形後のデータです．

```python
data_dict
```


```bash
    {'hero': ['alive',
      'break',
      'buyback_cost',
      'buyback_cooldown',
      'disarmed',
      'has_debuff',
      'health',
      'health_percent',
      'hexed',
      'id',
      'level',
      'magicimmune',
      'mana',
      'mana_percent',
      'max_health',
      'max_mana',
      'muted',
      'name',
      'respawn_seconds',
      'selected_unit',
      'silenced',
      'stunned',
      'talent_1',
      'talent_2',
      'talent_3',
      'talent_4',
      'talent_5',
      'talent_6',
      'talent_7',
      'talent_8',
      'xpos',
      'ypos'],
     'player': ['assists',
      'camps_stacked',
      'deaths',
      'denies',
      'gold',
      'gold_reliable',
      'gold_unreliable',
      'gpm',
      'hero_damage',
      'kill_list:victimid_#',
      'kill_streak',
      'kills',
      'last_hits',
      'net_worth',
      'pro_name',
      'runes_activated',
      'support_gold_spent',
      'wards_destroyed',
      'wards_placed',
      'wards_purchased',
      'xpm']}
```


### Get Dota2 data

ここから，Dota2のデータを取得します．

#### data name loop

先ほどの辞書からデータの名前を1つづ取り出すコードを作成します．

```python
for data_kind_name in data_dict.keys():
    print("===================")
    print(data_kind_name)
    print("--------------------")
    for data_name in data_dict[data_kind_name]:
        print(data_name)
        #hero_name = state.get(data_kind_name, {}).get(data_name)
```

```bash
    ===================
    hero
    --------------------
    alive
    break
    buyback_cost
    buyback_cooldown
    disarmed
    has_debuff
    health
    health_percent
    hexed
    id
    level
    magicimmune
    mana
    mana_percent
    max_health
    max_mana
    muted
    name
    respawn_seconds
    selected_unit
    silenced
    stunned
    talent_1
    talent_2
    talent_3
    talent_4
    talent_5
    talent_6
    talent_7
    talent_8
    xpos
    ypos
    ===================
    player
    --------------------
    assists
    camps_stacked
    deaths
    denies
    gold
    gold_reliable
    gold_unreliable
    gpm
    hero_damage
    kill_list:victimid_#
    kill_streak
    kills
    last_hits
    net_worth
    pro_name
    runes_activated
    support_gold_spent
    wards_destroyed
    wards_placed
    wards_purchased
    xpm
    
```
#### Define handle

これをハンドラーに組み込みます．

```python
def realtime_handle_state(last_state, state):
    # Use nested gets to safely extract data from the state
    
    for data_kind_name in data_dict.keys():
        print("===================")
        print(data_kind_name)
        
        for data_name in data_dict[data_kind_name]:
            print("--------------------")
            print(data_name)
            data_value = state.get(data_kind_name, {}).get(data_name)
            print(data_value)
    
    
```

#### Run server test

サーバーを起動させます．

```python
server = dota2gsi.Server(ip='0.0.0.0', port=3000)
server.on_update(realtime_handle_state)
server.start()
```
```bash
    DotA 2 GSI server listening on 0.0.0.0:3000 - CTRL+C to stop
    ===================
    hero
    --------------------
    alive
    True
    --------------------
    break
    False
    --------------------
    buyback_cost
    233
    ．．．．
    None
    --------------------
    wards_destroyed
    None
    --------------------
    wards_placed
    None
    --------------------
    wards_purchased
    None
    --------------------
    xpm
    23
    Server stopped.
   ．．．．． 
```
これでデータ取得する部分ができました．

### Adjust state data

次に，取得したデータを整形していきます．
stateから1行のDataFrameに変形します．

```python
def state2df(state):
    
    df_list = []
    for data_kind_name in data_dict.keys():
        #print("===================")
        #print(data_kind_name)
        
        data_name_list = []
        data_value_list = []
        
        for data_name in data_dict[data_kind_name]:
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
    print(df_merge)
    
```

これを新しいハンドラ2を作成し組み込みます．

```python
def realtime_handle_state2(last_state, state):
    # Use nested gets to safely extract data from the state
    df_state = state2df(state)
    
    df_data_base = pd.concat([df_data_base, df_state])
    print(df_data_base)
```
以上を踏まえてクラスを作成します．


### Define class

stateを取得し，DataFrameに変形するクラスです．

#### 定期的保存機能

30秒ごとに保存する機構を加えます．
これで，後から解析できます．

```python
if(self.df_data_base['clock_time'].values[-1] % 30 == 0):
    print("===================")
    print(self.df_data_base['clock_time'].values[-1])
    print(self.df_data_base.tail(5))
    self.df_data_base.to_csv('log_{}.csv'.format(self.df_data_base['matchid'].values[-1]))

```
#### コード全体

```python
import dota2gsi
import glob
import csv
import pprint
pd.set_option('display.max_columns', 5)

class Dota2Analy:
    
    def __init__(self, funname="dota2"):
        self.funname = funname
        
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

        self.df_data_base = pd.concat([self.df_data_base, df_state])
        
        
        if(self.df_data_base['clock_time'].values[-1] % 30 == 0):
            print("===================")
            print(self.df_data_base['clock_time'].values[-1])
            print(self.df_data_base.tail(5))
            self.df_data_base.to_csv('log_{}.csv'.format(self.df_data_base['matchid'].values[-1]))
        
    def run(self):
        server = dota2gsi.Server(ip='0.0.0.0', port=3000)
        server.on_update(self._realtime_handle_state2)
        server.start()

if __name__ == '__main__':
    D2A = Dota2Analy()
    D2A.run()
```

実行するとこのように，時刻ごとに追加されていきます．

```bash
    DotA 2 GSI server listening on 0.0.0.0:3000 - CTRL+C to stop
    ===================
    270
      alive  break  ... wards_purchased    xpm
    0  True  False  ...             NaN  328.0
    0  True  False  ...             NaN  328.0
    0  True  False  ...             NaN  328.0
    0  True  False  ...             NaN  328.0
    0  True  False  ...             NaN  327.0
    
    [5 rows x 66 columns]
    ===================
    270
      alive  break  ... wards_purchased    xpm
    0  True  False  ...             NaN  328.0
    0  True  False  ...             NaN  328.0
    0  True  False  ...             NaN  328.0
    0  True  False  ...             NaN  327.0
    0  True  False  ...             NaN  327.0
    
    [5 rows x 66 columns]
    ．．．．
```

## おわりに

今回は，Dota2からstateを取得し，csvに記載されているIDを使ってデータを取得しました．
取得したデータが1行のDataFrameに変形し追加し，定期的に保存する機構を作ることができました．

次回は保存したデータをプロットしていこうと思います．


