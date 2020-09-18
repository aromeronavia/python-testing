## Setup
```sh
$ pyenv virtualenv 3.7.1 testing-workshop
$ pyenv activate testing-workshop
$ pip install -r requirements.txt
$ npm install -g nodemon
$ nodemon --ext py --exec "pytest src/**"
```
