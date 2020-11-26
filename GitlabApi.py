import gitlab
import xlwt
# import time
import datetime

url = 'https://gitlab.daynine.top/'
token='123456'

#统计最近三天的日志
dt = datetime.datetime.now()
paramDt = dt + datetime.timedelta(-1)
querystr = paramDt.strftime('%Y-%m-%d 00:00:00')
datestr = dt.strftime('%Y-%m-%d')


def genenrate_worklog_excel():
    w = xlwt.Workbook(encoding='utf-8')
    return w;


def generate_worklog_sheet(workbook,sheetName):
    sheet = workbook.add_sheet(sheetName)
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
    width_col = sheet.col(0)       #xlwt中是行和列都是从0开始计算的
    width_col.width = 256*10
    width_col=sheet.col(1)
    width_col.width=256*30
    width_col=sheet.col(2)
    width_col.width=256*20
    width_col=sheet.col(3)
    width_col.width=256*22
    width_col=sheet.col(4)
    width_col.width=256*15
    width_col=sheet.col(5)
    width_col.width=256*15
    width_col=sheet.col(6)
    width_col.width=256*25
    width_col=sheet.col(7)
    width_col.width=256*70
    width_col=sheet.col(8)
    width_col.width=256*10
    width_col=sheet.col(9)
    width_col.width=256*80
    tall_style = xlwt.easyxf('font:height 580;') # 36pt,类型小初的字号
    first_row = sheet.row(0)
    first_row.set_style(tall_style)

    style = xlwt.XFStyle()
    style.alignment.wrap = 1  #设置自动换行
    return sheet


def export_worklog_sheet(gl,sheet):
    ccount = 0
    # 列出所有的项目
    projects = gl.projects.list()
    for project in projects:
        print(project)
        branches = project.branches.list()
        for branchItem in branches:
            print(branchItem)
            commits = project.commits.list(ref_name=branchItem.name, since=querystr, page=0, per_page=2000)
            for commitItem in commits:
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


def write_worklog_file(workboot,filename):
    workboot.save(filename)


# 登录
def connect_login_gitlab(giturl,accesstoken):
    gl = gitlab.Gitlab(giturl, private_token=accesstoken)
    return gl;

# 登录
def connect_login_gitlab_with_config():
    gl = gitlab.Gitlab.from_config('git', ['./config.cfg'])
    return gl;


def query_gitlab_users(gl):
    return gl.users.list(all=True)




connect_login_gitlab_with_config()
w = genenrate_worklog_excel()
sheet = generate_worklog_sheet(w,datestr)
#gl = connect_login_gitlab(url,token)
gl = connect_login_gitlab_with_config()
export_worklog_sheet(gl,sheet)
export_filename = '/Users/shiaihua/Desktop/xls/开发日志/开发工作日志'+datestr + '.xls'
write_worklog_file(w,export_filename)

