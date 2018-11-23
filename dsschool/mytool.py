
# 리스트를 테이블로 변환시켜줌 (첫째는 리스트 모음, 둘째는 각 리스트의 명칭)

def list_to_table(all_list, col_names):
    import pandas as pd
    import numpy as np

    all_list = np.transpose(all_list)
    df = pd.DataFrame(data = np.array(all_list))
    df.columns = col_names
#    df.sort_values(by=args, ascending=[False], inplace=True)

    return df


# 데이터 분석시 기본 모듈 로딩

def data_tool():
    # 분석 모듈
    import pandas as pd
    import numpy as np

    # cross validation 등에서 에러 메시지 나오지 않도록 하는 것
    import warnings
    warnings.filterwarnings('ignore')

    # 시각화 모듈
    import seaborn as sns
    import matplotlib as mpl
    import matplotlib.pyplot as plt
#    %matplotlib inline

    # 오늘날짜 반환
    import datetime
    today = datetime.datetime.today().strftime("%y%m%d")

    return today