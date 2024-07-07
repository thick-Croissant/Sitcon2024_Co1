import requests
import logging
import google.generativeai as genai
import os

choose = "請輸入選擇編號。如【A-1】"

def fetch_news_data(query, api_key):
    """
    Fetch news data from News API with a focus on Traditional Chinese (Taiwan) content.
    """
    # 指定语言为繁体中文（zh），国家为台湾（tw）
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        logging.error(f"Failed to fetch news data: {response.status_code}")
        return {"status": "error", "message": "無法獲取新聞數據"}

def generate_gmini_story(prompt, api_key):
    """
    Generate story using Google Gemini API.
    """
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-pro')
    #prompt = "使用繁體中文回答。\n" + prompt
    try:
       
        response = model.generate_content("使用繁體中文回答。\n" +prompt)
        # 提取生成的内容
        if response and response.text:
            return response.text
        else:
            logging.error("No generations found in response.")
            return "無法生成故事。"
            
    except Exception as e:
        logging.error(f"Failed to generate story: {e}")
        return "無法生成故事。"



def story_A(message):
    news = "\n\n改寫至: https://www.asahi.com/articles/ASQ3467CHQ2XUHBI050.html"
    start = ("歡迎來到超級英雄訓練營！在這裡，我們不分男女，每個人都有機會成為超級英雄！今天，我們要學習如何辨別和挑戰不公平的性別刻板印象。準備好了嗎？\n\n"+
            "訓練營的第一堂課是角色扮演。老師宣布：「今天我們要扮演拯救世界的超級英雄！男生扮演勇敢強壯的超人，女生扮演溫柔善良的護士！」\n"+
            "你聽到老師的話，心裡覺得怪怪的。這時，你有三個選擇：\n\n"+
            "A-1：舉手跟老師說：「老師，為什麼男生一定要當超人，女生一定要當護士？我覺得女生也可以很勇敢，男生也可以很溫柔啊！」\n"+
            "A-2：跟旁邊的同學小聲說：「你不覺得老師這樣說怪怪的嗎？為什麼女生不能當超人？」 \n"+
            "A-3：什麼都不說，乖乖聽老師的話。"
            )
    A1 = ("太棒了！你勇敢地表達了自己的想法，也讓老師和其他同學意識到性別刻板印象的問題。\n\n"+
           "老師聽完你的話後，思考了一下，笑著說：「你說得對！我們不應該被傳統觀念限制，每個人都可以成為自己想成為的樣子！"+
           "這樣吧，我們讓大家自由選擇角色，好不好？」\n\n"+
           "老師讓大家自由選擇角色後，訓練營的氣氛變得更加活躍。同學們興奮地選擇自己喜歡的角色，"+
           "有的男生選擇當護士，有的女生選擇當超人。大家開始進行角色扮演，互相合作，體驗不同角色的魅力。\n\n"+
            "訓練結束後，老師問大家今天的感受。同學們紛紛表示，這樣的自由選擇讓他們更有參與感，也讓他們明白了每個人都可以挑戰性別刻板印象。\n\n"
          )
    A2 = ("你向身邊的同學表達了你的想法，很棒！你們可以一起思考，試著找機會跟老師或其他同學討論這個問題。\n\n"+
          "你和身邊的同學一起思考後，決定在下課後找老師討論這個問題。老師聽了你們的想法，表示非常欣賞你們的勇氣和觀察力。"+
           "他同意在以後的課程中，不再設置性別限制，讓每個人都有機會選擇自己喜歡的角色。\n\n"+
          "這次討論讓你們更加堅定了挑戰性別刻板印象的決心。你和同學們決定成立一個「性別平等小組」，在校園內推廣性別平等的理念。"
          )
    
    A3 = ("你選擇了沉默，但心裡可能還是有些不舒服。沒關係，意識到問題的存在就是一個好的開始。\n\n"+
           "雖然你沒有說出自己的想法，但心裡一直覺得不舒服。下課後，你和朋友討論了這件事，決定下次遇到類似的情況一定要勇敢表達自己的意見。\n"+
           "這次經歷讓你明白，挑戰性別刻板印象需要勇氣和行動，下次遇到類似的情況，試著勇敢一點，表達你的想法吧！")
    
    if "A.超級英雄訓練營！" == message:
        return start
        
    elif "A-1" == message:
        return A1 + news

    elif "A-2" == message:
        return A2 + news
        
    elif "A-3" == message:
        return A3 + news

    else:
        return choose
        
