<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>
<div align="center">
<h1 align="center">ð nonebot_plugin_wordsnorote</h1>
â¨ å¥ä»¬å¥ä»¬ï¼èåè¯ä¹ï¼å¥ä»¬ï¼ â¨

</div>

<p align="center">
  <a href="https://github.com/GC-ZF/nonebot_plugin_wordsnorote/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/GC-ZF/nonebot_plugin_wordsnorote" alt="license">
  </a>
  <a href="https://pypi.python.org/pypi/nonebot_plugin_wordsnorote">
    <img src="https://img.shields.io/pypi/v/nonebot_plugin_wordsnorote" alt="pypi">
  </a>
  <img src="https://img.shields.io/badge/python-3.7.3+-blue" alt="python">
  <img  src="https://visitor-badge.glitch.me/badge?page_id=nonebot_plugin_wordsnorote" /><br />
</p></br>


## æä»¶æè¿°

ä¸æ¬¾åºäº[Nonebot2](https://github.com/nonebot/nonebot2)çæä»¶

**ä¸æ¯å§ï¼ççæäººæ¿QQèåè¯ä¹ï¼ï¼**

<div align="center">
  <img height="300px" src="https://testingcf.jsdelivr.net/gh/GC-ZF/nonebot_plugin_wordsnorote/img/example1.png">
</div>

åè½æ¯æåæçï¼è¿ä¸ªåè½ææè§å¾é¸¡èï¼ æä¸ç´ä¹ æ¯äºAPPèåè¯ï¼æ¨èå æ¬¾è½¯ä»¶

* çµèï¼[Uahh/ToastFish: ä¸ä¸ªå©ç¨æ¸é±¼æ¶é´èåè¯çè½¯ä»¶](https://github.com/Uahh/ToastFish)ï¼å°æä¸å¥½ç¨ççµèç«¯åè¯è½¯ä»¶ï¼ï¼
* ææºï¼æè´åè¯ãä¸èåè¯
* å¹³æ¿ï¼æ¬§éè¯å¸ï¼åè½å¼ºå¤§ï¼ï¼

ä½å¥¹è¯´å«äººåæ¶æ¯**QQé«é¢**ç¹å¼ï¼è¿ä¸ªçç±å¥½åä¹æºæéçï¼æä»¥ç®ååäºä¸ä¸ªæºå¨äººæä»¶ãä½æ è®ºä»ä¹æ¹å¼ï¼éå¨**åæ**ï¼

pyå°ç½ï¼å¦ææä»»ä½é®é¢ãå»ºè®®ï¼æ¬¢è¿[issues](https://github.com/GC-ZF/nonebot_plugin_wordsnorote/issues)

## å®è£
```python
pip install nonebot_plugin_wordsnorote
```
## éç½®é¡¹
å¨`bot.py`ä¸­æ·»å 
```python
nonebot.load_plugin("nonebot_plugin_wordsnorote")
```
å¨`.env`ï¼å¦ï¼`.env.dev`ï¼ä¸­éç½®åæ°è¯´æ

| config    | type | default | example        | usage                    |
| --------- | ---- | ------- | -------------- | ------------------------ |
| num_words | int  | 20      | num_words = 50 | æ¯æ¥æ¨éåè¯æ°éï¼é»è®¤20 |

æ¯ä¸ä¸ªQQå·ç¸å½äºä¸ä¸ªIDï¼æ°æ®ä¿å­å¨`data/wordsnoreote/student.json`ï¼å¶ä¸­`wordID`å³æèåè¯æ°é

## æ´æ¢è¯åº

å ä¸ºæé¢åçæ¯å¤§å­¦çï¼æä»¥é»è®¤è¯åºæ¯èç è±è¯­ï¼[kajweb/dict](https://github.com/kajweb/dict)ä»åºå·²å°æéæ°æ®æ´çï¼åæ¬å°å­¦å°å¤§å­¦çè¯¾æ¬ãåå­çº§ãèç ãéæ...ï¼81æ¬ä¹¦ï¼å°å¼ ä¸å¯è½åå°æ¬æ¬é½å¼å®¹ï¼æä»¥åäºä¸äºè½¬æ ¼å¼ä»£ç ï¼æ¹ä¾¿å¤§å®¶æ¢ä¹¦

1. ä»ä»åºä¸­ä¸è½½è¯åº
2. è¿è¡ä»åºä¸­`turn_json.py`è½¬æ ¼å¼ï¼æ³¨æè±æ æ¯å¦ä¹±ç ï¼æ¨èå¨MacæLinuxç¯å¢ä¸è¿è¡ï¼å¾®è½¯ç¼ç é»è®¤GBKï¼å¹¶éåä¸éæ°æ®ï¼æ¥çæ¯å¦æç¼ºå¤±
3. è¿è¡ä»åºä¸­`fix_keys.py`å¡«è¡¥ç¼ºå¤±æ°æ®ï¼ä»¥èç è¯åºç¼ºå¤±ä¾å¥ä¸åé³ä¸ºä¾ï¼æ ¹æ®å®éæåµä¿®æ¹`try...expect`å¼å¸¸ï¼
3. å°è¯åºéå½åå¹¶æ¾å¨`data/wordsnorote/wordbook.json`

å¦æè½¬æ ¼å¼å¤±è´¥ï¼ä½ ä¹å¯ä»¥éè¿**issue**çä¸è¯åºç **åå­\id** ï¼åªè¦æºæä»¶ç¼ºçä¸è¥¿ä¸å¤ï¼å¯ä»¥ä¿®å¤ï¼å°å¼ æ½ç©ºå¯ä»¥å¸®å¿å¼ä¸ä¸ï¼

å·²è½¬æ ¼å¼çè¯åºå¨æ¬ä»åº`Dict\å·²æ´çè¯åº`ä¸

## ç¤ºä¾

<div align="center">
  <img height="300px" src="https://testingcf.jsdelivr.net/gh/GC-ZF/nonebot_plugin_wordsnorote/img/example2.png">
  <img height="300px" src="https://testingcf.jsdelivr.net/gh/GC-ZF/nonebot_plugin_wordsnorote/img/example3.png">
</div>

## æ´æ°è®°å½

2022.8.29ï¼å¼å§æ¬å°æå»ºï¼local_testæä»¶å¤¹ï¼ãç¼åè¯åºè½¬æ ¼å¼ä¸ä¿®å¤ãå®ç°æä»¶åï¼ä¿®æ¹æææä»¶è¯»åè·¯å¾ï¼å¢å èªå®ä¹åè¯æ°éãèªå®ä¹è¯åºåè½

2022.8.30ï¼åå¤æµè¯ï¼QQåå¹¶è½¬åä¸è½è¶è¿100æ¡ï¼éæé»è¾ï¼åå¸è³ååº

æªæ¥å¯è½æ·»å çåè½

* æ·»å å¤ä¹ åè½ï¼æä¸ææä¸ºï¼åéåè¯IDèå´ï¼ä¾å¦`å¤ä¹ x~y`ï¼å°x~yé¡ºåºéææä¹±ï¼ååéä¸æ¡åªåå«åè¯çåå¹¶æ¶æ¯ï¼ååéä¸æ¡ç­æ¡çåå¹¶æ¶æ¯ãä¼å¿ï¼èªç±æå®å¤ä¹ èå´ï¼ç¸å¯¹äºåªå¤ä¹ æ¨æ¥çåè¯çµæ´»ä¸äº
