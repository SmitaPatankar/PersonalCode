#### Installation
```
pip install {toolname}
```

#### coverage
```
coverage run --branch --source {path} --omit {path} -m pytest
coverage report --show-missing
```

#### flake8
```
flake8 --config .flake8 {path}
```

```
cat .flake8

[flake8]
max_line_length = 99
max_complexity = 10
ignore = E133,D203,D213,W503
select = E,F,W,C,Q,N,D,D212,D404,A,M
```

#### black
```
black {path}
```