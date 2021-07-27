import yaml
try:
    stack = yaml.safe_load(open("C://Users//7000019522//Downloads//docker-stack.yml").read())
except:
    print("issue")
else:
    print("successful")

# successful
