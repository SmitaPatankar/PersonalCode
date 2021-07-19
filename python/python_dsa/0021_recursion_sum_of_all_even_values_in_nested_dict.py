def total(obj, sum=0):
  for _, v in obj.items():
    if type(v) is int:
      if v % 2 == 0:
        sum += v
    elif type(v) is dict:
      sum += total(v)
  return sum

obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

print(total(obj1))
print(total(obj2))
