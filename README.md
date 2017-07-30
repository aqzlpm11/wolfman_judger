# wolfman_judger
狼人杀面杀助手 -- 第一夜法官

## 写在前面
### 启发

在线下狼人杀的时候，经常出现人数不够的情况，比如总共就8个人。
这个时候，再有一个人当法官，游戏就玩不了了……

所以经常的做法，就是去附近叫一个人，充当第一个晚上的法官。第一天晚上死亡的玩家，充当剩余游戏的法官。
（当然，如果被女巫救了，没死人，那就很尴尬……）

但是，并不是附近总能叫到人充当法官的。怎么办呢？在我线下的经历中，观察到手机是必带的物品。由此，我构想，可否写一个程序，来充当我们的第一夜法官？
因此，这个repository就出现了。

### 技术选择

考虑到应用场景，这个程序需要

* 免安装
* 跨IOS和Android
* 操作简单

根据前两点，使用网页或者基于微信的形式是比较好的。又根据自己的技术能力，在此选择了网页方式。设想，可通过微信群来共享游戏链接，来让大家进入同一个应用环境。

### 自身定位

同时，还需要强烈的认识到，这是一个**工具**，而不是一个线上的狼人杀（来来来，大家坐成一圈，掏出手机，按屏幕提示，开始打字！按键说话！）。
所以在这个定位下，这个程序需要完成以下功能：

* 提示游戏流程
* 完成角色行动

其不需要：

* 给玩家分发身份（虽然这个功能在没带牌的情况下也不错，但是基本上大家都有牌。线下聚会，还是摸牌比较爽不是？~）
* 线上聊天

总而言之，这个程序只起到**辅助工具**的作用！并且尽可能的**弱化其存在感**，以免将欢乐的线下聊天聚会，变成线下玩手机聚会。

（以上写给自己，免得写歪了`^_^`）

