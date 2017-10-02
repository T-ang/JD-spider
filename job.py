#coding:utf-8
import sys,requests,json,time,csv
reload(sys)
sys.setdefaultencoding('utf-8')

csvfile = open('jobinfo.csv','wb')

for pageno in range(1,6):

    post_data = {'first':'false','kd':'SEO','pn':pageno}
    r = requests.post("http://www.lagou.com/jobs/positionAjax.json?px=new&city=%E6%88%90%E9%83%BD", data=post_data) 
    detail = json.loads(r.text)
    
    for id in range(0,15):
        companyName = detail['content']['positionResult']['result'][id]['companyShortName']
        Salary = detail['content']['positionResult']['result'][id]['salary']
        Field = detail['content']['positionResult']['result'][id]['industryField']
        Stage = detail['content']['positionResult']['result'][id]['financeStage']
        Advantage = detail['content']['positionResult']['result'][id]['positionAdvantage']
        positionName = detail['content']['positionResult']['result'][id]['positionName']
        CreateTime = detail['content']['positionResult']['result'][id]['formatCreateTime']
        
        data = []
        data.append(CreateTime)
        data.append(positionName)
        data.append(Salary)
        data.append(companyName)
        data.append(Field)
        data.append(Stage)
        data.append(Advantage)

        writer = csv.writer(csvfile,dialect='excel')
        writer.writerow(data)
csvfile.close()