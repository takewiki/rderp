from rderp.md.material import Material

app = Material(acct_id='606ada0b30a9e2', user_name='胡立磊', app_id='224986_TY8p2yGs4vg9Xf0tRfSA3a/N6K3d6OlH',
               app_secret='e1e0cdc4e8204d178cc383557e64e959', server_url='http://8.133.163.217/k3cloud/')
data = app.View(Number='01.21.010')
print(data)
# app.Save(FNumber='test.02',FName='demo2')
app.Submit(Numbers=['mtrl_01'])