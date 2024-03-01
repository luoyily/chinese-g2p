简单的中文G2P转换，使用传统的字典+分词匹配方法。（其实效果也还行，没有很差）

主要帮隔壁NaruseMioShirakana做的，为了方便搬到其他语言，所以做的很简单，算是Minimum example了，有需要也可以拿去用，之后会适当扩大字典以覆盖更多情况。

字典由网上爬取并做了简单清洗，在Release中可下载。

字典样本：

```json
{
    "测试": {
        "phoneme": ["c", "e", "sh", "i"],
        "tone": [0, 4, 0, 4]
    }
}
```

G2P 示例：

```
# 字符串
我这次回来这里呢，是为了再一次，倾听星星的声音呢。 
 wo3 zhe4 ci4 hui5 lai2 zhe4 li3 ne5 shi4 wei4 le5 zai4 yi1 ci4 qing1 ting1 xing1 xing5 de5 sheng1 yin1 ne5
 有些风景，自然而然就在脑海中复苏。
 you3 xie5 feng1 jing3 zi4 ran2 er2 ran2 jiu5 zai4 nao3 hai3 zhong1 fu4 su1
有些记忆，就像是和飘落的樱花相呼应一样在我内心深处不断浮现。
 you3 xie5 ji4 yi4 jiu5 xiang5 shi4 he2 piao5 luo5 de5 ying1 hua5 xiang5 hu1 ying4 yi1 yang4 zai4 wo3 nei4 xin1 shen1 chu4 bu4 duan5 fu2 xian5
那些全是即使我不愿回想……也会浮现而来的景象。
 na4 xie5 quan5 shi4 ji2 shi3 wo3 bu4 yuan5 hui5 xiang5 ye3 hui5 fu2 xian5 er2 lai2 de5 jing3 xiang5
落英斑斓的樱花瓣在空中飞舞。
 luo5 ying1 ban1 lan2 de5 ying1 hua5 ban4 zai4 kong1 zhong1 fei1 wu3
「主人!早上了哦,快起来快起来」
 zhu3 ren2 zao3 shang4 liao5 o4 kuai5 qi3 lai2 kuai5 qi3 lai2
「不在恰当的时候做恰当的事情，你会后悔的,主人」
 bu4 zai4 qia5 dang4 de5 shi2 hou4 zuo5 qia5 dang4 de5 shi4 qing2 ni3 hui5 hou4 hui5 de5 zhu3 ren2
「就是和同龄的朋友大声地欢笑，愉快地玩耍」
 jiu5 shi4 he2 tong2 ling2 de5 peng2 you5 da4 sheng1 di4 huan5 xiao5 yu2 kuai5 di4 wan2 shua5
「不去体验这种理所当然的事情，往后的生活会很难受，主人」
 bu4 qu4 ti3 yan4 zhe4 zhong3 li3 suo5 dang1 ran2 de5 shi4 qing2 wang3 hou4 de5 sheng1 huo5 hui5 hen3 nan4 shou4 zhu3 ren2
# 完整
我这次回来这里呢，是为了再一次，倾听星星的声音呢。
Phoneme: ['w', 'o', 'zh', 'e', 'c', 'i', 'h', 'ui', 'l', 'ai', 'zh', 'e', 'l', 'i', 'n', 'e', 'sh', 'i', 'w', 'ei', 'l', 'e', 'z', 'ai', 'y', 'i', 'c', 'i', 'q', 'ing', 't', 'ing', 'x', 'ing', 'x', 'ing', 'd', 'e', 'sh', 'eng', 'y', 'in', 'n', 'e']
Tone: [0, 3, 0, 4, 0, 4, 0, 5, 0, 2, 0, 4, 0, 3, 0, 5, 0, 4, 0, 4, 0, 5, 0, 4, 0, 1, 0, 4, 0, 1, 0, 1, 0, 1, 0, 5, 0, 5, 0, 1, 0, 1, 0, 5]
```

