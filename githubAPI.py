import requests
import githubBot

#url
py_url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
java_url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'

temp_url = 'https://api.github.com/search/repositories?q=language:'

###

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

py_sourse = {key: value for key, value in zip(py_names, py_repositorys)}


#java#
java_r = requests.get(java_url)
java_response_dict =java_r.json()
java_repo_dicts = java_response_dict['items']

java_names, java_repository, java_desriptions = [], [], []

for java_repo_dict in java_repo_dicts:
        java_names.append(java_repo_dict['name'])
        java_repository.append(java_repo_dict['html_url'])
        java_desriptions.append(java_repo_dict['description'])