def story_B(message):
    news="https://www.parenting.com.tw/article/5092375"

    if "B.小葉的故事" in message:
        return 0
            
    elif "B-1" or "B-2" in message:
        return "小葉都在朋友的支持下變得更加堅強和自信。然而，校園中的霸凌問題依然存在，甚至在某些情況下變得更加嚴重。\n這時，他和朋友們面臨著一個重要的決定：他們是應該大聲疾呼，讓更多人知道這個問題，還是繼續低調行事，慢慢改變周圍的環境？\n選擇B-3：公開發聲\n小葉和他的朋友們決定公開發聲，利用社交媒體和校報等平台，引起更多人的關注，呼籲大家共同對抗霸凌，推動性別平等。\n\n選擇B-4：低調處理\n小葉和他的朋友們決定低調行事，專注於自己的小組活動，默默地支持彼此，希望通過潛移默化的方式來改變周圍人的態度。"
            
    elif "B-3" in message:
        return "小葉和他的朋友們公開發聲後，成功地引起了更廣泛的關注。他們的行動不僅影響了學校，還推動了社會的變革，最終推動了性別平等運動的進展。小葉的故事成為了鼓舞更多人的力量，他們一起為性別平等而努力，並取得了顯著的成效。\n"+news

    elif "B-4" in message:
        return "小葉和他的朋友們低調處理後，創建了一個友善和包容的小圈子。他們的影響範圍雖然有限，但這種變化是真實而深遠的。小葉在朋友的支持下，逐漸成長為一個堅強和自信的人。他們的小圈子成為了一個溫暖的避風港，讓更多人感受到平等和包容的力量。\n"+news
    
    else:
        return choose
    
def story_C(message):
    news = "\n\n改寫至: https://consent.yahoo.com/v2/collectConsent?sessionId=1_cc-session_c8aaa472-fca0-40ad-90d3-f4a2c818ea8f"
    start = ("歡迎來到彩虹王國！在這裡，每個人都有著獨一無二的顏色，代表著不同的個性和興趣。"+
             "今天，我們將跟著小藍和小粉展開一場特別的冒險，學習性別平等和情感教育。準備好了嗎？出發！\n\n"+
            "小藍和小粉是好朋友，他們在運動場上玩耍。小藍喜歡踢足球，而小粉喜歡跳繩。\n"+
            "「我們來比賽踢足球吧！」小藍興奮地說。\n"+
            "「可是我比較想跳繩...」 小粉有點猶豫。\n"+
            "「跳繩是女生玩的遊戲啦！我們一起踢足球才刺激！」 小藍大聲說道。\n"+
            "聽見小藍的話，小粉心裡有些不舒服。\n"+
            "你覺得小粉應該怎麼做？\n\n"+      
            "C-1：為了和小藍一起玩，勉強答應踢足球。\n"+
            "C-2：勇敢地和小藍表達自己的想法。")
    
    C1 = ("小粉鼓起勇氣說：「每個人都可以選擇自己喜歡的遊戲，不分男生女生。我比較想跳繩，我們可以一起跳啊！」\n"+
           "然而，因為不熟悉規則，小粉不小心踢到了小藍，讓小藍非常生氣，兩個人不歡而散。\n\n"+
           "結局一：不歡而散\n"+
           "小藍和小粉因為誤會而吵架，沒能好好溝通，友誼也因此產生了裂痕。"
           )
    
    C2 = ("小粉鼓起勇氣說：「每個人都可以選擇自己喜歡的遊戲，不分男生女生。我比較想跳繩，我們可以一起跳啊！」\n"+
           "小藍聽了小粉的話，意識到自己剛才的說法不對。\n"+
           "「對不起，我不應該說跳繩是女生玩的遊戲。我們可以先一起跳繩，然後再一起踢足球嗎？」 小藍誠懇地說。\n"+
           "小粉開心地笑了：「好啊！我們輪流玩吧！」\n\n"+
           "你覺得小藍和小粉的做法對嗎？\n"+
           "C-3：對，他們學會了互相尊重和理解。\n"+
           "C-4：不對，他們應該堅持自己的喜好。"
          )
    
    C3 = ("小藍和小粉在互相尊重和理解的基礎上，找到了彼此都能接受的玩法，度過了快樂的一天。\n\n"+
          "結局二：快樂的一天\n"+
           "小藍和小粉學會了尊重彼此的喜好，並且願意互相包容和理解，他們的友誼更加牢固了。")
    
    C4 = ("小藍和小粉因為堅持自己的喜好，沒有辦法一起玩耍，最後各自回家，感到有些孤單。\n\n"+
          "結局三：孤單的回家路\n"+
           "小藍和小粉因為沒有找到彼此都能接受的方式，最終沒能一起玩耍，只能各自回家，心裡感到有些失落。")

    
    if "C.彩虹王國的冒險" == message:
        return start
        
    elif "C-1" == message:
        return C1 + news

    elif "C-2" == message:
        return C2
        
    elif "C-3" == message:
         return C3 + news
        
    elif "C-4" == message:
        return C4 + news

    else:
        return choose


