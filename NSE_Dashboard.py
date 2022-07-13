import streamlit as st
import pandas as pd
import nsepy
from nsepy import get_history
from datetime import date
import datetime
import requests
import json
from dfply import *
cookievalue= ""
st.set_page_config(layout='wide')
def price_data(symb, start_date, around= 1):
    #"SBIN"
#     data = get_history(symbol=symb, start=date(2015,1,1), end=date(2015,1,31))
    print(start_date - datetime.timedelta(days=around))
    print(start_date + datetime.timedelta(days=around))
    data = get_history(symbol=symb, start=start_date - datetime.timedelta(days=around), end=start_date + datetime.timedelta(days=around))
    print(data)
    return data

def announcements(symb, start_day, cookievalue):
    url = "https://www.nseindia.com/api/corporate-announcements"
#     start_day= datetime.datetime.strptime(start_day, "%d-%m-%Y").date()
#     end_day= datetime.datetime.strptime(end_day, "%d-%m-%Y").date()
    if cookievalue =="":
        cookievalue= 'Cookie: RT="z=1&dm=nseindia.com&si=07781908-c00d-49fc-8fd7-dd7c74d848a5&ss=l5jjsj0u&sl=0&tt=0&bcn=%2F%2F684d0d46.akstat.io%2F&ld=283ij&nu=kpaxjfo&cl=6vt"; _ga_PJSKY6CFJH=GS1.1.1657713459.7.1.1657713461.58; _ga=GA1.1.1126232499.1657641661; _gid=GA1.2.764847340.1657641692; ak_bmsc=CFC850E24CE5670381329BD64193BDB6~000000000000000000000000000000~YAAQN0YDFyMWOq6BAQAA8xIz9xAqdJ+PIU1CChIy0YOa7X1b7EsYXsJbOzXlwq9A2GpBwgnYosQ8fQb01Tx6QaOTzTvhqp+pvLlT5QCQjoEpy2dpoXWz+uWPq8MHPI8N+10xtJCFpVBxg5Kh7gWxLQQAjCdqUpL28z0aq1oQo1voFXZd7r4IgC7Ia7Zq6y3vWdlOJQOHc9NoKastyluVvAHtPpVpoFj7L3YPN89QL4hv4Uwr/DLMt5tRXsgngbT5ltOlW2rvS91i5iY4IEq5cdqQKzrK37DKPFkeb15R7P8BX0oBwGES8eNqifbFYtlivm51o/2dXGs+5jmiJdHhezrGTWvm8dYK+1TZfN7YW8oio9gIHpP+JRi/y49X+w48lDomWjt/B6T4Xst9wkPb4KcxkhdmyKv+0nvGhII0WgZN9dt1X8oqS+LxCw7h6K6djRUD0TSoZTNx2uNHL9qKU4cmF3E5AJDzUYy3eMyM+Is=; bm_sv=6BA191A9643A66B90B38428901A7A51A~YAAQN0YDF9l6O66BAQAAjxts9xB6VTHuuC07ZPGQno36QJ0sddVAel4YQ3yezI6YWom/BWiDo22NSGZqgG0HBHGbJCgiLY38irM1hIJBjcyAnmIRIcZRDbumSoLbMPBYalPuYamA96CHIFIAekBemggaZYzOy77+XSratnzxF1Qo64x/BSG4hElHa9MKA4ohqJlrNTud8/edj87v8+p3vZXZedEI3fATgg0+GZrJz/dnU914W3aImtXLFv/E+ssycmoP~1; bm_mi=B7871CE31094EB95D9F8C4B7BA04351F~YAAQN0YDF7UVOq6BAQAAhQcz9xA3ANKCJQiK51b4qostmG7mAxR3QcCzYiMoaNM4EB9hT0br8PPaYKaCpFtMpO5qDphXrjJDsyHPYsXzjRPCP2vGbK+C2hS5TXTBTxPF5mC0MrmhLYhSPgnJTDvHlVQDIupzR0r6B9NYyo1UL0AcLYNZIQFNJy4qciPOQXnMkJfoN2uIHtWSwDB2KDV8mw0N6ASSgSDWdQrTtLRqXmuD12ozDZ3hlUHkSJuptEceR6Eaif957W5kT07CR0N3tz9NlDiZQb8OjvIZZoKMxuN0cBOvetssfxWzlD54ou3AOnEKbjzLL3bjnZvBFuYLgmkbvtPBOtSnNxNx0iJ+zmjEq6CGZa15FuNjZiw/~1; nsit=cOMNphr2jjI8asLifYBJYgp0; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTY1NzcxMzQ1OSwiZXhwIjoxNjU3NzE3MDU5fQ.a8eA9JptJXP8QC3G2Edw78OHSK4ZtYvHA-IbB-HZwR8; AKA_A2=A'

    # start_day= datetime.datetime.strptime(start_day, '%Y-%m-%d').strftime('%d-%m-%Y')
    day_1= start_day - datetime.timedelta(days=1)
    # day_1= datetime.datetime.strptime(day_1, '%Y-%m-%d').strftime('%d-%m-%Y')
    day_1= day_1.strftime('%d-%m-%Y')
    day_2= start_day + datetime.timedelta(days=1)
    day_2= day_2.strftime('%d-%m-%Y')

    params={
    "index" : "equities",
   "from_date":  day_1, #"01-06-2022",
   "to_date":  day_2 , #"10-07-2022",
   "symbol":  symb, #"INFY",
#     "issuer": "Infosys Limited"
}

    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
      'Accept': '*/*',
      'Referer': 'https://www.nseindia.com/companies-listing/corporate-filings-announcements',
      'Cookie': cookievalue
    }
    response = requests.request("GET", url, headers=headers, data={}, params= params)
    # print(response.text)  

    temp= json.loads(response.text)
    temp= pd.DataFrame(temp).drop(['seq_id','difference','csvName','bflag','exchdisstime','dt','old_new','sort_date','sm_isin','smIndustry','orgid'], axis= 1)
    return temp


