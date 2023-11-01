import requests


poem1 = {
    'poem_name':'静夜思',
    'poem_author':'李白',
    'poem_dynasty':'唐',
    'poem_type':'五言绝句',
    'poem_content':'床前明月光，疑是地上霜。举头望明月，低头思故乡。'
}

# with requests.post('http://127.0.0.1:5000/poem',json=poem1) as response:
#     print(response.json())


with requests.get('http://127.0.0.1:5000/poem') as response:
    print(response.json())
#
#
# with requests.delete('http://127.0.0.1:5000/poem/1') as response:
#     print(response.text)