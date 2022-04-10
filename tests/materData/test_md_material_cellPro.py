from rderp.md.material import Material
from rderp.model import Model

app2 = Material(acct_id='623c094620dfbd', user_name='胡立磊', app_id='225823_2f1MXZsE5lmZTXxLwd0q3c/MVt1XwqNp',
               app_secret='e69e4a3631ce4b4280975ee596286e0a', server_url='http://cellprobio.gnway.cc/k3cloud/')
app = Model(token="EDCFD199-AF57-4591-8BA9-CD44415B816B",FFormId = 'BD_MATERIAL',FActionName='Save')
op2 = app.dataGen()
op2 = app.setValue(option=op2, FMainKey='FNumber', FValue='PRD-01')
op2 = app.setValue(option=op2, FMainKey='FName', FValue='演示物料')
op2 = app.setValue(option=op2, FMainKey='FErpClsID', FValue=1)
op2 = app.setValue(option=op2, FMainKey='FMinIssueUnitId', FValue='123')
op2 = app.setValue(option=op2, FMainKey='FPurchaseUnitId', FValue='carton')
op2 = app.setValue(option=op2, FMainKey='FPurchasePriceUnitId', FValue='carton')
op2 = app.setValue(option=op2, FMainKey='FMinIssueUnitId', FValue='carton')
print(op2)
res = app2.Save(data=op2)
print(res)