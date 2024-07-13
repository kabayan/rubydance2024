# Wow! technical background
この動画作成に関するドキュメント。

## 作成意図
- 生成AIを作品作りに使うのではなく、作品の評論を生成することができるかを確かめる。
- 評論は、その作品を鑑賞したすべての人が自由に行うことができるなら、生成AIが行ってもアーティストの権利を侵害しないはずという前提。
- AIであれば（制限付きながら）属人性や人間関係を考慮しない客観的な評論ができる可能性を確かめる。
- 2024年7月時点で利用できる各種AIを、評論に使えるかという観点で比較したかった。
- 作成した動画をCC4.0で公開することで、今後出てくる生成AIでの評論性能の比較のベンチマークとして利用できるようにしたかった。

## ライセンス
- 動画、楽曲はCC 4.0。商用利用する際は楽曲のライセンスは要確認。
- プログラムはApache License 2.0。

# 開催概要
- 『第16回 シアターΧ 国際舞台芸術祭2024（IDTF）』
- 2024年6月15日(土)～7月21日(日)
- “地球惑星人として、いま”
    - http://www.theaterx.jp/24/240615-240721p.php
- 2024/7/13 14:30 Rubydance『Wow！』として初演。

# 各種データ
## 動画データ
- https://www.youtube.com/watch?v=vxlv1rSnaO8
- https://github.com/kabayan/rubydance2024 (mp4)

## ソースコード
- Github
  - https://github.com/kabayan/rubydance2024

## 使用楽曲
- SoundCloudの楽曲を利用。
- 全てCC4.0。本編では全曲を使用しているわけではないことに注意。
- https://soundcloud.com/wouterhoogland/animal-roadtrip?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing
- https://soundcloud.com/jean-edouard/animal-vocal-synth?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing
- https://soundcloud.com/nsnoskill/satiswaltz?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing
- https://soundcloud.com/sunshinechristo/stam?si=79959555fce647869d9435a02785946d&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing
- https://soundcloud.com/lunova/lunova-labs-eplp-earth?si=256f2a0ccfec4a12afc706cbfd06c252&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

# 使用技術
## Generative AI
- GPT4o(OpenAI)
  - Web経由
- Gemini Pro 1.5(Google)
  - Google AI Studio経由。
- Clude3(Anthropic)
  - Web経由
## AI related
- Text-to-Speech AI(Google)
- DeepL (翻訳)
## etc
- Visual studio code, Python 3.10
- Davinci Resolve

# 構築手順
1. 楽曲を選んでつなげる
2. 背景色を提案してもらう
3. GPT4oに音楽ファイルを与えて解析
   - Gemini. Cludeでは音楽を解釈できず。
4. 背景動画を生成する
   - 背景色情報をCludeに与えてプログラムを生成。
   - Gemini, GPT4oではまともに生成できず。
5. 各パートのダンス動画を撮影。
6. 短いキャッチと評論作成
    - ダンス動画をGeminiに与えて生成。
    - 3つのパート毎に生成。
    - GPT4o、Clude3では生成できず。
7. 全ての評論のまとめ
    - GPT4oに３つの評論をまとめて与えて要約を生成。
    - Gemini. Cludeでも生成したが最もそれらしいのがGPT4oだった。
8. 楽曲、背景動画、ダンス動画、キャッチ、評論をDavinci Resolveで連結。