def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    text = link.split('=')[0]
    return f'<a target="_blank" href="{link}">{text}</a>'


st.subheader("Corp. Announcements Effect On Stock Price", anchor=None)
pd.set_option('display.max_colwidth', -1)

with st.form("input_form"):
    symb= st.text_input("Enter Symbol ", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, placeholder=None, disabled=False)
    select_date= st.date_input("Enter Date to Analyse", value=None, min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
    cookievalue= st.text_input("Enter Cookies ", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, placeholder=None, disabled=False)

    if cookievalue =="":
        cookievalue='RT="z=1&dm=nseindia.com&si=07781908-c00d-49fc-8fd7-dd7c74d848a5&ss=l5jbi97k&sl=0&tt=0&bcn=%2F%2F684d0d4c.akstat.io%2F&ld=2qkpe&nu=kpaxjfo&cl=62s"; _ga_PJSKY6CFJH=GS1.1.1657699542.5.1.1657699544.58; _ga=GA1.1.1126232499.1657641661; _gid=GA1.2.764847340.1657641692; ak_bmsc=7ADC5FB20AC1C3E5F087F455771FE382~000000000000000000000000000000~YAAQN0YDF8wFLq6BAQAAuaw89hA50eqVjZJeCADC14ZUJbHCuJ36z+Jtolfa05Tjb15bNYur/pWteHx5DOyRywFpk51pey4427qMBxuPtX0ivpVy37KLLhmGmI0ft1tL2fv/MtWtU3oRwlEow5+y0fyjie6clA3EN7vDuzHVAaLlvGfoCRPtWyqXX/1LotGIVUha7ZfAzvFIbbsWhy92HFdImTGhtBiI3x1dUx65CgA+z4A/NfxZ5nHN3rDw/Di1I4QM3miM+IMvswhqD8WZO4FPgGlF9sBud4io1kpzKuc1mP7HZ5Z+72fLU1+gzYbESCerBkJ6NUDZlEAz55yJniU9n1uPikFSpNfCCFyE69p76dkkF4HX1fBj6eQ2jt1mjQqr6h8IBKtslPhhirokMnc/z4zHZDKtui2PyZI4dkVRg9E5OVR+xuv28p9iur8I45goH8ekevEGl7UHVIn1bVsVyXVBZRvxhU5Wq+3Cyy/ooBH5kZicz5NVkhCQh5GPTBTSqcj4+K1Qb/135w6cBN+8iB3ki7rBfbUmSLDYH35W3JgAIf21NM2ACMeAVcpJA9S5; bm_mi=71310E069A835331EBD7061E9EC0592D~YAAQN0YDF2UDLq6BAQAA+HU89hAAtmCvIy7QDPvgDs/xJWRgVfFFQZH2oQ49eguTXc5J8fG0/QSHOlVQUV1ZiVzRSe/ajsgGcOm414OBI12LAXJoMdN31SLubI5QL0fDDIMJ521MQxjQhgqwu+g+mbag2tmVHtt6f/2BnhMrp7xC/dzuMa6CdS/5EkrhQ4Re//GF+0P3zhgczCgMXGrCsttFYWs8aS0Col3qwbNt6gX5Ubpzpcm0Dw4pMhr68nmMaK74HXG/TLVan3swg1zF4SBuURTsdMBkpAsO6m+ILULwiwyCiOAKopSlyj7+8U/zBvtEnhU2W+cMT4zalRvHolA+UL5AYjwVB64SzDXepSXnZ0hIoISmtb7dYuMw~1; bm_sv=F7CE8E2725DF76B40030DA9D30602799~YAAQN0YDF6EbM66BAQAAa72X9hBpoN509oPxT3RWZRm9v8bQ4/VBQJ2LeokFzORfC03Lfxnx0X9YL7xLo81+MRAO3baxSZ/E79n6k6FiYxGaLMY0SUxXjfnh9cifNDVlNyo1ebdfN8HBLDKbbXxFBT7UMRGeeer0/doASDio0AeUb8Fxgt5K1TmxAYjm0xWUhxNkNsDDroZBq8iHOSN5YzHvcekR61rnWLj0FSVlaGis8PePonjMZLkVthk/ERAZpd2lVw==~1; nsit=Kf1xgroV2nFRFc7m7xhJfSVe; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTY1NzY5OTU0MiwiZXhwIjoxNjU3NzAzMTQyfQ.dg---2l-RbkZ5bEoVvaNNNRV43AICTgm4xmxUGzajyk; AKA_A2=A'

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        # st.write("symb", symb, "date", select_date)
        st.write("")
        st.write("#")
        st.subheader('Stock Price Data')
        price_date = price_data("SBIN",select_date) #datetime.date(2020,1,1))
        price_date.drop(['Symbol','Series','Prev Close','Turnover'], axis=1, inplace= True)
        price_date= price_date >> mutate(Spike=100*(X.High - X.Low)/X.Low)
        st.write(price_date)

        temp= announcements("INFY",  select_date,cookievalue) #"01-06-2022"
        temp.drop(['symbol','sm_name'], axis=1, inplace= True)
        # CSS to inject contained in a string
        hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """

        import numpy as np
        marketstart = datetime.time(9, 30)
        marketend = datetime.time(15, 30)
        temp['an_dt']= pd.to_datetime(temp['an_dt'])
        temp['MarketTime_color'] = np.where( temp['an_dt'].dt.time <= marketstart , False, True)
        temp['MarketTime_color'] = np.where( temp['an_dt'].dt.time >= marketend , False, True)

        Color_green= np.where(temp['MarketTime_color'] ==True)
        temp.sort_values(by='an_dt', ascending=True, inplace=True)
        temp_bk=temp.copy() 
        # Color_red= np.where(temp['Record B'] !=temp['Record A'])

        # temp['attchmntFile'] = temp['attchmntFile'].apply(make_clickable)
        # temp = temp.to_html(escape=False)
        st.write("#")
        st.write("#")
        st.subheader('Corporate Announcements')
        st.dataframe(temp.style.set_properties(subset = pd.IndexSlice[Color_green[0].tolist(), :], **{'background-color' : 'lightgreen'}).hide_index()) #.set_properties(subset = pd.IndexSlice[Color_red[0].tolist(), :], **{'background-color' : 'lightyellow'}).hide_index())

        st.write("#")
        temp_bk.drop(['MarketTime_color','desc','attchmntText'], axis=1, inplace= True)
        temp_bk['attchmntFile'] = temp_bk['attchmntFile'].apply(make_clickable)
        temp_bk = temp_bk.to_html(escape=False)
        st.write(temp_bk, unsafe_allow_html=True)


        # price_date = price_data("SBIN",select_date) #datetime.date(2020,1,1))
        # price_date.drop(['Symbol','Series','Prev Close','Turnover'], axis=1, inplace= True)
        # st.write(price_date)

        # temp= announcements("INFY",  select_date,cookievalue) #"01-06-2022"
        # temp.drop(['symbol','sm_name'], axis=1, inplace= True)
        # # CSS to inject contained in a string
        # hide_table_row_index = """
        #     <style>
        #     tbody th {display:none}
        #     .blank {display:none}
        #     </style>
        #     """
        # link is the column with hyperlinks
        # import numpy as np
        # marketstart = datetime.time(9, 30)
        # marketend = datetime.time(15, 30)
        # temp['an_dt']= pd.to_datetime(temp['an_dt'])
        # temp['MarketTime_color'] = np.where( temp['an_dt'].dt.time <= marketstart , False, True)
        # temp['MarketTime_color'] = np.where( temp['an_dt'].dt.time >= marketend , False, True)

        # Color_green= np.where(temp['MarketTime_color'] ==True)
        # temp.sort_values(by='an_dt', ascending=True, inplace=True)
        # temp_bk=temp.copy() 
        # # Color_red= np.where(temp['Record B'] !=temp['Record A'])

        # # temp['attchmntFile'] = temp['attchmntFile'].apply(make_clickable)
        # # temp = temp.to_html(escape=False)

        # st.write(temp.style.set_properties(subset = pd.IndexSlice[Color_green[0].tolist(), :], **{'background-color' : 'lightgreen'}).hide_index()) #.set_properties(subset = pd.IndexSlice[Color_red[0].tolist(), :], **{'background-color' : 'lightyellow'}).hide_index())


        # temp_bk.drop(['MarketTime_color','desc','attchmntText'], axis=1, inplace= True)
        # temp_bk['attchmntFile'] = temp_bk['attchmntFile'].apply(make_clickable)
        # temp_bk = temp_bk.to_html(escape=False)
        # st.write(temp_bk, unsafe_allow_html=True)


# col1, col2, col3 = st.columns(3)
# price_date = price_data("SBIN",select_date) #datetime.date(2020,1,1))
# price_date.drop(['Symbol','Series','Prev Close','Turnover'], axis=1, inplace= True)

# with col1:
#     st.header("Date - 1")
#     # st.image("https://static.streamlit.io/examples/cat.jpg")
#     # price_data_1("SBIN",date(2020,1,1))
#     # price_data_1("SBIN",date(2020,1,1))
#     st.write(price_date)


# with col2:
#     st.header("Date")
#     # st.image("https://static.streamlit.io/examples/dog.jpg")

# with col3:
#     st.header("Date + 1")
#     # st.image("https://static.streamlit.io/examples/owl.jpg")


# st.write(price_date)

# temp= announcements("INFY",  "01-06-2022", "13-06-2022","")
# st.write(temp)








#####Separate UI
# st.write("#")
# st.subheader('Stock Price Data')
# price_date = price_data("SBIN",select_date) #datetime.date(2020,1,1))
# price_date.drop(['Symbol','Series','Prev Close','Turnover'], axis=1, inplace= True)
# price_date= price_date >> mutate(Spike=100*(X.High - X.Low)/X.Low)
# st.write(price_date)

# temp= announcements("INFY",  select_date,cookievalue) #"01-06-2022"
# temp.drop(['symbol','sm_name'], axis=1, inplace= True)
# # CSS to inject contained in a string
# hide_table_row_index = """
#     <style>
#     tbody th {display:none}
#     .blank {display:none}
#     </style>
#     """

# import numpy as np
# marketstart = datetime.time(9, 30)
# marketend = datetime.time(15, 30)
# temp['an_dt']= pd.to_datetime(temp['an_dt'])
# temp['MarketTime_color'] = np.where( temp['an_dt'].dt.time <= marketstart , False, True)
# temp['MarketTime_color'] = np.where( temp['an_dt'].dt.time >= marketend , False, True)

# Color_green= np.where(temp['MarketTime_color'] ==True)
# temp.sort_values(by='an_dt', ascending=True, inplace=True)
# temp_bk=temp.copy() 
# # Color_red= np.where(temp['Record B'] !=temp['Record A'])

# # temp['attchmntFile'] = temp['attchmntFile'].apply(make_clickable)
# # temp = temp.to_html(escape=False)
# st.write("#")
# st.write("#")
# st.subheader('Corporate Announcements')
# st.dataframe(temp.style.set_properties(subset = pd.IndexSlice[Color_green[0].tolist(), :], **{'background-color' : 'lightgreen'}).hide_index()) #.set_properties(subset = pd.IndexSlice[Color_red[0].tolist(), :], **{'background-color' : 'lightyellow'}).hide_index())

# st.write("#")
# temp_bk.drop(['MarketTime_color','desc','attchmntText'], axis=1, inplace= True)
# temp_bk['attchmntFile'] = temp_bk['attchmntFile'].apply(make_clickable)
# temp_bk = temp_bk.to_html(escape=False)
# st.write(temp_bk, unsafe_allow_html=True)
