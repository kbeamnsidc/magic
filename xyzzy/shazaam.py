from importlib.resources import read_text


template = read_text('plugh', 'scripty_foo.py')
script = template.format(author='Zaphod', planet='x42')

print(script)