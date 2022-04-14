from rderp.md.material import Material
from rderp.model import Model

app2 = Material(acct_id='623c094620dfbd', user_name='胡立磊', app_id='225823_2f1MXZsE5lmZTXxLwd0q3c/MVt1XwqNp',
               app_secret='e69e4a3631ce4b4280975ee596286e0a', server_url='http://cellprobio.gnway.cc/k3cloud/')
app = Model(token="AD64F20D-6063-4E87-81E8-A24C1751D758",FFormId = 'BD_MATERIAL',FActionName='Save')
op2 = app.dataGen()
# print(op2)
#不填表示新增
#op2 = app.setValue(option=op2, FMainKey='FMATERIALID', FValue='262208')
#填写表示修改
op2 = app.setValue(option=op2, FMainKey='FCreateOrgId', FValue='100')
op2 = app.setValue(option=op2, FMainKey='FUseOrgId', FValue='100')
op2 = app.setValue(option=op2, FMainKey='FNumber', FValue='PRD-03')
op2 = app.setValue(option=op2, FMainKey='FName', FValue='演示物料3')
op2 = app.setValue(option=op2, FMainKey='F_SZSP_CPDL', FValue='1')
print(op2)
#op2 = app.setValue(option=op2, FMainKey='FErpClsID', FValue=1)
#op2 = app.setValue(option=op2, FMainKey='FMinIssueUnitId', FValue='123')
#op2 = app.setValue(option=op2, FMainKey='FPurchaseUnitId', FValue='carton')
#op2 = app.setValue(option=op2, FMainKey='FPurchasePriceUnitId', FValue='carton')
#op2 = app.setValue(option=op2, FMainKey='FMinIssueUnitId', FValue='carton')


res = app2.Save(data=op2)
print(res)
