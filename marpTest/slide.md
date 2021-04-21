---
marp: true
theme: gaia
paginate: true
backgroundImage: url('https://marp.app/assets/hero-background.jpg')
header:  '做簡報只要~~10分鐘~~，讓你*更專注於內容*'
footer: '**Copyright 2021 Richard All rights reserved**'
style: |
  footer {
    text-align: end;color: rgb(30,30,30);padding-right: 80px;
  }
---
<!-- _color: rgb(245,245,245) -->
<!-- _header: ""-->
<!-- _footer: "" -->
<!-- _paginate: false -->

# 做簡報只要10分鐘<br>讓你更專注於內容

### -- 如何使用Marp
<br>
<br>
<br>
<br>
<br>

##### 2021/04/22 Richard

![bg brightness:0.5 opacity:0.8](https://media.gettyimages.com/videos/creative-millennial-business-people-using-adhesive-notes-in-meeting-video-id576634954?s=640x640)

---
<!-- _header: ""-->
<!-- _footer: ""-->
<!-- _paginate: false -->

# 目錄

- 前言
- 誰適合使用這項工具?
- 安裝VSCode 和 Marp
- Marp是什麼?
- 開始使用Marp
- Marp實際操作
- 總結

---
# 前言

<!-- _header: ""-->
<!-- _footer: ""-->
<!-- _backgroundImage: "" -->
<!-- _backgroundColor: #FFF -->
<!-- _class: [lead] -->

![bg 80% opacity:0.2](https://img.freepik.com/free-vector/cup-coffee-book-with-pen-from-splash-watercolor-hand-drawn-sketch-illustration-paints_291138-304.jpg?size=626&ext=jpg)

---
# 前言
### 我們浪費過多的時間在簡報**排版**上，有時候內容都已經想好了，但排版就浪費了非常多的時間
<br>

### 如果我們能夠花**更少時間**產生簡報，就可以把精神集中在簡報**內容**上，是否就能提升我們的產出品質?

---
# 前言 - con't
### 傳統的思維方式是:
1.  開啟 Office PowerPoint / Google Slide
2.  開始一頁頁填上內容
3.  進行排版
4.  檢查

##### 其中「排版」是多數人卡住的環節，就算套用簡報模板還是必須進行排版。這真的是太花時間了!
---
# 前言 - con't
<br>
<br>

### 這裡提供另一種方式 — 用技術方式解決簡報排版問題。你不用怕這項技術會很難，它只有一個門檻：會寫 ***Markdown***
<br>

##### 只要會寫Markdown，你已經學會了 50%!
---
# 誰適合使用這項工具?

<!-- _header: ""-->
<!-- _footer: ""-->
<!-- _backgroundImage: "" -->
<!-- _backgroundColor: #FFF -->
<!-- _class: [lead] -->

![bg 60% opacity:0.2](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9AwxljKLKYAV9WA2qmaWGEJF4kfp2WIDHih6c9N2ZCgOwJYT2hm28KqBbrRBbJg5zbyM&usqp=CAU)

---
# 誰適合使用這項工具?
### 如果你是以下這 3 種人，那很適合推薦給你:
- 不想浪費時間在簡報排版(例如工程師)
- 需要時常將文字、筆記轉換成簡報
- 時常需要簡報，不需要太多客製化排版，但需要時常更新內容
---
# 安裝VSCode 和 Marp?

<!-- _header: ""-->
<!-- _footer: ""-->
<!-- _backgroundImage: "" -->
<!-- _backgroundColor: #FFF -->
<!-- _class: [lead] -->

![bg 60% opacity:0.2](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjJEmD9SBE_lEB10lDktqtX02XadDIu0GMkQFubqKzkiqyyFTI375MTN2WEbt3dAlgDFE&usqp=CAU)

---
# 安裝VSCode 和 Marp
<!-- _footer: "" -->

![](https://miro.medium.com/max/1050/1*qtW0-zp9OzZyjEdrUHbmnQ.png)

---
# 安裝VSCode 和 Marp - con't
<!-- _footer: "" -->

![](https://miro.medium.com/max/1050/1*82_i1ElFPIKAc7QALd060A.png)

---
# Marp是什麼?

<!-- _header: ""-->
<!-- _footer: ""-->
<!-- _backgroundImage: "" -->
<!-- _backgroundColor: #FFF -->
<!-- _class: [lead] -->

![bg 60% opacity:0.3](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmgz-ajVuWbm2Eh8FlWJqppM_bH8aD5WkWuXqdC7ZC7QgVzGrypF6cRJY-Mw7YeazI9Rc&usqp=CAU)

---
# Marp是什麼?

### Markdown Presentation Ecosystem 
Marp 是利用Markdown語法編寫簡報的功能，可以僅用編輯器就生出來，同時使用Markdown語法給予簡報內容整齊又美觀的排版。

Marp本身是一個開源專案，安裝VSCode的擴充功能，便能以雙欄式操作即時呈現簡報結果。[官網](https://marp.app/)

**在內容準備好的情況下，由於不需要太管排版，10分鐘內就可以完成簡報了!**

---

# 開始使用Marp

<!-- _header: ""-->
<!-- _footer: ""-->
<!-- _backgroundImage: "" -->
<!-- _backgroundColor: #FFF -->
<!-- _class: [lead] -->

![bg 60% opacity:0.2](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRp6dh7JTDlRTWHMi9hIrKU1-ptxgrJ4NTx76OOFrypmhAkP6jG4q33a4q1pcmWNr2zipU&usqp=CAU)

---
# 開始使用Marp

- 打開VSCode並於最上方輸入，即可使用`Marp`(告訴VSCode說我們要開始使用Marp了!)
  ```
  ---
  marp: true
  ```
- 使用`---`代表換下一頁
- 支援Markdown語法，包含 `#`、`-`、`[超連結](網址)`、`:emoji:`、`粗體`、`斜體`、` ```code ` ...:spades: :hearts::diamonds::clubs::blush:

[語法文件](https://marpit.marp.app/directives)

---
# 開始使用Marp - con't
- 設定Marp`預設參數` (整份Marp簡報開頭是使用`YAML`來設定)
```yaml
---
marp: true
theme: gaia     # 設定簡報主題
paginate: true  # 設定顯示頁碼
backgroundImage: url('https://marp.app/assets/hero-background.jpg') # 設定背景圖片
header:  '做簡報只要~~10分鐘~~，讓你*更專注於內容*'
footer: '**Copyright 2021 Richard All rights reserved**'
style: |    # 視需求，設定CSS
  footer {
    text-align: end;color: rgb(30,30,30);padding-right: 80px;
  }
---
```
---
# 開始使用Marp - con't
- 其中主題預設提供三種 (每種主題在背景顏色，Markdown 文字的擺放位置都會有差異)
  * Default
  * Gaia
  * Uncover

[可於官網查看](https://github.com/marp-team/marp-core/tree/main/themes#readme)

---
# 開始使用Marp - con't
- 屬性 (在 Marp 中稱為**directives**)分兩種:
  * 整份簡報
    + 如上面提到的**YAM**L設定那裡
    + 會影響到整份簡報(例如`paginate:true`每頁都要有頁碼)
  * 針對單一投影片
    + 在指定投影片使用`<!-- 屬性 -->` 即可
    + 例如 `<!-- paginate:false -->` 表示 此頁**後**不顯示頁碼

---
# 開始使用Marp - con't
![bg right](https://marpit.marp.app/assets/directives.png)

- `<!-- 屬性 -->` vs  `<!-- _屬性 -->`
- `<!-- 屬性 -->`: 此頁**後**都套用
- `<!-- _屬性 -->`: **只有**此頁套用

---
# Marp實際操作

<!-- _header: ""-->
<!-- _footer: ""-->
<!-- _backgroundImage: "" -->
<!-- _backgroundColor: #FFF -->
<!-- _class: [lead] -->

![bg right:55% opacity:0.6](https://i.insider.com/54ff07ea6da8111c6feb1ed8?width=1100&format=jpeg&auto=webp)


---
# 總結

<!-- _header: ""-->
<!-- _footer: ""-->
<!-- _backgroundImage: "" -->
<!-- _backgroundColor: #FFF -->
<!-- _class: [lead] -->

![bg opacity:0.8 right:80%](https://thumbor.forbes.com/thumbor/fit-in/416x416/filters%3Aformat%28jpg%29/https%3A%2F%2Fspecials-images.forbesimg.com%2Fimageserve%2F5f4ebe0c87612dab4f12a597%2F0x0.jpg%3Fbackground%3D000000%26cropX1%3D292%26cropX2%3D3684%26cropY1%3D592%26cropY2%3D3987)
![bg brightness:0.9](https://p4.pstatp.com/origin/pgc-image/1a2fbe7a78c444338842d6376d619595.jpeg)
![bg brightness:0.8](https://storage.googleapis.com/opinion-cms-cwg-tw/article/202008/article-5f44866b0ad57.jpg)

---
# 總結
### Marp的特點
- 將文字、筆記很輕鬆的轉換成簡報
- 更高效率處理簡報排版
- 把寶貴時間與精神投注在「構思簡報」上

### 推薦你使用這個方式做簡報!

---
# Reference

- [如何快速完成簡報排版，將精神專注在準備演講上？使用 Marp 套件轉換 Markdown 成簡報](https://medium.com/pm%E7%9A%84%E7%94%9F%E7%94%A2%E5%8A%9B%E5%B7%A5%E5%85%B7%E7%AE%B1/%E5%A6%82%E4%BD%95%E5%BF%AB%E9%80%9F%E5%AE%8C%E6%88%90%E7%B0%A1%E5%A0%B1%E6%8E%92%E7%89%88-%E5%B0%87%E7%B2%BE%E7%A5%9E%E5%B0%88%E6%B3%A8%E5%9C%A8%E6%BA%96%E5%82%99%E6%BC%94%E8%AC%9B%E4%B8%8A-eab8a0668733)
- [使用Marp以Markdown快速製作簡報，並匯出HTML、PPTX與PDF](https://www.youtube.com/watch?v=-sM-2RyhW38&ab_channel=%E7%B0%A1%E7%9D%BF%E8%BB%9F%E9%AB%94%E9%A0%BB%E9%81%93)
- [【Markdown】Marp for VS Code - 快速建立你的展示文档, 向powerpoint说再见](https://www.youtube.com/watch?v=uBmZEgGNnkk&list=RDCMUCazV3A3_1-Mtd6E_auw_ifg&start_radio=1&t=810&ab_channel=%E5%B0%8F%E9%A9%AC%E6%8A%80%E6%9C%AF)