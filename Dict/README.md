**book文件夹**为[kajweb/dict](https://github.com/kajweb/dict)整理

**已整理词库文件夹**中为已做过格式处理的文件，注意将词库重命名并放在`data/wordsnorote/wordbook.json`

---

#  JSON 格式说明

以 CET4_3.json 第一个单词 cancel 为例

```json
{
  // 单词序号
  "wordRank": 1,
  // 单词
  "headWord": "cancel",
  "content": {
    "word": {
      "wordHead": "cancel",
      "wordId": "CET4_3_1",
      "content": {
        // 单词相关测试
        "exam": [
          {
            // 问题
            "question": "As we can no longer wait for the delivery of our order, we have to _______ it.",
            // 答案
            "answer": {
              "explain": " cancel order：  取消订单。 句意：  订购的货物尚未送到， 我们不能再等了， 不得不取消订单。 postpone：  推迟， 使延期； refuse：  拒绝， 谢绝； delay：  耽搁， 延迟， 延期。",
              "rightIndex": 4
            },
            // 测试类型
            "examType": 1,
            // 选项
            "choices": [
              {
                "choiceIndex": 1,
                "choice": "postpone"
              },
              {
                "choiceIndex": 2,
                "choice": "refuse"
              },
              {
                "choiceIndex": 3,
                "choice": "delay"
              },
              {
                "choiceIndex": 4,
                "choice": "cancel"
              }
            ]
          }
        ],
        // 例句
        "sentence": {
          "sentences": [
            {
              // 英语
              "sContent": "Our flight was cancelled.",
              // 中文翻译
              "sCn": "我们的航班取消了。"
            },
            {
              "sContent": "I’m afraid I’ll have to cancel our meeting tomorrow.",
              "sCn": "恐怕我得取消我们明天的会议。"
            },
            {
              "sContent": "You’ll just have to ring John and cancel.",
              "sCn": "你只能打电话给约翰取消了。"
            }
          ],
          // 描述
          "desc": "例句"
        },
        // 美音音标
        "usphone": "'kænsl",
        // 近义词
        "syno": {
          "synos": [
            {
              // 词性
              "pos": "vt",
              // 对应词义
              "tran": "[计]取消；删去",
              // 近义词/词组
              "hwds": [
                {
                  "w": "recall"
                },
                {
                  "w": "call it off"
                }
              ]
            },
            {
              "pos": "vi",
              "tran": "[计]取消；相互抵销",
              "hwds": [
                {
                  "w": "call it off"
                },
                {
                  "w": "declare off"
                }
              ]
            },
            {
              "pos": "n",
              "tran": "[计]取消，撤销",
              "hwds": [
                {
                  "w": "withdrawal"
                },
                {
                  "w": "revocation"
                }
              ]
            }
          ],
          "desc": "同近"
        },
        // 英音音标
        "ukphone": "'kænsl",
        // 英音发音https请求参数
        "ukspeech": "cancel&type=1",
        // 短语
        "phrase": {
          "phrases": [
            {
              // 英语
              "pContent": "cancel button",
              // 翻译
              "pCn": "取消按钮"
            },
            {
              "pContent": "cancel out",
              "pCn": "取消；抵销"
            },
            {
              "pContent": "cancel after verification",
              "pCn": "核销"
            }
          ],
          "desc": "短语"
        },
        // 同根词
        "relWord": {
          "rels": [
            {
              // 词性
              "pos": "n",
              "words": [
                {
                  // 英语
                  "hwd": "cancellation",
                  // 翻译
                  "tran": " 取消；删除"
                }
              ]
            }
          ],
          "desc": "同根"
        },
        // 美音发音https请求参数
        "usspeech": "cancel&type=2",
        // 翻译
        "trans": [
          {
            // 中释
            "tranCn": " 取消， 撤销； 删去",
            "descOther": "英释",
            // 词性
            "pos": "vt",
            "descCn": "中释",
            // 英英释义
            "tranOther": "to decide that something that was officially planned will not happen"
          }
        ]
      }
    }
  },
  // 单词书 ID
  "bookId": "CET4_3"
}
```

## 🎙 发音请求

有道英语发音接口

```
https://dict.youdao.com/dictvoice?audio={word}&type={1|2}
```

type 1 为英音 2 为美音

## ⚡ 声明

若本应用侵犯了您的权益，或造成不利影响，请联系 lyy@iwwee.com 并提供微信号码，在确认身份后我将立即下架本应用。

## ⌛ 目录

| 序号 | 图片                                                                                                                     | 标题                        | 单词数量 | 文件大小 | 背诵人数 | 下载地址                                                                                                                                                              | id                  | 标签          |
| ---- | ------------------------------------------------------------------------------------------------------------------------ | --------------------------- | -------- | -------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------- |
| 1    | ![四级真题核心词（图片记忆）](https://nos.netease.com/ydschool-online/1496632727200CET4luan_1.jpg)                       | 四级真题核心词（图片记忆）  | 1162     | 788457   | 875260   | [本地地址](book/1523620217431_CET4luan_1.zip) [原始地址](http://ydschool-online.nos.netease.com/1523620217431_CET4luan_1.zip)                                         | CET4luan_1          | 四级、有道    |
| 2    | ![六级真题核心词（图片记忆）](https://nos.netease.com/ydschool-online/1496655382926CET6luan_1.jpg)                       | 六级真题核心词（图片记忆）  | 1228     | 591417   | 218418   | [本地地址](book/1521164660466_CET6luan_1.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164660466_CET6luan_1.zip)                                         | CET6luan_1          | 六级、有道    |
| 3    | ![考研必考词汇](https://nos.netease.com/ydschool-online/1496632762670KaoYanluan_1.jpg)                                   | 考研必考词汇                | 1341     | 771889   | 252505   | [本地地址](book/1521164661106_KaoYanluan_1.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164661106_KaoYanluan_1.zip)                                     | KaoYanluan_1        | 考研、有道    |
| 4    | ![专四真题高频词](https://nos.netease.com/ydschool-online/1496632776935Level4luan_1.jpg)                                 | 专四真题高频词              | 595      | 269844   | 62169    | [本地地址](book/1521164630387_Level4luan_1.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164630387_Level4luan_1.zip)                                     | Level4luan_1        | 专四、有道    |
| 5    | ![专八真题高频词](https://nos.netease.com/ydschool-online/1491037703359Level8_1.jpg)                                     | 专八真题高频词              | 684      | 242255   | 30059    | [本地地址](book/1521164635290_Level8_1.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164635290_Level8_1.zip)                                             | Level8_1            | 专八、有道    |
| 6    | ![四级英语词汇](https://nos.netease.com/ydschool-online/youdao_CET4_2.jpg)                                               | 四级英语词汇                | 3739     | 2723074  | 215979   | [本地地址](book/1524052539052_CET4luan_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1524052539052_CET4luan_2.zip)                                         | CET4luan_2          | 四级、有道    |
| 7    | ![六级英语词汇](https://nos.netease.com/ydschool-online/youdao_CET6_2.jpg)                                               | 六级英语词汇                | 2078     | 1111633  | 64093    | [本地地址](book/1524052554766_CET6_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1524052554766_CET6_2.zip)                                                 | CET6_2              | 六级、有道    |
| 8    | ![考研英语词汇](https://nos.netease.com/ydschool-online/youdao_KaoYan_2.jpg)                                             | 考研英语词汇                | 4533     | 2431155  | 147205   | [本地地址](book/1521164654696_KaoYan_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164654696_KaoYan_2.zip)                                             | KaoYan_2            | 考研、有道    |
| 9    | ![专四核心词汇](https://nos.netease.com/ydschool-online/youdao_Level4_2.jpg)                                             | 专四核心词汇                | 4025     | 1783295  | 18858    | [本地地址](book/1521164625401_Level4luan_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164625401_Level4luan_2.zip)                                     | Level4luan_2        | 专四、有道    |
| 10   | ![专八核心词汇](https://nos.netease.com/ydschool-online/youdao_Level8_2.jpg)                                             | 专八核心词汇                | 12197    | 5320395  | 23123    | [本地地址](book/1521164650006_Level8luan_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164650006_Level8luan_2.zip)                                     | Level8luan_2        | 专八、有道    |
| 11   | ![新东方四级词汇](https://nos.netease.com/ydschool-online/newOriental_CET4_3.jpg)                                        | 新东方四级词汇              | 2607     | 1719305  | 3063     | [本地地址](book/1521164643060_CET4_3.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164643060_CET4_3.zip)                                                 | CET4_3              | 四级、新东方  |
| 12   | ![新东方六级词汇](https://nos.netease.com/ydschool-online/newOriental_CET6_3.jpg)                                        | 新东方六级词汇              | 2345     | 1452645  | 1193     | [本地地址](book/1521164633851_CET6_3.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164633851_CET6_3.zip)                                                 | CET6_3              | 六级、新东方  |
| 13   | ![新东方考研词汇](https://nos.netease.com/ydschool-online/newOriental_KaoYan_3.jpg)                                      | 新东方考研词汇              | 3728     | 1838572  | 2644     | [本地地址](book/1521164658897_KaoYan_3.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164658897_KaoYan_3.zip)                                             | KaoYan_3            | 考研、新东方  |
| 14   | ![四级真题核心词（正序版）](https://nos.netease.com/ydschool-online/1491037568440CET4_1.jpg)                             | 四级真题核心词（正序版）    | 1162     | 764018   | 6324     | [本地地址](book/1521164649209_CET4_1.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164649209_CET4_1.zip)                                                 | CET4_1              | 有道          |
| 15   | ![六级真题核心词（正序版）](https://nos.netease.com/ydschool-online/1491037677590CET6_1.jpg)                             | 六级真题核心词（正序版）    | 1228     | 753196   | 3888     | [本地地址](book/1521164668667_CET6_1.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164668667_CET6_1.zip)                                                 | CET6_1              | 六级、有道    |
| 16   | ![考研必考词汇（正序版）](https://nos.netease.com/ydschool-online/1491037662208KaoYan_1.jpg)                             | 考研必考词汇（正序版）      | 1341     | 685507   | 7621     | [本地地址](book/1521164669833_KaoYan_1.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164669833_KaoYan_1.zip)                                             | KaoYan_1            | 考研、有道    |
| 17   | ![专四真题高频词（正序版）](https://nos.netease.com/ydschool-online/1491037690141Level4_1.jpg)                           | 专四真题高频词（正序版）    | 595      | 267335   | 2698     | [本地地址](book/1521164647417_Level4_1.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164647417_Level4_1.zip)                                             | Level4_1            | 专四、有道    |
| 18   | ![四级英语词汇（正序版）](https://nos.netease.com/ydschool-online/youdao_CET4_2.jpg)                                     | 四级英语词汇（正序版）      | 3739     | 2542778  | 11803    | [本地地址](book/1521164635506_CET4_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164635506_CET4_2.zip)                                                 | CET4_2              | 四级、有道    |
| 19   | ![专四核心词汇（正序版）](https://nos.netease.com/ydschool-online/youdao_Level4_2.jpg)                                   | 专四核心词汇（正序版）      | 4025     | 1706442  | 4700     | [本地地址](book/1521164653685_Level4_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164653685_Level4_2.zip)                                             | Level4_2            | 专四、有道    |
| 20   | ![专八核心词汇（正序版）](https://nos.netease.com/ydschool-online/youdao_Level8_2.jpg)                                   | 专八核心词汇（正序版）      | 12197    | 4763514  | 8040     | [本地地址](book/1521164663794_Level8_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164663794_Level8_2.zip)                                             | Level8_2            | 专八、有道    |
| 21   | ![雅思词汇](https://nos.netease.com/ydschool-online/youdao_IELTS_2.jpg)                                                  | 雅思词汇                    | 3427     | 1597545  | 276495   | [本地地址](book/1521164624473_IELTSluan_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164624473_IELTSluan_2.zip)                                       | IELTSluan_2         | IELTS、有道   |
| 22   | ![TOEFL词汇](https://nos.netease.com/ydschool-online/youdao_TOEFL_2.jpg)                                                 | TOEFL 词汇                  | 9213     | 4327321  | 118896   | [本地地址](book/1521164640451_TOEFL_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164640451_TOEFL_2.zip)                                               | TOEFL_2             | TOEFL、有道   |
| 23   | ![GRE词汇](https://nos.netease.com/ydschool-online/youdao_GRE_2.jpg)                                                     | GRE 词汇                    | 7199     | 2470882  | 47072    | [本地地址](book/1521164637271_GRE_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164637271_GRE_2.zip)                                                   | GRE_2               | GRE、有道     |
| 24   | ![SAT词汇](https://nos.netease.com/ydschool-online/youdao_SAT_2.jpg)                                                     | SAT 词汇                    | 4423     | 1784650  | 13876    | [本地地址](book/1521164670910_SAT_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164670910_SAT_2.zip)                                                   | SAT_2               | SAT、有道     |
| 25   | ![GMAT词汇](https://nos.netease.com/ydschool-online/youdao_GMAT_2.jpg)                                                   | GMAT 词汇                   | 3254     | 1509190  | 14874    | [本地地址](book/1521164629611_GMATluan_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164629611_GMATluan_2.zip)                                         | GMATluan_2          | GMAT、有道    |
| 26   | ![新东方雅思词汇](https://nos.netease.com/ydschool-online/newOriental_IELTS_3.jpg)                                       | 新东方雅思词汇              | 3575     | 1729987  | 1707     | [本地地址](book/1521164666922_IELTS_3.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164666922_IELTS_3.zip)                                               | IELTS_3             | IELTS、新东方 |
| 27   | ![新东方TOEFL词汇](https://nos.netease.com/ydschool-online/newOriental_TOEFL_3.jpg)                                      | 新东方 TOEFL 词汇           | 4264     | 2015157  | 1294     | [本地地址](book/1521164667985_TOEFL_3.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164667985_TOEFL_3.zip)                                               | TOEFL_3             | TOEFL、新东方 |
| 28   | ![新东方GRE词汇](https://nos.netease.com/ydschool-online/newOriental_GRE_3.jpg)                                          | 新东方 GRE 词汇             | 6515     | 2319121  | 673      | [本地地址](book/1521164677706_GRE_3.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164677706_GRE_3.zip)                                                   | GRE_3               | GRE、新东方   |
| 29   | ![新东方SAT词汇](https://nos.netease.com/ydschool-online/newOriental_SAT_3.jpg)                                          | 新东方 SAT 词汇             | 4464     | 1759354  | 292      | [本地地址](book/1521164636496_SAT_3.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164636496_SAT_3.zip)                                                   | SAT_3               | SAT、新东方   |
| 30   | ![新东方GMAT词汇](https://nos.netease.com/ydschool-online/newOriental_GMAT_3.jpg)                                        | 新东方 GMAT 词汇            | 3047     | 1365145  | 333      | [本地地址](book/1521164672691_GMAT_3.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164672691_GMAT_3.zip)                                                 | GMAT_3              | GMAT、新东方  |
| 31   | ![雅思词汇（正序版）](https://nos.netease.com/ydschool-online/youdao_IELTS_2.jpg)                                        | 雅思词汇（正序版）          | 3427     | 1525677  | 6286     | [本地地址](book/1521164657744_IELTS_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164657744_IELTS_2.zip)                                               | IELTS_2             | IELTS、有道   |
| 32   | ![GMAT词汇（正序版）](https://nos.netease.com/ydschool-online/youdao_GMAT_2.jpg)                                         | GMAT 词汇（正序版）         | 3254     | 1422468  | 2064     | [本地地址](book/1521164662073_GMAT_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164662073_GMAT_2.zip)                                                 | GMAT_2              | GMAT、有道    |
| 33   | ![中考必备词汇](https://nos.netease.com/ydschool-online/youdao_ChuZhong_2.jpg)                                           | 中考必备词汇                | 1420     | 940509   | 273321   | [本地地址](book/1521164669076_ChuZhongluan_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164669076_ChuZhongluan_2.zip)                                 | ChuZhongluan_2      | 有道          |
| 34   | ![高考必备词汇（图片记忆）](https://nos.netease.com/ydschool-online/youdao_GaoZhong_2.jpg)                               | 高考必备词汇（图片记忆）    | 3668     | 2120036  | 256873   | [本地地址](book/1521164673602_GaoZhongluan_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164673602_GaoZhongluan_2.zip)                                 | GaoZhongluan_2      | 有道          |
| 35   | ![新东方初中词汇](https://nos.netease.com/ydschool-online/newOriental_ChuZhong_3.jpg)                                    | 新东方初中词汇              | 1803     | 1149674  | 5117     | [本地地址](book/1521164652700_ChuZhong_3.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164652700_ChuZhong_3.zip)                                         | ChuZhong_3          | 新东方        |
| 36   | ![新东方高中词汇](https://nos.netease.com/ydschool-online/newOriental_GaoZhong_3.jpg)                                    | 新东方高中词汇              | 2340     | 1346745  | 2619     | [本地地址](book/1521164679263_GaoZhong_3.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164679263_GaoZhong_3.zip)                                         | GaoZhong_3          | 新东方        |
| 37   | ![人教版小学英语-三年级上册](https://nos.netease.com/ydschool-online/2_youdao_PEPXiaoXue3_1.jpg)                         | 人教版小学英语-三年级上册   | 64       | 42478    | 378234   | [本地地址](book/1521164661774_PEPXiaoXue3_1.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164661774_PEPXiaoXue3_1.zip)                                   | PEPXiaoXue3_1       | 人教版        |
| 38   | ![人教版小学英语-三年级下册](https://nos.netease.com/ydschool-online/2_youdao_PEPXiaoXue3_2.jpg)                         | 人教版小学英语-三年级下册   | 72       | 40675    | 103262   | [本地地址](book/1521164656604_PEPXiaoXue3_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164656604_PEPXiaoXue3_2.zip)                                   | PEPXiaoXue3_2       | 人教版        |
| 39   | ![人教版小学英语-四年级上册](https://nos.netease.com/ydschool-online/2_youdao_PEPXiaoXue4_1.jpg)                         | 人教版小学英语-四年级上册   | 84       | 47587    | 89159    | [本地地址](book/1521164677447_PEPXiaoXue4_1.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164677447_PEPXiaoXue4_1.zip)                                   | PEPXiaoXue4_1       | 人教版        |
| 40   | ![人教版小学英语-四年级下册](https://nos.netease.com/ydschool-online/2_youdao_PEPXiaoXue4_2.jpg)                         | 人教版小学英语-四年级下册   | 104      | 53505    | 50627    | [本地地址](book/1521164663086_PEPXiaoXue4_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164663086_PEPXiaoXue4_2.zip)                                   | PEPXiaoXue4_2       | 人教版        |
| 41   | ![人教版小学英语-五年级上册](https://nos.netease.com/ydschool-online/2_youdao_PEPXiaoXue5_1.jpg)                         | 人教版小学英语-五年级上册   | 131      | 71424    | 65368    | [本地地址](book/1530101080610_PEPXiaoXue5_1.zip) [原始地址](http://ydschool-online.nos.netease.com/1530101080610_PEPXiaoXue5_1.zip)                                   | PEPXiaoXue5_1       | 人教版        |
| 42   | ![人教版小学英语-五年级下册](https://nos.netease.com/ydschool-online/2_youdao_PEPXiaoXue5_2.jpg)                         | 人教版小学英语-五年级下册   | 156      | 87211    | 37829    | [本地地址](book/1530101073491_PEPXiaoXue5_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1530101073491_PEPXiaoXue5_2.zip)                                   | PEPXiaoXue5_2       | 人教版        |
| 43   | ![人教版小学英语-六年级上册](https://nos.netease.com/ydschool-online/2_youdao_PEPXiaoXue6_1.jpg)                         | 人教版小学英语-六年级上册   | 130      | 76633    | 69570    | [本地地址](book/1530101075331_PEPXiaoXue6_1.zip) [原始地址](http://ydschool-online.nos.netease.com/1530101075331_PEPXiaoXue6_1.zip)                                   | PEPXiaoXue6_1       | 人教版        |
| 44   | ![人教版小学英语-六年级下册](https://nos.netease.com/ydschool-online/2_youdao_PEPXiaoXue6_2.jpg)                         | 人教版小学英语-六年级下册   | 108      | 64879    | 38501    | [本地地址](book/1521164632445_PEPXiaoXue6_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164632445_PEPXiaoXue6_2.zip)                                   | PEPXiaoXue6_2       | 人教版        |
| 45   | ![人教版初中英语-七年级上册](https://nos.netease.com/ydschool-online/3_youdao_PEPChuZhong7_1.jpg)                        | 人教版初中英语-七年级上册   | 392      | 203341   | 126509   | [本地地址](book/1530101067588_PEPChuZhong7_1.zip) [原始地址](http://ydschool-online.nos.netease.com/1530101067588_PEPChuZhong7_1.zip)                                 | PEPChuZhong7_1      | 人教版        |
| 46   | ![人教版初中英语-七年级下册](https://nos.netease.com/ydschool-online/3_youdao_PEPChuZhong7_2.jpg)                        | 人教版初中英语-七年级下册   | 492      | 266712   | 40795    | [本地地址](book/1521164677043_PEPChuZhong7_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164677043_PEPChuZhong7_2.zip)                                 | PEPChuZhong7_2      | 人教版        |
| 47   | ![人教版初中英语-八年级上册](https://nos.netease.com/ydschool-online/3_youdao_PEPChuZhong8_1.jpg)                        | 人教版初中英语-八年级上册   | 419      | 222704   | 69006    | [本地地址](book/1530101070747_PEPChuZhong8_1.zip) [原始地址](http://ydschool-online.nos.netease.com/1530101070747_PEPChuZhong8_1.zip)                                 | PEPChuZhong8_1      | 人教版        |
| 48   | ![人教版初中英语-八年级下册](https://nos.netease.com/ydschool-online/3_youdao_PEPChuZhong8_2.jpg)                        | 人教版初中英语-八年级下册   | 466      | 244325   | 31355    | [本地地址](book/1521164666522_PEPChuZhong8_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164666522_PEPChuZhong8_2.zip)                                 | PEPChuZhong8_2      | 人教版        |
| 49   | ![人教版初中英语-九年级全册](https://nos.netease.com/ydschool-online/3_youdao_PEPChuZhong9_1.jpg)                        | 人教版初中英语-九年级全册   | 551      | 278981   | 69649    | [本地地址](book/1530101078234_PEPChuZhong9_1.zip) [原始地址](http://ydschool-online.nos.netease.com/1530101078234_PEPChuZhong9_1.zip)                                 | PEPChuZhong9_1      | 人教版        |
| 50   | ![外研社版初中英语-七年级上册](https://nos.netease.com/ydschool-online/reciteWord_1545032535025_WaiYanSheChuZhong_1.png) | 外研社版初中英语-七年级上册 | 629      | 351737   | 1031     | [本地地址](book/reciteWord_1545032533243_WaiYanSheChuZhong_1.zip) [原始地址](http://ydschool-online.nos.netease.com/reciteWord_1545032533243_WaiYanSheChuZhong_1.zip) | WaiYanSheChuZhong_1 | 外研社版      |
| 51   | ![外研社版初中英语-七年级下册](https://nos.netease.com/ydschool-online/reciteWord_1545032535434_WaiYanSheChuZhong_2.png) | 外研社版初中英语-七年级下册 | 438      | 247606   | 693      | [本地地址](book/reciteWord_1545032493536_WaiYanSheChuZhong_2.zip) [原始地址](http://ydschool-online.nos.netease.com/reciteWord_1545032493536_WaiYanSheChuZhong_2.zip) | WaiYanSheChuZhong_2 | 外研社版      |
| 52   | ![外研社版初中英语-八年级上册](https://nos.netease.com/ydschool-online/reciteWord_1545032535509_WaiYanSheChuZhong_3.png) | 外研社版初中英语-八年级上册 | 320      | 184306   | 552      | [本地地址](book/reciteWord_1545032532744_WaiYanSheChuZhong_3.zip) [原始地址](http://ydschool-online.nos.netease.com/reciteWord_1545032532744_WaiYanSheChuZhong_3.zip) | WaiYanSheChuZhong_3 | 外研社版      |
| 53   | ![外研社版初中英语-八年级下册](https://nos.netease.com/ydschool-online/reciteWord_1545032534561_WaiYanSheChuZhong_4.png) | 外研社版初中英语-八年级下册 | 266      | 147166   | 629      | [本地地址](book/reciteWord_1545032533455_WaiYanSheChuZhong_4.zip) [原始地址](http://ydschool-online.nos.netease.com/reciteWord_1545032533455_WaiYanSheChuZhong_4.zip) | WaiYanSheChuZhong_4 | 外研社版      |
| 54   | ![外研社版初中英语-九年级上册](https://nos.netease.com/ydschool-online/reciteWord_1545032534804_WaiYanSheChuZhong_5.png) | 外研社版初中英语-九年级上册 | 381      | 196315   | 462      | [本地地址](book/reciteWord_1545032533808_WaiYanSheChuZhong_5.zip) [原始地址](http://ydschool-online.nos.netease.com/reciteWord_1545032533808_WaiYanSheChuZhong_5.zip) | WaiYanSheChuZhong_5 | 外研社版      |
| 55   | ![外研社版初中英语-九年级下册](https://nos.netease.com/ydschool-online/reciteWord_1545032534322_WaiYanSheChuZhong_6.png) | 外研社版初中英语-九年级下册 | 128      | 72801    | 495      | [本地地址](book/reciteWord_1545032534071_WaiYanSheChuZhong_6.zip) [原始地址](http://ydschool-online.nos.netease.com/reciteWord_1545032534071_WaiYanSheChuZhong_6.zip) | WaiYanSheChuZhong_6 | 外研社版      |
| 56   | ![人教版高中英语-必修1](https://nos.netease.com/ydschool-online/3_youdao_PEPGaoZhong_1.jpg)                              | 人教版高中英语-必修 1       | 311      | 145874   | 114721   | [本地地址](book/1521164674793_PEPGaoZhong_1.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164674793_PEPGaoZhong_1.zip)                                   | PEPGaoZhong_1       | 人教版        |
| 57   | ![人教版高中英语-必修2](https://nos.netease.com/ydschool-online/3_youdao_PEPGaoZhong_2.jpg)                              | 人教版高中英语-必修 2       | 319      | 148700   | 24566    | [本地地址](book/1521164678610_PEPGaoZhong_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164678610_PEPGaoZhong_2.zip)                                   | PEPGaoZhong_2       | 人教版        |
| 58   | ![人教版高中英语-必修3](https://nos.netease.com/ydschool-online/3_youdao_PEPGaoZhong_3.jpg)                              | 人教版高中英语-必修 3       | 366      | 162383   | 47142    | [本地地址](book/1521164676690_PEPGaoZhong_3.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164676690_PEPGaoZhong_3.zip)                                   | PEPGaoZhong_3       | 人教版        |
| 59   | ![人教版高中英语-必修4](https://nos.netease.com/ydschool-online/3_youdao_PEPGaoZhong_4.jpg)                              | 人教版高中英语-必修 4       | 307      | 129777   | 16866    | [本地地址](book/1521164657462_PEPGaoZhong_4.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164657462_PEPGaoZhong_4.zip)                                   | PEPGaoZhong_4       | 人教版        |
| 60   | ![人教版高中英语-必修5](https://nos.netease.com/ydschool-online/3_youdao_PEPGaoZhong_5.jpg)                              | 人教版高中英语-必修 5       | 357      | 162923   | 24188    | [本地地址](book/1521164657147_PEPGaoZhong_5.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164657147_PEPGaoZhong_5.zip)                                   | PEPGaoZhong_5       | 人教版        |
| 61   | ![人教版高中英语-选修6](https://nos.netease.com/ydschool-online/3_youdao_PEPGaoZhong_6.jpg)                              | 人教版高中英语-选修 6       | 391      | 172125   | 12203    | [本地地址](book/1521164629184_PEPGaoZhong_6.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164629184_PEPGaoZhong_6.zip)                                   | PEPGaoZhong_6       | 人教版        |
| 62   | ![人教版高中英语-选修7](https://nos.netease.com/ydschool-online/3_youdao_PEPGaoZhong_7.jpg)                              | 人教版高中英语-选修 7       | 384      | 174623   | 8576     | [本地地址](book/1521164648940_PEPGaoZhong_7.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164648940_PEPGaoZhong_7.zip)                                   | PEPGaoZhong_7       | 人教版        |
| 63   | ![人教版高中英语-选修8](https://nos.netease.com/ydschool-online/3_youdao_PEPGaoZhong_8.jpg)                              | 人教版高中英语-选修 8       | 420      | 187484   | 7481     | [本地地址](book/1521164666266_PEPGaoZhong_8.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164666266_PEPGaoZhong_8.zip)                                   | PEPGaoZhong_8       | 人教版        |
| 64   | ![人教版高中英语-选修9](https://nos.netease.com/ydschool-online/3_youdao_PEPGaoZhong_9.jpg)                              | 人教版高中英语-选修 9       | 352      | 145854   | 3759     | [本地地址](book/1521164670293_PEPGaoZhong_9.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164670293_PEPGaoZhong_9.zip)                                   | PEPGaoZhong_9       | 人教版        |
| 65   | ![人教版高中英语-选修10](https://nos.netease.com/ydschool-online/3_youdao_PEPGaoZhong_10.jpg)                            | 人教版高中英语-选修 10      | 361      | 140211   | 3470     | [本地地址](book/1521164634796_PEPGaoZhong_10.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164634796_PEPGaoZhong_10.zip)                                 | PEPGaoZhong_10      | 人教版        |
| 66   | ![人教版高中英语-选修11](https://nos.netease.com/ydschool-online/3_youdao_PEPGaoZhong_11.jpg)                            | 人教版高中英语-选修 11      | 309      | 120512   | 4450     | [本地地址](book/1521164639915_PEPGaoZhong_11.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164639915_PEPGaoZhong_11.zip)                                 | PEPGaoZhong_11      | 人教版        |
| 67   | ![初中英语词汇（正序版）](https://nos.netease.com/ydschool-online/youdao_ChuZhong_2.jpg)                                 | 初中英语词汇（正序版）      | 1420     | 912718   | 82677    | [本地地址](book/1521164647926_ChuZhong_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164647926_ChuZhong_2.zip)                                         | ChuZhong_2          | 有道          |
| 68   | ![高中英语词汇（正序版）](https://nos.netease.com/ydschool-online/youdao_GaoZhong_2.jpg)                                 | 高中英语词汇（正序版）      | 3668     | 1999328  | 172704   | [本地地址](book/1521164675301_GaoZhong_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164675301_GaoZhong_2.zip)                                         | GaoZhong_2          | 人教版        |
| 69   | ![商务英语词汇](https://nos.netease.com/ydschool-online/youdao_BEC_2.jpg)                                                | 商务英语词汇                | 2753     | 1494016  | 300528   | [本地地址](book/1521164626760_BEC_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164626760_BEC_2.zip)                                                   | BEC_2               | BEC           |
| 70   | ![新东方BEC词汇](https://nos.netease.com/ydschool-online/newOriental_BEC_3.jpg)                                          | 新东方 BEC 词汇             | 2825     | 1502966  | 4659     | [本地地址](book/1521164649506_BEC_3.zip) [原始地址](http://ydschool-online.nos.netease.com/1521164649506_BEC_3.zip)                                                   | BEC_3               | 新东方、BEC   |
| 71   | ![北师大版高中必修一](https://nos.netease.com/ydschool-online/reciteWord_BeiShiGaoZhong_1.jpg)                           | 北师大版高中必修一          | 226      | 111762   | 5571     | [本地地址](book/reciteWord_BeiShiGaoZhong_1.zip) [原始地址](http://ydschool-online.nos.netease.com/reciteWord_BeiShiGaoZhong_1.zip)                                   | BeiShiGaoZhong_1    | 北师版        |
| 72   | ![北师大版高中必修二](https://nos.netease.com/ydschool-online/reciteWord_BeiShiGaoZhong_2.jpg)                           | 北师大版高中必修二          | 244      | 128789   | 1822     | [本地地址](book/1530101085958_BeiShiGaoZhong_2.zip) [原始地址](http://ydschool-online.nos.netease.com/1530101085958_BeiShiGaoZhong_2.zip)                             | BeiShiGaoZhong_2    | 北师版        |
| 73   | ![北师大版高中必修三](https://nos.netease.com/ydschool-online/reciteWord_BeiShiGaoZhong_3.jpg)                           | 北师大版高中必修三          | 295      | 150496   | 1437     | [本地地址](book/1530101089143_BeiShiGaoZhong_3.zip) [原始地址](http://ydschool-online.nos.netease.com/1530101089143_BeiShiGaoZhong_3.zip)                             | BeiShiGaoZhong_3    | 北师版        |
| 74   | ![北师大版高中必修四](https://nos.netease.com/ydschool-online/reciteWord_BeiShiGaoZhong_4.jpg)                           | 北师大版高中必修四          | 336      | 163541   | 1294     | [本地地址](book/reciteWord_BeiShiGaoZhong_4.zip) [原始地址](http://ydschool-online.nos.netease.com/reciteWord_BeiShiGaoZhong_4.zip)                                   | BeiShiGaoZhong_4    | 北师版        |
| 75   | ![北师大版高中必修五](https://nos.netease.com/ydschool-online/reciteWord_BeiShiGaoZhong_5.jpg)                           | 北师大版高中必修五          | 327      | 166181   | 1515     | [本地地址](book/reciteWord_BeiShiGaoZhong_5.zip) [原始地址](http://ydschool-online.nos.netease.com/reciteWord_BeiShiGaoZhong_5.zip)                                   | BeiShiGaoZhong_5    | 北师版        |
| 76   | ![北师大版高中选修六](https://nos.netease.com/ydschool-online/reciteWord_BeiShiGaoZhong_6.jpg)                           | 北师大版高中选修六          | 271      | 121058   | 1071     | [本地地址](book/reciteWord_BeiShiGaoZhong_6.zip) [原始地址](http://ydschool-online.nos.netease.com/reciteWord_BeiShiGaoZhong_6.zip)                                   | BeiShiGaoZhong_6    | 北师版        |
| 77   | ![北师大版高中选修七](https://nos.netease.com/ydschool-online/reciteWord_BeiShiGaoZhong_7.jpg)                           | 北师大版高中选修七          | 334      | 166699   | 880      | [本地地址](book/1530101082895_BeiShiGaoZhong_7.zip) [原始地址](http://ydschool-online.nos.netease.com/1530101082895_BeiShiGaoZhong_7.zip)                             | BeiShiGaoZhong_7    | 北师版        |
| 78   | ![北师大版高中选修八](https://nos.netease.com/ydschool-online/reciteWord_BeiShiGaoZhong_8.jpg)                           | 北师大版高中选修八          | 364      | 171446   | 796      | [本地地址](book/reciteWord_BeiShiGaoZhong_8.zip) [原始地址](http://ydschool-online.nos.netease.com/reciteWord_BeiShiGaoZhong_8.zip)                                   | BeiShiGaoZhong_8    | 北师版        |
| 79   | ![北师大版高中选修九](https://nos.netease.com/ydschool-online/reciteWord_BeiShiGaoZhong_9.jpg)                           | 北师大版高中选修九          | 299      | 122391   | 493      | [本地地址](book/reciteWord_BeiShiGaoZhong_9.zip) [原始地址](http://ydschool-online.nos.netease.com/reciteWord_BeiShiGaoZhong_9.zip)                                   | BeiShiGaoZhong_9    | 北师版        |
| 80   | ![北师大版高中选修十](https://nos.netease.com/ydschool-online/reciteWord_BeiShiGaoZhong_10.jpg)                          | 北师大版高中选修十          | 267      | 108057   | 485      | [本地地址](book/reciteWord_BeiShiGaoZhong_10.zip) [原始地址](http://ydschool-online.nos.netease.com/reciteWord_BeiShiGaoZhong_10.zip)                                 | BeiShiGaoZhong_10   | 北师版        |
| 81   | ![北师大版高中选修十一](https://nos.netease.com/ydschool-online/reciteWord_BeiShiGaoZhong_11.jpg)                        | 北师大版高中选修十一        | 330      | 139130   | 739      | [本地地址](book/reciteWord_BeiShiGaoZhong_11.zip) [原始地址](http://ydschool-online.nos.netease.com/reciteWord_BeiShiGaoZhong_11.zip)                                 | BeiShiGaoZhong_11   | 北师版        |

# 致谢

感谢有道团队以及考神团队为中国教育与中外交流做出的重要贡献。
