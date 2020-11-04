import pytest
import yaml

def get_envconfig(env):
    with open(f'./data/{env}_env.yaml', encoding='utf-8') as f:
        return yaml.safe_load(f)

@pytest.mark.hogwarts
def test_env(env):
    print(f'你在命令行输入env的值是：{env}')
    # 根据不同的环境，读取不同的配置文件来获取配置数据
    print(get_envconfig(env))
