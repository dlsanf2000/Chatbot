# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

from bothub_client.bot import BaseBot
from bothub_client.decorators import channel
from bothub_client.messages import Message
import requests
from bs4 import BeautifulSoup


class Bot(BaseBot):
    """Represent a Bot logic which interacts with a user.

    BaseBot superclass have methods belows:

    * Send message
      * self.send_message(message, chat_id=None, channel=None)
    * Data Storage
      * self.set_project_data(data)
      * self.get_project_data()
      * self.set_user_data(data, user_id=None, channel=None)
      * self.get_user_data(user_id=None, channel=None)
    * Channel Handler
      from bothub_client.decorators import channel
      @channel('<channel_name>')
      def channel_handler(self, event, context):
        # Handle a specific channel message
    * Command Handler
      from bothub_client.decorators import command
      @command('<command_name>')
      def command_handler(self, event, context, args):
          # Handle a command('/<command_name>')
    * Intent Handler
      from bothub_client.decorators import intent
      @intent('<intent_id>')
      def intent_result_handler(self, event, context, answers):
          # Handle a intent result
          # answers is a dict and contains intent's input data
            {
              "<intent slot id>" : <entered slot value>
              ...
            }
    """
    @channel()
    def default_handler(self, event, context):
        """Handle a message received

        event is a dict and contains trigger info.

        {
           "trigger": "webhook",
           "channel": "<name>",
           "sender": {
              "id": "<chat_id>",
              "name": "<nickname>"
           },
           "content": "<message content>",
           "raw_data": <unmodified data itself webhook received>
        }
        """
        # self.send_message('Echo: {}'.format(event['content']))

        content = event['content']

        if content == '포도포도 에이드':
          self.a1(event)
        elif content == '청포도 포도 에이드':
          self.a2(event)
        
        elif content == '오곡라떼':
          self.a3(event)
        
        elif content == '그린티라떼':
          self.a4(event)
        elif content == '밀크티라떼':
          self.a5(event)

        elif content == '리얼초콜릿라떼':
          self.a6(event)

        elif content == '고구마라떼':
          self.a7(event)
        elif content == '밀크버블티':
          self.a8(event)
        elif content == '타로버블티':
          self.a9(event)
        elif content == '그린티프라페노':
          self.a10(event)
        elif content == '초코칩프라페노':
          self.a11(event)

        elif content == '플레인요거트스무디':
          self.a12(event)
        elif content == '딸기요거트스무디':
          self.a13(event)
        elif content == '블루베리요거트스무디':
          self.a14(event)
        elif content == '오렌지주스':
          self.a15(event)
        elif content == '자몽주스':
          self.a16(event)
        elif content == '키위주스':
          self.a17(event)
        elif content == '녹차':
          self.a18(event)
        elif content == '잉글리쉬블랙퍼스트':
          self.a19(event)
        elif content == '얼그레이':
          self.a20(event)
        elif content == '민트(허브티)':
          self.a21(event)
        elif content == '카모마일(허브티)':
          self.a22(event)
        elif content == '블렌딩 티 에이드(자몽&히비스커스)':
          self.a23(event)
        elif content == '유자티':
          self.a24(event)
        elif content == '아이스티(복숭아)':
          self.a25(event)
        elif content == '자몽차':
          self.a26(event)
        elif content == '레몬에이드':
          self.a27(event)
        elif content == '자몽에이드':
          self.a28(event)
        elif content == '브라운슈가 밀크티 펄라떼':
          self.a29(event)
        elif content == '라즈베리 골드 아이스 티':
          self.a30(event)
        elif content == '리치 레드 아이스 티':
          self.a31(event)
       


        elif content == '나이트로 콜드브루':
          self.b1(event)
        
        elif content == '콜드브루 헤이즐넛라떼':
          self.b2(event)


        elif content == '콜드브루 바닐라젤라또 라떼':
          self.b3(event)

        elif content == '브라운슈가 콜드브루 펄라떼':
          self.b4(event)

       
        elif content == '흑당 아인슈페너':
          self.b5(event)
        elif content == '흑당 아인슈페너 라떼':
          self.b6(event)
        else:
          self.send_welcome_message(event)
        
        
    def send_welcome_message(self, event):
      message = '반갑습니다.\n저는 카페베네 메뉴를 입력하면, \n메뉴 설명을 해드립니다.\n메뉴를 입력하세요.'
      self.send_message(message)
      message = '---------메뉴 목록---------\n\n=====음료&차=====\n\n포도포도 에이드\n청포도 포도 에이드\n오곡라떼\n그린티라떼\n밀크티라떼\n리얼초콜릿라떼\n고구마라떼\n밀크버블티\n타로버블티\n그린티프라페노\n초코칩프라페노\n플레인요거트스무디\n딸기요거트스무디\n블루베리요거트스무디\n오렌지주스\n자몽주스\n키위주스\n녹차\n잉글리쉬블랙퍼스트\n얼그레이\n민트(허브티)\n카모마일(허브티)\n블렌딩 티 에이드(자몽&히비스커스)\n유자티\n아이스티(복숭아)\n자몽차\n레몬에이드\n자몽에이드\n브라운슈가 밀크티 펄라떼\n라즈베리 골드 아이스 티\n리치 레드 아이스 티\n\n=======커피=======\n\n나이트로 콜드브루\n콜드브루 헤이즐넛라떼\n콜드브루 바닐라젤라또 라떼\n브라운슈가 콜드브루 펄라떼\n흑당 아인슈페너\n흑당 아인슈페너 라떼'
      self.send_message(message)
        

    def a1(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=890'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
        print(title.text)
      message = '포도포도에이드는 ONLY ICED입니다!'
      self.send_message(message)



    def a2(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=891'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)

      message = '청포도 포도 에이드는 ONLY ICED입니다!'
      self.send_message(message)



    def a3(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=639'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '오곡라떼는 HOT, ICED 모두 있습니다!'
      self.send_message(message)



    def a4(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=640'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      
      message = '그린티라떼는 HOT, ICED 모두 있습니다!'
      self.send_message(message)



    def a5(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=642'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '밀크티라떼는 HOT, ICED 모두 있습니다!'
      self.send_message(message)


    def a6(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=646'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '리얼초콜릿라떼는 HOT, ICED 모두 있습니다!'
      self.send_message(message)



    def a7(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=648'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '고구마라떼는 HOT, ICED 모두 있습니다!'
      self.send_message(message)



    def a8(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=651'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '밀크버블티는 ONLY ICED입니다!'
      self.send_message(message)


    def a9(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=652'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '타로버블티는 ONLY ICED입니다!'
      self.send_message(message)


    def a10(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=658'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '그린티 프라페노는 ONLY ICED입니다!'
      self.send_message(message)



    def a11(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=659'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '초코칩 프라페노는 ONLY ICED입니다!'
      self.send_message(message)



    def a12(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=660'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '플레인 요거트 스무디는 ONLY ICED입니다!'
      self.send_message(message)


    def a13(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=661'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '딸기 요거트 스무디는 ONLY ICED입니다!'
      self.send_message(message)


    def a14(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=662'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '블루베리 요거트 스무디는 ONLY ICED입니다!'
      self.send_message(message)


    def a15(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=664'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '오렌지주스는 ONLY ICED입니다!'
      self.send_message(message)


    def a16(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=665'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '자몽주스는 ONLY ICED입니다!'
      self.send_message(message)


    def a17(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=666'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '키위주스는 ONLY ICED입니다!'
      self.send_message(message)



    def a18(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=670'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '녹차는 ONLY HOT입니다!'
      self.send_message(message)



    def a19(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=671'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '잉글리쉬 블랙퍼스트는 ONLY HOT입니다!'
      self.send_message(message)



    def a20(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=672'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '얼그레이는 ONLY HOT입니다!'
      self.send_message(message)



    def a21(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=673'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '민트(허브티)는 ONLY HOT입니다!'
      self.send_message(message)



    def a22(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=674'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '카모마일(허브티)는 ONLY HOT입니다!'
      self.send_message(message)


    def a23(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=930'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '블렌딩 티 에이드(자몽&히비스커스)는 ONLY ICED입니다!'
      self.send_message(message)


    def a24(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=675'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '유자티는 ONLY HOT입니다!'
      self.send_message(message)



    def a25(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=677'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '아이스티(복숭아)는 ONLY ICED입니다!'
      self.send_message(message)



    def a26(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=679'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '자몽차는 ONLY HOT입니다!'
      self.send_message(message)



    def a27(self, event): 
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=682'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '레몬에이드는 ONLY ICED입니다!'
      self.send_message(message)



    def a28(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=683'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '자몽에이드는 ONLY ICED입니다!'
      self.send_message(message)



    def a29(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=952'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '브라운슈가 밀크티 펄라떼는 ONLY ICED입니다!'
      self.send_message(message)



    def a30(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=953'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '라즈베리 골드 아이스 티는 ONLY ICED입니다!'
      self.send_message(message)



    def a31(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M4I0&ItemCode=954'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '리치 레드 아이스 티는 ONLY ICED입니다!'
      self.send_message(message)



    def b1(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M3I0&ItemCode=887'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '나이트로 콜드브루는 ONLY ICED입니다!'
      self.send_message(message)



    def b2(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M3I0&ItemCode=888'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '콜드브루 헤이즐넛라떼는 ONLY ICED입니다!'
      self.send_message(message)



    def b3(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M3I0&ItemCode=889'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '콜드브루 바닐라젤라또 라떼는 ONLY ICED입니다!'
      self.send_message(message)



    def b4(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M3I0&ItemCode=951'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '브라운슈가 콜드브루 펄라떼는 ONLY ICED입니다!'
      self.send_message(message)



    def b5(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M3I0&ItemCode=916'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
      message = '흑당 아인슈페너는 HOT, ICED 모두 있습니다!'
      self.send_message(message)



    def b6(self, event):
      Tag = '#contents > div.prdDetailWrap > div.prdSummary > div > p'
      URL = 'http://www.caffebene.co.kr/Content/Gnb/Menu/MenuDetail.aspx?code=T2M3I0&ItemCode=918'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')

      all_a = soup.select(Tag)
      for title in all_a:
        self.send_message(title.text)
        
      message = '흑당 아인슈페너 라떼는 HOT, ICED 모두 있습니다!'
      self.send_message(message)








