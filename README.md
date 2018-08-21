# JXQuant
该库主要分享“匠芯量化”公众号内的策略源码，更多策略细节请关注微信公众号：“匠芯量化”（微信搜索公众号“jxquant”）。

目录：

Init_StockALL_Sp.py  —— 【数据采集】利用tushare接口将日线行情存储到本地数据库。
DC.py   ——  【数据预处理】将本地存储的日基础行情整合成一份训练集。
SVM.py   ——  【SVM建模】对个股用SVM进行建模，训练和预测。
Model_Evaluate.py   ——   【模型评估】通过回测+推进式建模的方式对模型进行评估，主要计算查准率Precision，查全率Recall，F1分值，并存入结果表。
Portfolio.py   ——   【仓位管理】基于马科维茨投资组合理论，计算一段时间序列内投资组合的风险、仓位配比和夏普率，有市场方向和最佳收益方向两种结果。
MY_CAP.py   ——   【回测】封装类，用于回测过程中获取最新的资产账户相关数据。
