import requests
import datetime as dt
from datetime import date

date=date.today()
payload={
  'answers': "[{\"questionId\":\"r6fcb2dea580f46a8ba8183ce74e4e03a\",\"answer1\":\"TON NOM ET PRÉNOM\"},{\"questionId\":\"rd1e6fe77dc974c50b47109eb94d085a1\",\"answer1\":\""+str(date)+"\"},{\"questionId\":\"r3916373d3d07405799e5a456b5b4abdd\",\"answer1\":\"Non\"},{\"questionId\":\"rb182dbc040534f369aef08a41cf95c6a\",\"answer1\":\"Non\"},{\"questionId\":\"r0c04441af0b74d199615ae39b0682847\",\"answer1\":\"Non\"},{\"questionId\":\"r22ca79abadee489da47fa4b913a17858\",\"answer1\":\"Non\"}]"
   }

url_forms="https://forms.office.com/formapi/api/440dc7ad-ee96-48ec-9443-cdbce09e750c/users/03820ac8-9002-4717-9aaf-e16c05414842/forms('rccNRJbu7EiUQ8284J51DMgKggMCkBdHmq_hbAVBSEJUQ1M4VjYyODRHQ1VGV0VMSFBXQVlMWjFXOS4u')/responses"
code=requests.post(url_forms,data=payload)


now=dt.datetime.now()
log=open("D:\\log.txt","a")
log.write('\n')
log.write(str(now)+" Code: "+str(code))
