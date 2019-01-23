cur_path = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
ypath = os.path.join(cur_path, "config",  "token.yaml")
with open(ypath, 'r', encoding='utf-8') as file:
    data = yaml.load(file)
host = data["URL"]
h = {
    "User-Agent":"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; PBEM00 Build/OPM1.171019.026) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Content-Type":"application/x-www-form-urlencoded"
    }

with open("../config/token.yaml", 'r', encoding='utf-8') as file:
    data = yaml.load(file)
    host = data["URL"]