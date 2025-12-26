from google import genai
import inspect
c = genai.Client()
print('\n'.join([a for a in dir(c.models) if not a.startswith('_')]))
print('\n--- signature ---')
print(inspect.signature(c.models.generate_content))
print('\n--- doc ---')
print(c.models.generate_content.__doc__[:400])
print('\n--- response type attrs ---')
print('\n'.join(a for a in dir(genai.types.GenerateContentResponse) if not a.startswith('_')))
