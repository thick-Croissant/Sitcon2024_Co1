
#  Line性別平等機器人

## 競賽議題 & 子議題
- 團隊名稱：{厚可頌}
- 成員姓名：{許岑鎂}, {黃詩云}, {葉芷妤}, {林奇安}
- 競賽議題：{平等起跑線：用科技打破歧視的根源}
    - 子議題：{推廣性別平等與情感教育 X LINE}


### 專案簡介
- 用途/功能：

- 目標客群&使用情境：
    - 學生：可使用情境模擬來理解與反思生活上相似的情況發生
    - 一般民眾：查找近期性別相關新聞，提升對相關議題的認識


- 操作方式：
    - 環境設置
      可以看到 .env 檔案有各種 API，
        * LINE_CHANNEL_ACCESS_TOKEN、LINE_CHANNEL_SECRET<br>
        此為必需新增的 API，否則無法使用LINE Bot。
        * NEWS_API_KEY<br>
        連接至新聞
        * GEMINI_API_KEY<br>
        連接至GEMINI，獲取生成式AI的回覆
        * FIREBASE_URL<br>
        連接至FIREBASE資料庫

### 使用資源
- 工作仿資源：
    -  https://github.com/louis70109/linebot-gemini-earthquake <br>
    我們改編專案的來源
- 公開資源：
    - LINE Bot <br>
    用於管理LINE Bot帳號

### 你還想分享的事情
- 開發過程
  - 第一次參加，什麼都是第一次用，真的太困難了qwq
  - 好累歐qq GCP跑超慢
- 遇到的困難
  - 改編別人的程式要理解一~~大段時間
  - 原本以為連接API很簡單，結果格式什麼的需要處理，連接還一堆error
 
### 在這邊感謝LINE的工程師們提供的幫助<3

> SITCON Hackathon 2024
