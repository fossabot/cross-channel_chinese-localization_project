label ccb0001:
    #textclear
    call gl(0,"bgcc0001b")
    call vsp(0,1)
    call vsp(1,0)
    with Pixellate(300.0*2/1000.0,5)
    #modewin
    "放送部の合宿だった。"
    play bgm "bgm/bgm007.ogg"
    "俺たち一年生が進級し、幸せな三年生が引退して。"
    "新しい一年生が入ってきて。"
    "新たな面子は七人で。"
    "でも本当は八人で。"
    "７／８ならまあＯＫか、と俺は思っていた。"
    "彼女は……どうせ呼べばすぐにやってくる。"
    "７人集めるのに。"
    "支払った代価は安くない。"
    "そりゃもう大騒ぎさ。"
    "一因として、教員が参加しなかったことがある。"
    "なぜならこれプライベートな部活動だったからだ。"
    "学院には内緒のオチャメ。"
    "公になれば、ちょっとした騒ぎになる。"
    "けど平気だと思った。"
    "……………………。"
    "そうして、合宿が終わり。"
    "七人は帰路に着いた。"
    call gl(0,"bgcc0015b")
    call vsp(0,1)
    "途中で日が暮れた。"
    "ひどく長い時間、歩いていた気がする。"
    "何時間も。"
    "普段は一時間もかからない道だ。"
    "疲労のせいか。"
    "誰も何も言わなかった。"
    "七つの足音だけの世界だった。"
    "異様に静かな山道。"
    "虫の音さえも耳に届かない。"
    "空気までも冷たく感じさせる。"
    "夏だというのに。"
    call gl(0,"bgcc0015b")
    call vsp(0,1)
    with Pixellate(300.0*2/1000.0,5)
    "暗くても、見えたから。"
    "道が見えたから。"
    "俺は昔から夜目がきいた。"
    "道を間違えたのかなと思い出した頃、町に出た。"
    stop bgm
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "人類は滅亡していた。"
    pause (500.0/1000.0)
    pause (500.0/1000.0)
    #textoff
    with Dissolve(500.0/1000.0)
    pause (1000.0/1000.0)
    call gl(0,"TITLE2")
    call vsp(0,1)
    play se "seeye002"
    #dwave 1,"se/seeye002.ogg"
    with Pixellate(300.0*2/1000.0,5)
    pause (5000.0/1000.0)
    return
    #