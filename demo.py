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
