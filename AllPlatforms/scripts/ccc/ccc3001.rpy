label ccc3001:
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(2,0)
    with Dissolve(500.0/1000.0)
    play se "SE001"
    call gl(0,"bgcc0005as")
    call vsp(0,1)
    call gl(1,"TCSY0000s|tcsy")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with Pixellate(300.0*2/1000.0,5)
    play bgm "bgm/bgm015.ogg"
    "去年の初夏だった。"
    "新川豊と出会ったのは。"
    "蝉のうるさい夏だった。"
    "偶然、ぶつかった。"
    "妙に会話が弾んで。"
    "ウマがあった。"
    "群青には完全に自分の世界で生きている者もいる。"
    "人を傷つけやすい者もいる。"
    "ある頃から、世界は狂人を生み出しはじめた。"
    "その多くが人を傷つけた。"
    "心の病は、ただ己だけの問題ではなくなっていた。"
    "原因はわからない。"
    "政府はいくつかの対策を打ち出したが、その内容が広く報道されることはなかった。"
    "水面下で動いている、と曜子ちゃんは言っていた。"
    "詳細は不明。"
    "少なくとも、世界が緩慢な狂気に浸されていることは……自分の胸に聞けばよく理解できた。"
    "だから群青学院は存在した。"
    "隔離施設として。"
    "留年は日常茶飯事。"
    "だが何年かけても症状が回復しない者は、さらなる施設へと送られる。"
    "そういう人々は、ほとんど他者との接触を必要としない。"
    "独力で生きる力には欠けているが、当人の心は、もう人のそれを離れてしまっているのだ。"
    "だから。"
    "群青では友達を作るのは、少し難しい。"
    "対話が成立しにくいからだ。"
    "１クラスで、１０人くらいだろうか。"
    "まともに会話が成り立つのは。"
    call gl(1,"TCSY0001s|tcsy")
    call vsp(1,1)
    with dissolve
    voice "vmcca0011bshi033a"
    "新川『ＯＫ、なんとかやっていけそうな気がしてきた』"
    太一 "「…………」"
    "誰が悪かったのかな。"
    "俺か。"
    "それともヤツか。"
    "結論は出ない。"
    "涙も出ない。"
    stop bgm
    stop se
    "まだ、出ない。"
    return
    #