import streamlit as st
import pandas as pd
import numpy as np
import data

df_apt1,df_apt2 = data.read_data()

# 사이드바 // 메인에서 df의 값을 받아온다. main -> create_df -> side_bar
def side_bar(df) :
    s_bar = st.sidebar
    s_bar.title('지역을 선택해주세요.')

    # area에 df에서 열 중에서 중복된 값들을 제외하고 리스트로 변환

    # 시/도 선택
    city_list = df['시군구'].apply(lambda x: x.split()[0]).unique()
    city_choice = s_bar.selectbox('시/도 선택', city_list)

    # 시/군/구 선택
    gu_list = df['시군구'][df['시군구'].str.contains(city_choice)].apply(lambda x: x.split()[1]).unique()
    gu_choice = s_bar.selectbox('시/군/구 선택', gu_list)

    # 읍/면/동 선택
    town_list = df['시군구'][df['시군구'].str.contains(city_choice) & df['시군구'].str.contains(gu_choice)].apply(lambda x: x.split()[2]).unique()
    town_choice = s_bar.selectbox('읍/면/동 선택', town_list)

    # 리 선택
    try :
        village_list = df['시군구'][df['시군구'].str.contains(city_choice) & df['시군구'].str.contains(gu_choice) & df['시군구'].str.contains(town_choice)].apply(lambda x: x.split()[3]).unique()
        village_choice = s_bar.selectbox('리 선택', village_list)
        result = df[df['시군구'].str.contains(city_choice) & df['시군구'].str.contains(gu_choice) & df['시군구'].str.contains(town_choice) & df['시군구'].str.contains(village_choice)]
    except :
        result = df[df['시군구'].str.contains(city_choice) & df['시군구'].str.contains(gu_choice) & df['시군구'].str.contains(town_choice)]
    # 선택된 지역의 데이터만 추출
    
    # result 데이터프레임의 인덱스를 0->1부터 시작하도록 변경
    result.index = np.arange(1, len(result) + 1)

    st.dataframe(result)

    return result

side_bar(df_apt1)