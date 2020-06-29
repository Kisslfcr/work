# shiyanlou:Code/ $ cat analysis.py                                                                                        [17:01:12]
import json
import pandas as pd

def analysis(file, user_id):
    times = 0
    minutes = 0
    with open(file) as f:
        fj = json.loads(f.read())
    df = pd.DataFrame(fj)    
    df1 = df[df['user_id'] == user_id]
    print(df1)
    times = df1.shape[0]		#0去列，1是取行
    minutes = df1.minutes.sum()

    return times, minutes

if __name__ == '__main__':
    an1 = analysis('user_study.json',5348)
    print(an1)