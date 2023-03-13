from jinja2 import Environment, FileSystemLoader


testcases = [
    {'testcase_id': 'testcase1', 'result' : 'PASS', 'logs': 'system log sample'},
    {'testcase_id': 'testcase2', 'result': 'FAIL', 'logs': 'system log sample'},
    {'testcase_id': 'testcase3', 'result': 'FAIL', 'logs': 'system log sample'},
]

env = Environment(loader=FileSystemLoader("."))
template = env.get_template('./index.html')

content = template.render(testcases = testcases)
print(content)

f=open("python.html","w")
f.write(content)
f.close()
