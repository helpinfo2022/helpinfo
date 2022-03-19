# from muffin import Application
#
# import bd_work
#
# app = Application()
#
#
# def validate(username, password):
#     if username == 'root' and password == 'root':
#         return True
#     return False
#
#
# @app.route("/")
# async def index(request):
#     with open('index.html') as f:
#         page = f.read()
#     return page
#
# @app.route("/login")
# async def login(request):
#     if request.method == 'POST':
#         login_form = await request.form()
#         if validate(login_form['username'], login_form['password']):
#             print(login_form['username'])
#             return f"<p>{login_form['username']}</p>"
#     return '<p>Invalid username or password</p>'
#
# @app.route("/db_add")
# async def db_add(request):
#     if request.method == 'POST':
#         login_form = await request.form()
#         # bd_work.db_write(login_form['username'])
#         # bd_work.db_read()
#         print("helooo")
#         add_to_db = (login_form['id'] + login_form['name']+ login_form['ip']+ login_form['phone'])
#         bd_work.db_write(login_form['id'], login_form['name'],login_form['ip'],login_form['phone'])
#     return add_to_db
#
# @app.route("/db_update")
# async def db_update(request):
#     if request.method == 'POST':
#         login_form = await request.form()
#         bd_work.db_update(login_form['id'], login_form['name'])
#
#         bd_work.db_read()
#     return f'<p>info is updated</p>'
#
# @app.route("/db_delete")
# async def db_delete(request):
#     if request.method == 'POST':
#         login_form = await request.form()
#         # print("helooo")
#         print(login_form['id'])
#         bd_work.db_delete(login_form['id'])
#
#         bd_work.db_read()
#     return f'<p>ID number XX deleted</p>'
#
#
# @app.route("/db_delete/{id}")
# async def db_delete2(request):
#     id = request.path_params.get('id')
#     bd_work.db_delete(id)
#     return f'<p>ID number XX deleted</p>'
#
#
# @app.route("/db_read")
# async def db_read(request):
#     page = '<h1>DataBase return</h1>\n\n<p>----------</p>\n'
#     data = bd_work.db_read2()
#     for line in data:
#         name = line[0]
#         id = line[1]
#         ip = line[2]
#         phone = line[3]
#         button = f"""<form action="/db_delete/{id}" method="POST">
#           <input type="submit" value="Delete from DB">
#         </form>"""
#         page += f'<p>id = {id}</p>\n<p>name = {name}</p>\n<p>ip = {ip}</p>\n<p>phone = {phone}</p>\n\n{button}\n<p>----------</p>'
#     return page
#
#
#
#