def story_D(message):
    news = "\n\n改寫至: https://tw.news.yahoo.com/%E5%A5%B3%E5%8A%9B%E5%89%8D%E9%80%B2%E7%BF%BB%E8%BD%89%E7%A4%BE%E5%8D%80-%E5%A4%9A%E5%85%83%E5%9C%98%E9%AB%94%E5%A5%B3%E5%8A%9B%E8%B5%B0%E5%85%A5%E7%A4%BE%E5%8D%80%E7%99%BC%E6%8F%AE%E5%BD%B1%E9%9F%BF%E5%8A%9B-143053407.html"
    start = ("在一個多元社區裡，有一個年輕的女工程師名叫小雨。她充滿熱情和才華，致力於推動社區內的科技創新。\n"+
             "然而，小雨發現自己常常面臨來自同事和社區成員的性別偏見和刻板印象。\n"+
             "一天，社區內舉行了一場科技創新競賽，小雨決定參賽，展示她的新發明——一款能夠改善環境的智能裝置。\n"+
             "當她興奮地介紹她的作品時，她注意到評審中有一些人對她的表現並不以為然。\n"+
             "現在有三個選擇:\n"+
             "D-1:堅持自己的立場，強調發明的技術優勢和環境貢獻\n"+
             "D-2:尋求男性同事的支持，希望他們能幫助她獲得評審的認同\n"+
             "D-3:決定放棄，覺得自己的努力無法改變現狀"
            )
    D1 = ("小雨深吸一口氣，堅定地解釋了她的發明如何能夠改善環境，並詳細回答了評審的所有問題。\n"+
            "她的熱情和專業知識終於打動了評審，獲得了競賽的最高榮譽。\n"+
            "然而，她的成功並沒有結束性別偏見的挑戰。"
          )
    D2 = ("小雨決定尋求男性同事的支持，希望他們能幫助她獲得評審的認同。\n"+
           "她的同事們被她的熱情感染，決定幫助她。他們一起努力，最終說服了評審，艾麗絲獲得了競賽的榮譽。\n"+
            "但這也讓艾麗絲開始思考，為什麼她需要依賴男性的支持才能獲得成功。"
          )
    
    D3 = ("小雨感到沮喪和無力，決定放棄參賽。\n"+
           "她回到家裡，開始反思自己在這個社區中的位置。\n"+
           "她的朋友們鼓勵她重新振作，並提醒她，性別平等的改變需要每個人的努力。\n"+
            "艾麗絲重新思考後，決定繼續為性別平等而努力"
            )
    
    if "D.小雨的故事" == message:
        return start
        
    elif "D-1" == message:
        return D1 + news

    elif "D-2" == message:
        return D2 + news
        
    elif "D-3" == message:
        return D3 + news

    else:
        return choose
