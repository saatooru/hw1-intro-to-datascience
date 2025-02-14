import json
def kwargsAcceptFun(**kwargs):
    json_output = json.dumps(kwargs, indent=4)
    print(json_output)
kwargsAcceptFun(name="New Uzbekistan University", ranking=999, students_count=1000)
