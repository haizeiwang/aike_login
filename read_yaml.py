import yaml


def get_data():
    with open("./data/data_login.yaml", "r", encoding="utf-8") as i:
        data = yaml.load(i)
        return data


if __name__ == '__main__':
    list = []
    datas = get_data()
    for data in datas.values():
        list.append((data.get("username"), data.get("pwd")))
    print(list)
