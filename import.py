import pandas as pd
df = pd.read_csv("order_brush_order.csv")

count = df['userid'].value_counts()

# count[count>2].to_dict()
user = []
# shop = df['userid'].value_counts()

# print (count[count>2].to_dict())
for key in count[count>2].to_dict():
    user.append(key) #user id buy tiwce
   
# for x in user: 
  # print(x)
# df.loc[df['favorite_color'].isin(array)]
# df.drop(user, inplace = True)
merchant = df.loc[df['userid'].isin(user)]
print (merchant.sort_values(by=['userid','shopid', 'event_time']))

user_merchants = []
for key in merchant.to_dict();

hash = {215490055:[86572177, 62947690, 89127015, 86572177], usrer2:[merchant2]}

hash2 = {215490055:[86572177, 62947690, 89127015], usrer2:[merchant2]}
