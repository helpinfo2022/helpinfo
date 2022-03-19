from muffin import Application

import bd_work

app = Application()


def validate(username, password):
    if username == 'root' and password == 'root':
        return True
    return False


# @app.route("/")
# async def index(request):
#     with open('index.html') as f:
#         page = f.read()
#     return page

@app.route("/login")
async def login(request):
    if request.method == 'POST':
        login_form = await request.form()
        if validate(login_form['username'], login_form['password']):
            print(login_form['username'])
            return f"<p>{login_form['username']}</p>"
    return '<p>Invalid username or password</p>'

@app.route("/db_add")
async def db_add(request):
    if request.method == 'POST':
        login_form = await request.form()

        if login_form['id'].isnumeric()==False :
            return "it is not integer <br><a href=/>GO to index<</a>"

        add_to_db = (login_form['id']+" " + login_form['name']+" " + login_form['ip']+" " + login_form['phone'])
        bd_work.db_write(login_form['id'], login_form['name'], login_form['ip'], login_form['phone'])
        return add_to_db + f'<br>information successfully added to the database<br><a href=/>GO to index<</a>'


@app.route("/db_update")
async def db_update(request):
    if request.method == 'POST':
        login_form = await request.form()

        bd_work.db_update(login_form['id'], login_form['name'], login_form['ip'], login_form['phone'])
        print(login_form['id'], login_form['name'], login_form['ip'], login_form['phone'])
        my_id=login_form['id']
    return f'<p>info {my_id} is updated</p><br><a href=/>GO to index<</a>'




@app.route("/db_delete")
async def db_delete(request):
    if request.method == 'POST':
        login_form = await request.form()
        my_id = login_form['id']
        bd_work.db_delete(login_form['id'])

    return f'<p>ID number {my_id} deleted</p>'


@app.route("/db_delete/{id}")
async def db_delete_by_id(request):
    id = request.path_params.get('id')
    bd_work.db_delete(id)
    return f'<p>ID number {id} deleted</p><br><a href=/>GO to index</a>'

@app.route("/filter_id")
async def filter_id(request):
    if request.method == 'POST':
        login_form = await request.form()
        data = bd_work.db_filter_by_ip(login_form['id'])
        page = '<h1>Filer by id</h1>\n\n<p>----------</p>\n'
        for line in data:
            name = line[0]
            id = line[1]
            ip = line[2]
            phone = line[3]
            page += f'<p>{id} {name} {ip} {phone}</p>'
    return page

@app.route("/filter_ip")
async def filter_ip(request):
    if request.method == 'POST':
        login_form = await request.form()
        data = bd_work.db_filter_by_ip(login_form['ip'])
        page = '<h1>Filer by ip</h1>\n\n<p>----------</p>\n'
        for line in data:
            name = line[0]
            id = line[1]
            ip = line[2]
            phone = lin
            e[3]
            page += f'<p>{line}</p>'
            # page += f'<p>{id} {name} {ip} {phone}</p>'
    return page

@app.route("/filter_name")
async def filter_name(request):
    if request.method == 'POST':
        login_form = await request.form()
        data = bd_work.db_filter_by_name(login_form['name'])
        page = '<h1>Filer by name</h1>\n\n<p>----------</p>\n'
        for line in data:
            name = line[0]
            id = line[1]
            ip = line[2]
            phone = line[3]
            page += f'<p>{id} {name} {ip} {phone}</p>'
    return page

@app.route("/filter_phone")
async def filter_phone(request):
    if request.method == 'POST':
        login_form = await request.form()
        data = bd_work.db_filter_by_ip(login_form['phone'])
        page = '<h1>Filer by phone</h1>\n\n<p>----------</p>\n'
        for line in data:
            name = line[0]
            id = line[1]
            ip = line[2]
            phone = line[3]
            page += f'<p>{id} {name} {ip} {phone}</p>'
    return page



@app.route("/")
async def index(request):
    page = '<h1>Read from DB</h1>\n\n<p>----------</p>\n'
    with open('index.html') as f:
        page = f.read() + page
    data = bd_work.db_read()
    for line in data:
        name = line[0]
        id = line[1]
        ip = line[2]
        phone = line[3]

        button_delete = f"""<form action="/db_delete/{id}" method="POST">
          <input type="submit" value="Delete from DB">
        </form>"""


        page += f"""<p>id = {id}</p>\n
        <form action="/db_update/" method="POST">
        \n
        <p>id     = <input type="text" name="id" value={id} >
        <p>name = <input type="text" name="name" value={name}></p>\n
        <p>ip     = <input type="text" name="ip" value={ip}> </p> \n
        <p>phone = <input type="text" name="phone" value={phone}> </p> \n\n
         <input type="submit" value="UPDATE to DB"></form> \n\n
         
        {button_delete}\n\n<p>----------</p>"""
    return page

