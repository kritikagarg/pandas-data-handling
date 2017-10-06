import pandas as pd
import sys 

newsameline=sys arg[1]
ts=sys arg[2]
all_hsh=sys arg[3]
tweets=sys arg[5]
user_hsh=sys arg[6]

df1= pd.read_csv(newsameline ,sep='\t', header=None )

df1.columns=['id','time', 'user', 'tweet']
df2=df1.tweet.str.findall(r'#.*?(?=\s|$)')
df=pd.concat([df1, df2], axis=1)
df.columns=['id','time', 'user', 'tweet', 'hashtag']

def faster(df6):
        s = df6['hashtag'].str.split(', ', expand=True).stack()
        i = s.index.get_level_values(0)
        df2 = df6.loc[i].copy()
        df2["hashtag"] = s.values
        df2.drop_duplicates(subset=['user','hashtag'], keep='first', inplace=True)
        return df2

df6=pd.concat([df.user, df.hashtag], axis=1)
df6.hashtag=df6['hashtag'].apply(lambda x: ', '.join(x))
df6= faster(df6)


l=df.user.tolist()               #create list from dataframe column

user_list=list(set(l))     #remove duplicate users

timestamp=[]
hashtag=[]
tweets=[]
user_hashtag=[]
for i in user_list:
	ts=df.loc[df['user']==i, ['time']]
	hs=df.loc[df['user']==i, ['hashtag']]
	hs.hashtag=hs['hashtag'].apply(lambda x: ', '.join(x))
	twt=df.loc[df['user']==i, ['tweet']]
	user_hs=df6.loc[df6['user']==i, ['hashtag']]	
	user_hs=user_hs.reset_index(drop=True)
	timestamp.append(ts)
	hashtag.append(hs)
	tweets.append(twt)
	user_hashtag.append(user_hs)


df3 = pd.concat(timestamp, axis=1)
df4 = pd.concat(hashtag, axis=1)
df5 = pd.concat(tweets, axis=1)
df7 = pd.concat(user_hashtag, axis=1)

df3.columns= user_list
df4.columns= user_list
df5.columns= user_list
df7.columns= user_list


df3.to_csv(ts, sep='\t')
df4.to_csv(all_hsh, sep='\t')
df5.to_csv(tweets, sep='\t')
df7.to_csv(user_hsh, sep='\t')





