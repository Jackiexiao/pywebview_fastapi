# FastApi + pywebview + Vue3 + Vite Demo

简单的 FastApi + pywebview + Vue3 + Vite 的示例项目, 可生成一个桌面应用程序

## Usage
```bash
# 首先确保你已经安装了 pnpm / nodejs
# install
pip install -r requirements.txt
cd frontend/ && pnpm install

# 启动开发模式后端
python manage.py start

# 打包项目, 然后在 dist/ 目录下查看生成的应用程序
python manage.py build
```