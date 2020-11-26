import gitlab
import xlwt
# import time
import datetime

url = 'https://localhost:3000/'
token='b128a8d280aa2c63d431578ae270189efc6ee41d'

token = gogs_client.Token("my_token")
username = "username"  # username of owner of repo
repository_name = "repo_name"

api = GogsApi("https://try.gogs.io/")

if not api.repo_exists(token, username, repository_name):
    print("Repository does not exist")
else:
    repo = api.lookup_repo(token, username, repository_name)
    if repo.fork:
        print("Repository is a fork")
    else:
        print("Repository is not a fork")



dt = datetime.datetime.now()
paramDt = dt + datetime.timedelta(-3)
#querystr = paramDt.strftime('%Y-%m-%d %H:%M:%S')
querystr = paramDt.strftime('%Y-%m-%d 00:00:00')
datestr = dt.strftime('%Y-%m-%d')


w = xlwt.Workbook(encoding='utf-8')
sheet = w.add_sheet(datestr)
sheet.write(0, 0, '序号')
sheet.write(0, 1, '提交id')
sheet.write(0, 2, '账号')
sheet.write(0, 3, '邮箱')
sheet.write(0, 4, '项目')
sheet.write(0, 5, '分支')
sheet.write(0, 6, '提交时间')
sheet.write(0, 7, '工作内容')
sheet.write(0, 8, '文件数')
sheet.write(0, 9, '文件信息')
widthCol = sheet.col(0)       #xlwt中是行和列都是从0开始计算的
widthCol.width = 256*10
widthCol=sheet.col(1)
widthCol.width=256*30
widthCol=sheet.col(2)
widthCol.width=256*20
widthCol=sheet.col(3)
widthCol.width=256*22
widthCol=sheet.col(4)
widthCol.width=256*15
widthCol=sheet.col(5)
widthCol.width=256*15
widthCol=sheet.col(6)
widthCol.width=256*25
widthCol=sheet.col(7)
widthCol.width=256*70
widthCol=sheet.col(8)
widthCol.width=256*10
widthCol=sheet.col(9)
widthCol.width=256*80
tall_style = xlwt.easyxf('font:height 580;') # 36pt,类型小初的字号
first_row = sheet.row(0)
first_row.set_style(tall_style)

style = xlwt.XFStyle()
style.alignment.wrap = 1  #设置自动换行

# 登录
gl = gitlab.Gitlab(url, private_token=token)
all_users = gl.users.list(all=True)


ccount = 0
# 列出所有的项目
projects = gl.projects.list()
for project in projects:
    print(project)
    branches = project.branches.list()
    for branchItem in branches:
        print(branchItem)
        commits = project.commits.list(ref_name=branchItem.name,since=querystr, page=0, per_page=2000)
        for commitItem in commits:
            #print(commitItem)
            #print(commitItem.message)
            ccount += 1
            sheet.write(ccount, 0, ccount)
            sheet.write(ccount, 1, commitItem.id)
            sheet.write(ccount, 2, commitItem.author_name)
            sheet.write(ccount, 3, commitItem.author_email)
            sheet.write(ccount, 4, project.name)
            sheet.write(ccount, 5, branchItem.name)
            dateTime_p = datetime.datetime.strptime(commitItem.created_at, '%Y-%m-%dT%H:%M:%S.000Z')
            dateTIme_s = datetime.datetime.strftime(dateTime_p, '%Y-%m-%d %H:%M:%S')
            sheet.write(ccount, 6, dateTIme_s)
            sheet.write(ccount, 7, commitItem.message)
            diff = commitItem.diff()

            diffcount = 0;
            mydiffpath = '';
            for diffItem in diff:
                print(diffItem);
                mydiffpath = mydiffpath + ";\r" + diffItem['new_path']
                diffcount += 1
            sheet.write(ccount, 8, diffcount)
            sheet.write(ccount, 9, mydiffpath)
            data_tall_style = xlwt.easyxf('font:height 320;')  # 36pt,类型小初的字号
            data_row = sheet.row(ccount)
            data_row.set_style(data_tall_style)


w.save('/Users/shiaihua/Desktop/xls/开发日志/Gogs开发工作日志'+datestr + '.xls')


