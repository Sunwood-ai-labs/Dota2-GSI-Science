# Dota2-GSI-Science

- [1. Introduction](#1-introduction)
  - [1.1. データサイエンスでDota2強くなるかも説](#11-データサイエンスでdota2強くなるかも説)
- [2. Updates!!](#2-updates)
- [3. Coming soon](#3-coming-soon)
- [4. Environment](#4-environment)
- [5. Quick Start](#5-quick-start)
  - [5.1. Game State Integrationの設定](#51-game-state-integrationの設定)
    - [5.1.1. GSIファイルの作成](#511-gsiファイルの作成)
    - [5.1.2. 起動設定](#512-起動設定)
  - [5.2. Pythonとの連携](#52-pythonとの連携)
    - [5.2.1. パッケージのインストール](#521-パッケージのインストール)
    - [5.2.2. サンプルコード](#522-サンプルコード)
    - [5.2.3. データのID](#523-データのid)
    - [5.2.4. 実行結果](#524-実行結果)
- [6. おわりに](#6-おわりに)

## 1. Introduction


最近，Dota2を始めましたが全く勝てません
ハードボットにボコボコにされます．

色々と調べても「死ぬな」くらいのことしか分らず苦戦しています．

### 1.1. データサイエンスでDota2強くなるかも説

そこで，データサイエンスの力を借りて，どのような状況なら勝っているか？や前回に比べてどのように振舞ったから勝てたのか？ということを数値化して分析していけば強くなるのでは！と考えました．本企画はその仮説を検証していく企画です．

## 2. Updates!!

- 【2022/09/01】 初版投稿
- 【2023/01/14】 `state`情報の全部を保存

## 3. Coming soon

- [ ] 可視化ダッシュボードの作成
- [ ] 解析プログラムの作成

## 4. Environment

- Windows11
- Dota2(Steam)
- Python


## 5. Quick Start

### 5.1. Game State Integrationの設定

Game State Integration(以下GSI)はゲーム中のデータを取得するための公式APIで，こちらを使っていきます．

#### 5.1.1. GSIファイルの作成

`gamestate_integration_py.cfg`というファイル名で作成します．

```cfg
"Python Dota 2 GSI Integration"
{
    "uri"       "http://localhost:3000"
    "timeout"   "5.0"
    "buffer"    "0.1"
    "throttle"  "0.1"
    "heartbeat" "30.0"
    "data"
    {
        "provider"  "1"
        "map"       "1"
        "player"    "1"
        "hero"      "1"
        "abilities" "1"
        "items"     "1"
    }
}
```

こちらのファイルをDota2の`cfg`フォルダに`gamestate_integration`フォルダを作成してコピーします．

`cfg`フォルダはsteamの画面からメニューを開いて，ローカルファイル，参照でDota2のフォルダに移動してから

![file](https://hamaruki.com/wp-content/uploads/2022/09/image-1662007168773.png)

`dota 2 beta\game\dota\cfg`この場所にあります．
このフォルダに`gamestate_integration`フォルダを作成して

![file](https://hamaruki.com/wp-content/uploads/2022/09/image-1662007373027.png)

`gamestate_integration_py.cfg`ファイルをコピーします．

![file](https://hamaruki.com/wp-content/uploads/2022/09/image-1662007423662.png)


#### 5.1.2. 起動設定

メニューの一般から起動オプション`-gamestateintegration`を付けます．


![file](https://hamaruki.com/wp-content/uploads/2022/09/image-1662007521159.png)


### 5.2. Pythonとの連携

#### 5.2.1. パッケージのインストール

`dota2gsi`をインストールします．

```bash
pip install dota2gsi==0.1
```

```bash
pip install loguru
```

#### 5.2.2. サンプルコード

体力やマナなど，基本的な情報を取得するコードです．

```python
import dota2gsi

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

#### 5.2.3. データのID

サンプルコードで使用しているIDの詳細はこちらにあります．

https://github.com/xzion/dota2-gsi



#### 5.2.4. 実行結果

実行するとこんな感じで結構早い周期でデータを取得することができます．

```bash
(dota2) D:\Local_Project\5000_HaMaruki\5000.004_Dota2\Dota2-GSI-Science>python demo.py
DotA 2 GSI server listening on 0.0.0.0:3000 - CTRL+C to stop
clock_time:-58, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-57, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-57, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-56, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-56, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-56, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-56, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-56, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-56, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-56, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-56, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-56, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-56, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-56, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-56, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-56, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-56, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-56, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-56, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-56, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-55, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-55, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-55, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-55, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-55, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-55, health:640, gold:250, mana:291,  level:1,  xpm:0, 
clock_time:-55, health:640, gold:250, mana:291,  level:1,  xpm:0, 
Server stopped.

```



## 6. おわりに

こんかいは無事にDota2とPythonを連携させることができました．
次回はもう少し取得するデータを拡張し，データを保存する機構を作っていこうと思います．




