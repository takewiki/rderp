from rderp.model import Model
app = Model(token="EDCFD199-AF57-4591-8BA9-CD44415B816B",FFormId = 'BD_MATERIAL',FActionName='Save')
op2 = app.dataGen()
op2 = app.setValue(option=op2, FMainKey='FNumber', FValue='PRD-01')
op2 = app.setValue(option=op2, FMainKey='FName', FValue='演示物料')
op2 = app.setValue(option=op2, FMainKey='FErpClsID', FValue=1)
op2 = app.setValue(option=op2, FMainKey='FMinIssueUnitId', FValue='123')
print(op2)