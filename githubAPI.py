import requests
import githubBot

#url
py_url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
java_url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'

books_url = 'https://api.github.com/search/repositories?q=books'

#temp_url = 'https://api.github.com/search/repositories?q=language:{}'.format(githubBot.user_dict)

###
books_r = requests.get(books_url)
books_response_dict = books_r.json()
books_repo_dicts = books_response_dict['items']

books_names, books_repositorys, books_desriptions = [], [], []

for books_repo_dict in books_repo_dicts:
        books_names.append(books_repo_dict['name'])
        books_repositorys.append(books_repo_dict['html_url'])
        books_desriptions.append(books_repo_dict['description'])      


###

#python#
py_r = requests.get(py_url)
py_response_dict = py_r.json()
py_repo_dicts = py_response_dict['items']

py_names, py_repositorys, py_desriptions = [], [], []

for py_repo_dict in py_repo_dicts:
        py_names.append(py_repo_dict['name'])
        py_repositorys.append(py_repo_dict['html_url'])
        py_desriptions.append(py_repo_dict['description'])      

#py_sourse = {key: value for key, value in zip(py_names, py_repositorys)}


#java#
java_r = requests.get(java_url)
java_response_dict =java_r.json()
java_repo_dicts = java_response_dict['items']

java_names, java_repository, java_desriptions = [], [], []

for java_repo_dict in java_repo_dicts:
        java_names.append(java_repo_dict['name'])
        java_repository.append(java_repo_dict['html_url'])
        java_desriptions.append(java_repo_dict['description'])

'''
#temp_url#
temp_url_r = requests.get(temp_url)
temp_url_response_dict = temp_url_r.json()
temp_url_repo_dicts = temp_url_response_dict['items']

temp_url_names, temp_url_repository, temp_url_desriptions = [], [], []

for temp_url_repo_dict in temp_url_repo_dicts:
        temp_url_names.append(temp_url_response_dict['name'])
        temp_url_repository.append(temp_url_repo_dict['html_url'])
        temp_url_desriptions.append(temp_url_repo_dict['description'])
'''