import google.genai as genai
print('--- module attrs ---')
print('\n'.join([a for a in dir(genai) if not a.startswith('_')]))
print('\n--- client module attrs ---')
print('\n'.join([a for a in dir(genai.client) if not a.startswith('_')]))
print('\n--- Client class attrs (first 50) ---')
print('\n'.join(dir(genai.client.Client)[:50]))
