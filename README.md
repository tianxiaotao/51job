# 51job  Web/Js 数据逆向学习

逆向接口地址:  https://we.51job.com/api/job/search-pc
逆向参数: Sign, UUID

学习过程中主要采用js断点单步调试方法进行定位js加密位置.  调试过程中出现关键词【HmacSHA256】可知为SHA-256生成哈希值的HMAC算法
js加载方式为: webpack , 这样就只需找到加载器 就可扣取对应方法模块进行加密还原
详细方式查看博客: https://blog.csdn.net/Q718330882/article/details/138410187?spm=1001.2014.3001.5501


cookie 失效问题追踪, acw_sc__v2 重获取
定位cookie生成参数时需要用到js HOOK脚本  这样可以快速的断点到JS生成位置
说到这里就会给返回一个js文件.  那么这个js文件就是生成cookie  acw_sc__v2 值的关键
这里就需要保存下来, 然后进行补环境操作即可
详细方式查看博客: https://blog.csdn.net/Q718330882/article/details/138412237
