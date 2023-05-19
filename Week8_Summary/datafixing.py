import gdown
import pandas as pd

def dataCleaning(filename) :
    """
    : param filename: CSV 파일이름
    """
    df = pd.read_csv(filename, low_memory=False)
    df_book = df.dropna(axis=1, how='all')
    count_df = df_book[['도서명','저자','ISBN','권','대출건수']]
    loan_count = count_df.groupby(by=['도서명','저자','ISBN','권'], dropna=False).sum()
    dup_rows = df_book.duplicated(subset=['도서명','저자','ISBN','권'])
    unique_rows = ~dup_rows
    book_unique = df_book[unique_rows].copy()
    book_unique.set_index(['도서명','저자','ISBN','권'], inplace=True)
    book_unique.update(loan_count)
    book_return = book_unique.reset_index()
    book_return = book_return[df_book.columns]

    return book_return

import requests
from bs4 import BeautifulSoup

def dataFixing(df_book):
    """
    잘못된 값을 수정하거나 NaN을 채우는 함수
    :param df_book: dataCleaning() 함수에서 전처리된 데이터프레임
    """
    
    df_book = df_book.astype({'도서권수':'int32', '대출건수': 'int32'})
    set_isbn_na_rows = df_book['세트 ISBN'].isna()
    df_book.loc[set_isbn_na_rows, '세트 ISBN'] = ''

    # 발행년도 
    df_book2 = df_book.replace({'발행년도':'.*(\d{4}).*'}, r'\1', regex=True)
    unknown_year = df_book2['발행년도'].str.contains('\D', na=True)
    df_book2.loc[unknown_year, '발행년도'] = '-1'
    df_book2 = df_book2.astype({'발행년도': 'int32'})

    # 단군 력 빼기
    dangun_yy_rows = df_book2['발행년도'].gt(4000)
    df_book2.loc[dangun_yy_rows, '발행년도'] = df_book2.loc[dangun_yy_rows, '발행년도'] - 2333
    dangun_year = df_book2['발행년도'].gt(4000)
    df_book2.loc[dangun_year, '발행년도'] = -1

    # 0~1900년 사이
    old_books = df_book2['발행년도'].gt(0) & df_book2['발행년도'].lt(1900)
    df_book2.loc[old_books, '발행년도'] = -1

    na_rows = df_book2['도서명'].isna() | df_book2['저자'].isna() | df_book2['출판사'].isna() | df_book2['발행년도'].eq(-1)
    
    updated_sample = df_book2[na_rows].apply(get_book_info, axis=1, result_type = 'expand')

    df_book2 = df_book2.dropna(subset=['도서명', '저자', '출판사'])
    df_book2 = df_book2[df_book2['발행년도'] != -1]    

    return df_book2
    
def get_book_title(isbn):
    
    url = 'http://www.yes24.com/Product/Search?domain=BOOK&query={}'

    r = requests.get(url.format(isbn))
    soup = BeautifulSoup(r.text, 'html.parser')   # HTML 파싱

    title = soup.find('a', attrs={'class':'gd_name'}) \
            .get_text()
    return title

import re

def get_book_info(row):
    title = row['도서명']
    author = row['저자']
    pub = row['출판사']
    year = row['발행년도']

    url = 'http://www.yes24.com/Product/Search?domain=BOOK&query={}'
    # URL에 ISBN을 넣어 HTML 가져옵니다.
    r = requests.get(url.format(row['ISBN']))
    soup = BeautifulSoup(r.text, 'html.parser')   # HTML 파싱
    try:
        if pd.isna(title):
            # 클래스 이름이 'gd_name'인 a 태그의 텍스트를 가져옵니다.
            title = soup.find('a', attrs={'class':'gd_name'}) \
                    .get_text()
    except AttributeError:
        pass

    try:
        if pd.isna(author):
            # 클래스 이름이 'info_auth'인 span 태그 아래 a 태그의 텍스트를 가져옵니다.
            authors = soup.find('span', attrs={'class':'info_auth'}) \
                          .find_all('a')
            author_list = [auth.get_text() for auth in authors]
            author = ','.join(author_list)
    except AttributeError:
        pass
    
    try:
        if pd.isna(pub):
            # 클래스 이름이 'info_auth'인 span 태그 아래 a 태그의 텍스트를 가져옵니다.
            pub = soup.find('span', attrs={'class':'info_pub'}) \
                      .find('a') \
                      .get_text()
    except AttributeError:
        pass
    
    try:
        if year == -1:
            # 클래스 이름이 'info_date'인 span 태그 아래 텍스트를 가져옵니다.
            year_str = soup.find('span', attrs={'class':'info_date'}) \
                           .get_text()
            # 정규식으로 찾은 값 중에 첫 번째 것만 사용합니다.
            year = re.findall(r'\d{4}', year_str)[0]
    except AttributeError:
        pass

    return title, author, pub, year


link = ""
filename = 'PtLibraryData.csv'
#url = f'https://drive.google.com/uc?id={link}'
directory = './_csv/'

#gdown.download(url, filename, quiet=False)

pt_book_clean = dataCleaning(f"{directory}{filename}")
pt_book_clean.to_csv(f'{directory}pt_book_clean.csv', index=False)

pt_book_fix = dataFixing(pt_book_clean)
pt_book_fix.to_csv(f'{directory}pt_book_fix.csv', index=False)