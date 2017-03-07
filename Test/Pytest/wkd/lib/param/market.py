# coding: utf-8
'''
营销API参数化配置
'''
from .utils import Utils
import time
from .generic import Generic as g


class Market(object):

    def __init__(self,conf):
        self.conf = conf
        self.Utils = conf.Utils


    def card_coupons_add(self,**kwargs):
        '''
        添加卡券常用参数表

    =============     ===========    ============     ===================================
     字段              类型              默认               描述
    =============     ===========    ============     ===================================
     title              string         随机             卡券标题
     start_time        timestamp      当前时间          生效日期
     end_time          timestamp      明天              结束日期
    =============     ===========    ============     ===================================

        '''
        start_time = int(time.time()) - 3600
        end_time = start_time + 3600*24
        title = "测试卡券-" + self.Utils.rand_str()
        template = {"brand_name":"微客联盟","title":title,"logo_url":"http://imgcache.vikduo.com/static/44ae6a2fae8d1ae7acddc0129dabb128.png","color":"#55bd47","date_info_type":1,"begin":start_time,"end":end_time,"quantity":"999","get_limit":"200","can_give_friend":1,"code_type":"3","notice":"请出示卡券二维码","description":"使用说明。。。","service_phone":"13344556677","card_type":1,"assign":-1,"wx_card_type":2,"card_money":0,"money_limit":0,"card_discount":"8.8","exchange_content_text":"","product_ids":"","deal_detail":"8.8折折扣券1张，全场通用"}
        return g.get_params(template,kwargs)


    def card_coupons_receive_add(self,**kwargs):
        '''
        直接领取添加卡券
    =============     ===========    ============     ===================================
     字段              类型              默认               描述
    =============     ===========    ============     ===================================
     title              string         随机             卡券标题
     start_time        timestamp      当前时间          生效日期
     end_time          timestamp      明天              结束日期
    =============     ===========    ============     ===================================
        '''
        start_time=int(time.time())-3600
        end_time=start_time+3600*24
        title="直接领取卡券"+self.Utils.rand_str()
        template={"news":{"description":"信息摘要。。","title":title,"document_id":1336971,"imgsrc":"https://imgcache.vikduo.com/static/44ae6a2fae8d1ae7acddc0129dabb128.png"},"share_type":1,"title":"测试卡dxelp","card_type_id":991,"begin_time":start_time,"end_time":end_time}
        return g.get_params(template,kwargs)


    def card_coupons_policy_add(self,**kwargs):
        '''
        卡券赠送策略
        '''
        name="赠送卡券"+self.Utils.rand_str()
        template={"name":name,"type":1,"amount":10000,"card_type_ids":[991],"order_limit":1}
        return g.get_params(template, kwargs)




    def reduction_add(self,**kwargs):
        '''
        添加满减活动常用参数表

    =============     ===========    ============     ===================================
     字段              类型              默认               描述
    =============     ===========    ============     ===================================
     name               string          随机
     start_time         timestamp     当前时间          开始时间
     end_time           timestamp     明天              到期时间
    =============     ===========    ============     ===================================

        '''
        start_time = int(time.time()) - 3600
        end_time = start_time + 3600*24
        name = "满减-" + self.Utils.rand_str()
        template = {"name":name,"is_relate_all":1,"start_time":start_time,"end_time":end_time,"conditions":[{"condition_type":1,"level":1,"condition_min":90000,"strategys":[{"reduction_type":1,"amount":20000,"discount":"","point":"","card_type_id":"","red_packet_id":"","is_all_area":1,"area_id":"","area_cn":"","is_limit":2},{"reduction_type":3,"amount":"","discount":"","point":"20","card_type_id":"","red_packet_id":"","is_all_area":1,"area_id":"","area_cn":"","is_limit":2}]}],"products":[]}
        return g.get_params(template,kwargs)


    def cash_redpack_add(self,**kwargs):
        '''
        添加现金红包常用参数表

    =============     ===========    ============     ===================================
     字段              类型              默认               描述
    =============     ===========    ============     ===================================
     name               string         随机
     min_value           int            最小金额
     max_value           int            最大金额
     quantity            int            数量
    =============     ===========    ============     ===================================

        '''
        name = "红包-" + self.Utils.rand_str()
        template = {"type":1,"act_name":name,"send_name":"微客联盟","wishing":"恭喜发财！大吉大利！","remark":"一个测试红包","min_value":100,"max_value":100,"quantity":"50","deleted":2,"can_share":1}
        return g.get_params(template,kwargs)


    def redpack_add(self,**kwargs):
        '''
        添加红包活动常用参数表

    =============     ===========    ============     ===================================
    字段              类型              默认               描述
    =============     ===========    ============     ===================================
     name               string          随机             活动名称
    start_time          timestamp     当前时间          开始时间
    end_time            timestamp     明天              到期时间
    =============     ===========    ============     ===================================

        '''
        start_time = int(time.time()) - 3600
        end_time = start_time + 3600*24
        name = "红包活动-" + self.Utils.rand_str()
        template ={"activity":{"name":name,"desc":"1. 活动时间：#年#月#日#时 至 #年#月#日#时；\n2. 用户进入活动主页抢群红包，分享给好友瓜分群红包，瓜分到的红包金额自动发放到用户的商城账户；\n3. 用户必须关注微信公众号才能抢群红包；（打开强制关注后）；\n4. 每个用户只能发起一次活动，但可以瓜分不同用户转发的群红包；\n5. 瓜分群红包，先到先得，该群红包分完为止；\n6. 本活动最终解释权归XX商家所有。","start_time":start_time,"end_time":end_time,"share_type":1},"redPacketEvent":{"type":1,"red_packet_id":582,"num_per_packet":"100","red_packet_num":"100","is_attention":2},"shareMessage":{"title":"拼的是手气，抢的是红包~","desc":"#商家店名#发红包啦，不要白不要啊！","pic_id":10},"news":{"title":"拼的是手气，抢的是红包~","description":"亲，点击进入活动主页，意外惊喜等着你！","document_id":4}}
        return g.get_params(template,kwargs)


    def activity_points_add(self,**kwargs):
        '''
        添加积分活动常用参数表

    =============     ===========    ============     ===================================
     字段              类型              默认               描述
    =============     ===========    ============     ===================================
     name              string          随机             活动名称
     start_time        timestamp     当前时间           开始时间
     end_time          timestamp     第二天             到期时间
    =============     ===========    ============     ===================================
        '''
        start_time = int(time.time()) - 3600
        end_time = start_time + 3600*24
        name = "送积分-" + self.Utils.rand_str()
        template = {"activity":{"name":name,"expire_type":2,"start_time":start_time,"end_time":end_time},"pointsConsumption":{"type":2,"amount":1000,"points":"1","count_type":"2","together_buy_flag":2,"seckill_flag":2,"scan_flag":1,"normal_flag":1}}
        return g.get_params(template,kwargs)


    def smashegg_add(self,**kwargs):
        '''
        添加砸金蛋活动参数

    ===============     ===========    ============     ===================================
     字段                类型              默认               描述
    ===============     ===========    ============     ===================================
     name                string          随机
     template            int               4                  活动模板
     buy_limit           int
     start_time          timestamp      当前时间
     end_time            timestamp      第二天
     try_limit           int                5                  每日限制
     winning_limit       int                2                  中奖限制
    ===============     ===========    ============     ===================================

        '''
        start_time = int(time.time()) - 3600
        end_time = start_time + 3600*24
        name = "砸金蛋-" + self.Utils.rand_str()
        template = {
            "activity_name": name,
            "template": 4,
            "buy_limit":1,
            "start_time":start_time,
            "end_time": end_time,
            "is_subscribe": 2,
            "share_award": 2,
            "use_points": 2,
            "points_num": 0,
            "limit_type": 1,
            "try_limit": 5,
            "winning_limit": 2,
            "activity_desc": "砸金蛋活动规则说明...",
            "prize[0][level]": 0,
            "prize[0][type]": 1,
            "prize[0][name]": "谢谢参与！",
            "prize[0][type_id]": "",
            "prize[0][prize_pic]": "",
            "prize[0][documentLib][file_cdn_path]": "",
            "prize[0][num]": 0,
            "prize[0][probability]": 19,
            "prize[1][level]": 1,
            "prize[1][type]": 1,
            "prize[1][name]": "华为Mate9",
            "prize[1][prize_pic]": 91751,
            "prize[1][documentLib][file_cdn_path]": "http://imgcache.vikduo.com/static/463ad47a800772aa84aade7879749216.png",
            "prize[1][num]": 3,
            "prize[1][probability]": 1,
            "prize[2][level]": 2,
            "prize[2][type]": 5,
            "prize[2][name]": "测试红包",
            "prize[2][type_id]": 405,
            "prize[2][prize_pic]": 91753,
            "prize[2][documentLib][file_cdn_path]": "http://imgcache.vikduo.com/static/b5e7d2d43dbac650c358c1c2f77e1188.png",
            "prize[2][num]": 50,
            "prize[2][probability]": 30,
            "prize[3][level]": 3,
            "prize[3][type]": 3,
            "prize[3][name]": 10,
            "prize[3][prize_pic]": 91752,
            "prize[3][documentLib][file_cdn_path]": "http://imgcache.vikduo.com/static/8d665aa70eedd30e5ad62edcc7dc4979.png",
            "prize[3][num]": 100,
            "prize[3][probability]": 50,
            "is_collect": 2,
            "expiry_time": 1579756342,
            "share_type": 1,
            "startNews[title]": "一锤定音，开心砸金蛋~",
            "startNews[description]": "亲，点击进入活动主页，意外惊喜等着你！",
            "startNews[document_id]": 36791,
            "shareMessage[title]": "轻轻一锤，砸出精彩！",
            "shareMessage[desc]": "玩抽奖砸金蛋，千万奖品等你来，百分百赢中奖哟~",
            "shareMessage[pic_id]": 36790,
            "marketing_manage_id": 0
            }
        return g.get_params(template,kwargs)


    def togetherBuy_add(self,**kwargs):
        template = {"news":{"title":"成为团长带领小伙伴享受团购价！","description":"拼团活动开始啦，赶紧开团召集小伙伴一起团购吧！","document_id":187381}}
        return g.get_params(template,kwargs)
    

    def togetherBuy_goods_add(self,togetherBuyID, **kwargs):
        '''
        添加拼团商品参数

        ==============     ===========    ============     ===================================
         字段              类型              默认               描述
        ==============     ===========    ============     ===================================
        togetherBuyID      int                                团ID
         product_id        int            289888              产品ID
        ==============     ===========    ============     ===================================

        '''
        product_id = 289888
        template = {"together_buy_id":togetherBuyID,"product_id":289888,"product_sku_id":1171811,"buy_price":4900,"quota":"100","limit_buy":"2","together_num":"8"}
        return g.get_params(template,kwargs)


    def togetherBuy_edit(self,id,**kwargs):
        '''
        编辑拼团活动参数

        ==============     ===========    ============     ===================================
         字段              类型              示例               描述
        ==============     ===========    ============     ===================================
         name               随机
         id                 int            2873              活动ID
         start_time         timestamp     1484197822         开始时间
         end_time           timestamp     1578805824         结束时间
        ==============     ===========    ============     ===================================

        '''
        start_time = int(time.time())
        end_time = start_time + 3600*24
        name = "拼团活动-" + self.Utils.rand_str()
        template = {"activity":{"id":id,"name":name,"desc":"1. 活动时间：#年#月#日#时 至 #年#月#日#时；\n2. 团长：开团且该团第一位支付成功的人\n3. 参加成员：通过团长邀请购买该商品的成员即为参团成员，参团成员也可邀请更多的成员参团\n4. 退款说明：若拼团失败系统会将支付的金额返还至参团成员的支付账号中\n5. 拼团是基于好友的组团购买，获取团购优惠，为了保证广大消费者的权益，商家有权判定为黄牛倒货的团解散并取消订单","expire_type":1,"postage_setting_id":0,"start_time":start_time,"end_time":end_time,"share_type":1},"togetherBuy":{"id":815,"is_agree":2,"is_discount":2,"is_time_limit":2,"head_price":None,"time_limit":None,"is_open":2,"is_more":2,"is_auto_share":1,"auth_icons":[],"description":""},"shareMessage":{"title":"爱拼才会赢抱团才优惠","desc":"参与拼团召集小伙伴，一起静享团购优惠","pic_id":187380}}
        return g.get_params(template,kwargs)

    def second_kill_list(self,**kwargs):
        '''
        '''
        template = {"_page":1,"_page_size":15}
        return g.get_params(template, kwargs)



    def second_kill_add(self,**kwargs):
        '''
        添加秒杀活动参数

        =============     ===========    ============     ===================================
        字段              类型              默认               描述
        =============     ===========    ============     ===================================
         title               string          随机
        =============     ===========    ============     ===================================

        '''
        title = "只要一秒时间，顺手就捡个便宜!-" + self.Utils.rand_str()
        template = {"news":{"title":title,"description":"秒杀进行时，走过路过不容错过，随手一点，没准捡个大便宜呢~","document_id":1336962}}
        return g.get_params(template,kwargs)

    def second_kill_goods_add(self,act_id,**kwargs):
        '''
        添加秒杀活动商品参数

        =============     ===========    ============     ===================================
        字段              类型              默认               描述
        =============     ===========    ============     ===================================
         title               string          随机
        =============     ===========    ============     ===================================

        '''
        title = "只要一秒时间，顺手就捡个便宜!-" + self.Utils.rand_str()
        template = {"second_kill_id":act_id,"product_id":290014,"product_sku_id":1171972,"buy_price":4600,"quota":"800000","limit_buy":"500000"}
        return g.get_params(template,kwargs)


    def second_kill_edit(self,id,**kwargs):
        '''
        编辑秒杀活动参数

        =============     ===========    ============     ===================================
        字段              类型              示例               描述
        =============     ===========    ============     ===================================
         name
         id                 int            2873              活动ID
        start_time          timestamp     1484197822         开始时间
        end_time            timestamp     1578805824         结束时间
        =============     ===========    ============     ===================================

        '''
        start_time = int(time.time())
        end_time = start_time + 3600*24
        name = "秒杀活动-" + self.Utils.rand_str()
        template = {"activity":{"id":id,"name":name,"desc":"1. 活动时间：#年#月#日#时 至 #年#月#日#时；\n2. 当秒杀开始后，选择中意的商品，点击抢购按钮即可参与秒杀；\n3. 实物商品在秒杀结束后统一配送，请您耐心等待！\n4. 本活动最终解释权归XX商家所有。","expire_type":1,"postage_setting_id":0,"start_time":start_time,"end_time":end_time,"share_type":1},"secondKill":{"id":846},"shareMessage":{"title":"只要一秒时间，顺手就捡个便宜！","desc":"秒杀进行时，走过路过不容错过，随手一点，没准捡个大便宜呢~","pic_id":1336961}}
        return g.get_params(template,kwargs)



    def collect_zan_add(self,**kwargs):
        '''
        添加众筹活动参数
        =============     ===========    ============     ===================================
        字段              类型              默认               描述
        =============     ===========    ============     ===================================
         title               string          随机
        =============     ===========    ============     ===================================
        '''
        title = "顺手点个赞，有惊喜哦-" + self.Utils.rand_str()
        template={"news":{"title":title,"description": "亲，点击进入活动主页，意外惊喜等着你！","document_id": 6,}}
        return g.get_params(template,kwargs)





    def collect_zan_gift_add(self,collectId,**kwargs):
        '''
        添加众筹活动商品参数
        =============     ===========    ============     ===================================
        字段              类型              默认               描述
        =============     ===========    ============     ===================================
        collect_id        int              864            众筹商品ID
        =============     ===========    ============     ===================================
        '''

        template={"collect_id":collectId,"name":"小熊饼干","number":200,"count":100,"price":200,"lastCount":100,"document_id":1337027}
        return g.get_params(template,kwargs)


    def collect_zan_edit(self,collectId,**kwargs):
        '''
        编辑众筹活动参数
        =============     ===========    ============     ===================================
        字段              类型              示例               描述
        =============     ===========    ============     ===================================
         name
         id                 int            861               活动ID
        start_time          timestamp     1486713833        开始时间
        end_time            timestamp     1490774633         结束时间
        =============     ===========    ============     ===================================

        '''
        name = "点赞活动-" + self.Utils.rand_str()
        template={
            "collect[id]":collectId,
            "collect[name]":name,
            "collect[rule]":"众筹活动规则说明:由用户自主发起，利用微信分享好友参与活动，在指定时间内由好友帮忙点赞到指定集点数，发起人即可免费得到商品。1.活动时间：××××年××月××日-××××年××月××日；2.活动参与人必须关注活动商家微信公众号才能参与活动；（打开强制关注后）3.用户必须填写用户信息后才能参加活动；（打开“填写用户信息规则”后）4.在指定的时间内，集齐完点数，即可获得活动商品；5.若发起人成功集齐赞数，则可免费获得活动商品，工作人员将会在15个工作日与发起人联系；6. 若发起人成功集齐赞数，请尽快填写中奖资料；7. 若发起人在指定结束时间内没有集齐完点数，则此次活动失败；8.活动商品领完即止，先到先得。",
            "collect[is_attention]":2,
            "collect[start_time]":1486713833,
            "collect[end_time]":1490774633,
            "collect[share_type]":1,
            "collect[is_collect]":2,
            "collect[collection_info_setting]":"",
            "shareMessage[title]":"谁是点赞狂魔，一点就知道！",
            "shareMessage[desc]":"让好友来点赞，集够赞数免费获得指定大奖~",
            "shareMessage[pic_id]":11,
        }
        return g.get_params(template,kwargs)



    def slyder_add(self,**kwargs):
        '''
        添加大转盘活动参数
        ===============     ===========    ============     ===================================
        字段                类型              默认               描述
        ===============     ===========    ============     ===================================
         name               string          随机
        template            int              1                  活动模板
        buy_limit           int
        start_time          timestamp      当前时间
        end_time            timestamp      第二天
        try_limit           int                3                  每日限制
        winning_limit       int                1                  中奖限制
        ===============     ===========    ============     ===================================
        '''
        start_time = int(time.time()) - 3600
        end_time = start_time + 3600*24
        name = "大转盘-" + self.Utils.rand_str()
        template = {
            "activity_name":name,
            "template":1,
            "buy_limit":1,
            "start_time":start_time,
            "end_time":end_time,
            "is_subscribe":2,
            "share_award":2,
            "use_points":2,
            "points_num":0,
            "limit_type":2,
            "try_limit":3,
            "winning_limit"  :1,
            "activity_desc":"大转盘活动规则说明：1.活动时间：××××年××月××日-××××年××月××日；2. 抽奖对象：所有用户；3. 活动参与人必须关注活动商家微信公众号才能参与活动；（打开强制关注后）4.用户必须填写用户信息后才能参加活动；（打开“填写用户信息规则”后）5. #积分可以兑换一次抽奖机会，限制#次；6. 中奖限制：每人限中奖一次；7. 本活动最终解释权归XX商家所有。",
            "prize[0][level]":0,
            "prize[0][type]":1,
            "prize[0][name]":"谢谢参与！",
            "prize[0][type_id]":"",
            "prize[0][prize_pic]":"",
            "prize[0][documentLib][file_cdn_path]":"",
            "prize[0][num]":0,
            "prize[0][probability]":20,
            "prize[0][$$hashKey]":"object:54",
            "prize[1][level]":1,
            "prize[1][type]":1,
            "prize[1][name]":"特步运动鞋",
            "prize[1][type_id]":"",
            "prize[1][prize_pic]":1337015,
            "prize[1][documentLib][file_cdn_path]":"https://imgcache.vikduo.com/static/16d028d90965a5445efe454e3256a3d3.jpg",
            "prize[1][num]":3,
            "prize[1][probability]":10,
            "prize[1][$$hashKey]":"object:55",
            "prize[1][invalidInfo]":"",
            "prize[2][level]":2,
            "prize[2][type]":5,
            "prize[2][name]":"测试红包",
            "prize[2][type_id]":405,
            "prize[2][prize_pic]":91753,
            "prize[2][documentLib][file_cdn_path]":"http://imgcache.vikduo.com/static/b5e7d2d43dbac650c358c1c2f77e1188.png",
            "prize[2][num]":10,
            "prize[2][probability]":20,
            "prize[2][$$hashKey]":"object:56",
            "prize[2][invalidInfo]":"",
            "prize[3][level]":3,
            "prize[3][type]":3,
            "prize[3][name]":10,
            "prize[3][type_id]":"",
            "prize[3][prize_pic]":91752,
            "prize[3][documentLib][file_cdn_path]":"http://imgcache.vikduo.com/static/8d665aa70eedd30e5ad62edcc7dc4979.png",
            "prize[3][num]":100,
            "prize[3][probability]":50,
            "prize[3][$$hashKey]":"object:57",
            "prize[3][invalidInfo]":"",
            "is_collect":2,
            "collection_info_setting":"",
            "expiry_time":1488266975,
            "share_type": 1,
            "startNews[title]":"极速大转盘，幸运转转转~",
            "startNews[description]":"亲，点击进入活动主页，意外惊喜等着你！",
            "startNews[document_id]":3,
            "shareMessage[title]":"玩大转盘，轻轻一转好礼不断！",
            "shareMessage[desc]":"玩抽奖大转盘，千万奖品等你来，百分百赢中奖哟~",
            "shareMessage[pic_id]":9,
            "marketing_manage_id":0,
        }
        return g.get_params(template,kwargs)


    def memory_fan_add(self,**kwargs):
        '''
        添加记忆翻翻看活动参数
        ===============     ===========    ============     ===================================
        字段                类型              默认               描述
        ===============     ===========    ============     ===================================
         name               string          随机
        start_time          timestamp      当前时间
        end_time            timestamp      第二天
        ===============     ===========    ============     ===================================
        '''
        start_time = int(time.time()) - 3600
        end_time = start_time + 3600*24
        name = u"记忆翻翻看-" + self.Utils.rand_str()
        template = {
       "card1":"http://imgcache.vikduo.com/static/2ec7e6f594e33b5220eef7e37fc1081a.png",
        "card2":"http://imgcache.vikduo.com/static/2517f29b4d61bf0ff86182fa69beb484.png",
        "card3":"http://imgcache.vikduo.com/static/c7aa25062d57c4a54cb10f7de5b681c9.png",
        "card4":"http://imgcache.vikduo.com/static/61555aa92be0059ca0d17d1ae84c66e1.png",
        "card5":"http://imgcache.vikduo.com/static/4cc7a38280ce766cbb9fa0e4773b4eeb.png",
        "card6":"http://imgcache.vikduo.com/static/8fc50cd82eac4d85a7214f8efb50958f.png",
        "start_time":start_time,
        "end_time":end_time,
        "open_time":5,
        "game_time":30,
        "level":2,
        "min_score":1000,
        "prize_url":"",
        "reward_type":2,
        "share_type":1,
        "marketingActivity[activity_name]":name,
        "marketingActivity[buy_limit]":1,
        "marketingActivity[expiry_time]":1487574273,
        "marketingActivity[activity_desc]":"翻翻看规则说明:1.活动时间：××××年××月××日-××××年××月××日；2.活动对象：所有用户/购买过商品的用户；3.用户必须关注微信公众号才能参与活动；（打开“强制关注”后） 4.用户必须填写用户信息后才能参加活动；（打开“填写用户信息规则”后） 5.游戏开始后会有一段明牌时间,明牌时间结束后进入限时翻牌，如果连续两次翻开的卡片一样则会消除这组图片，6组图片消除完后如果游戏时间还未结束将会继续进行下一轮游戏6.在规定时间内对消除的牌数进行计分7.消除一对牌计100分，每消除一轮牌额外奖励500分，系统会根据分数计算最佳成绩与排名8.本活动最终解释权归XX商家所有。",
        "marketingActivity[is_subscribe]":2,
        "marketingActivity[sorry_word]":"大奖在前面等着你！",
        "marketingActivity[winning_limit]":1,
        "marketingActivity[logo_img]":"https://imgcache.vikduo.com/static/1f161b63d2133982f83cc5e28d036736.jpg",
        "marketingActivity[is_collect]":2,
        "marketingActivity[collection_info_setting]":"",
        "marketingActivity[startNews][title]":"看看你的记忆有几秒",
        "marketingActivity[startNews][description]":"据说鱼的记忆只有7秒，你会有几秒的记忆呢？",
        "marketingActivity[startNews][content]":"据说鱼的记忆只有7秒，你会有几秒的记忆呢？",
        "marketingActivity[startNews][document_id]":1054439,
        "marketingActivity[shareMessage][title]":"看看你的记忆有几秒",
        "marketingActivity[shareMessage][desc]":"据说鱼的记忆只有7秒，你会有几秒的记忆呢？要不你试试？",
        "marketingActivity[shareMessage][pic_id]":1054438,
        "marketingActivity[prize][0][level]":0,
        "marketingActivity[prize][0][type]":1,
        "marketingActivity[prize][0][name]":"大奖在前面等着你！",
        "marketingActivity[prize][0][type_id]":"",
        "marketingActivity[prize][0][prize_pic]":"",
        "marketingActivity[prize][0][documentLib][file_cdn_path]":"",
        "marketingActivity[prize][0][num]":0,
        "marketingActivity[prize][0][probability]":34,
        "marketingActivity[prize][1][level]":1,
        "marketingActivity[prize][1][type]":1,
        "marketingActivity[prize][1][name]":"华为p9",
        "marketingActivity[prize][1][type_id]":"",
        "marketingActivity[prize][1][prize_pic]":1337025,
        "marketingActivity[prize][1][documentLib][file_cdn_path]":"https://imgcache.vikduo.com/static/1f161b63d2133982f83cc5e28d036736.jpg",
        "marketingActivity[prize][1][num]":1,
        "marketingActivity[prize][1][probability]":1,
        "marketingActivity[prize][1][invalidInfo]":"",
        "marketingActivity[prize][2][level]":2,
        "marketingActivity[prize][2][type]":5,
        "marketingActivity[prize][2][name]":"测试红包",
        "marketingActivity[prize][2][type_id]":405,
        "marketingActivity[prize][2][prize_pic]":91753,
        "marketingActivity[prize][2][documentLib][file_cdn_path]":"http://imgcache.vikduo.com/static/b5e7d2d43dbac650c358c1c2f77e1188.png",
        "marketingActivity[prize][2][num]":100,
        "marketingActivity[prize][2][probability]":5,
        "marketingActivity[prize][2][invalidInfo]":"",
        "marketingActivity[prize][3][level]":3,
        "marketingActivity[prize][3][type]":2,
        "marketingActivity[prize][3][name]":"测试卡yrbup",
        "marketingActivity[prize][3][type_id]":1029,
        "marketingActivity[prize][3][prize_pic]":91750,
        "marketingActivity[prize][3][documentLib][file_cdn_path]":"http://imgcache.vikduo.com/static/105807a761f0383a34502b0f5776b9ad.png",
        "marketingActivity[prize][3][num]":200,
        "marketingActivity[prize][3][probability]":60,
        "marketingActivity[prize][3][invalidInfo]":"",
        }
        return g.get_params(template,kwargs)


    def reserve_add(self,**kwargs):
        '''
        预约活动API测试
    =============     ===========    ============     ===================================
     字段              类型              默认               描述
    =============     ===========    ============     ===================================
     name               string          随机
     start_time         timestamp     当前时间          开始时间
     end_time           timestamp     明天              到期时间
    =============     ===========    ============     ===================================
        '''
        start_time = int(time.time()) - 3600
        end_time = start_time + 3600*24
        name = u"预约活动-" + self.Utils.rand_str()
        template = {
        "reserveSetting[title]":name,
        "reserveSetting[summary]":"活动简介",
        "reserveSetting[note]":"报名须知",
        "reserveSetting[items][0][nametag]":"name",
        "reserveSetting[items][0][type]":"text",
        "reserveSetting[items][0][key]":"姓名",
        "reserveSetting[items][0][value]":"请输入您的名字",
        "reserveSetting[items][0][check]":"false",
        "reserveSetting[items][0][addtype]":"system",
        "reserveSetting[items][0][$$hashKey]":"object:35",
        "reserveSetting[items][1][nametag]":"sex",
        "reserveSetting[items][1][type]":"select",
        "reserveSetting[items][1][key]":"性别",
        "reserveSetting[items][1][value]":"男|女",
        "reserveSetting[items][1][check]":"false",
        "reserveSetting[items][1][addtype]":"system",
        "reserveSetting[items][1][$$hashKey]":"object:36",
        "reserveSetting[items][2][nametag]":"mobile",
        "reserveSetting[items][2][type]":"text",
        "reserveSetting[items][2][key]":"手机",
        "reserveSetting[items][2][value]":"请输入您的手机",
        "reserveSetting[items][2][check]":"false",
        "reserveSetting[items][2][addtype]":"system",
        "reserveSetting[items][2][$$hashKey]":"object:37",
        "reserveSetting[items][3][nametag]":"idCard",
        "reserveSetting[items][3][type]":"text",
        "reserveSetting[items][3][key]":"身份证",
        "reserveSetting[items][3][value]":"请输入您的身份证号码",
        "reserveSetting[items][3][check]":"false",
        "reserveSetting[items][3][addtype]":"system",
        "reserveSetting[items][3][$$hashKey]":"object:38",
        "reserveSetting[items][4][nametag]":"bookedDate",
        "reserveSetting[items][4][type]":"calendar",
        "reserveSetting[items][4][key]":"预约日期",
        "reserveSetting[items][4][value]":"点击输入",
        "reserveSetting[items][4][check]":"false",
        "reserveSetting[items][4][addtype]":"system",
        "reserveSetting[items][4][$$hashKey]":"object:39",
        "reserveSetting[items][5][nametag]":"bookedTime",
        "reserveSetting[items][5][type]":"select",
        "reserveSetting[items][5][key]":"预约时间",
        "reserveSetting[items][5][value]":"0:00-1:00|1:00-2:00|2:00-3:00|3:00-4:00|4:00-5:00|5:00-6:00|6:00-7:00|7:00-8:00|8:00-9:00|9:00-10:00|10:00-11:00|11:00-12:00|12:00-13:00|13:00-14:00|14:00-15:00|15:00-16:00|16:00-17:00|17:00-18:00|18:00-19:00|19:00-20:00|20:00-21:00|21:00-22:00|22:00-23:00|23:00-24:00",
        "reserveSetting[items][5][check]":"false",
        "reserveSetting[items][5][addtype]":"system",
        "reserveSetting[items][5][$$hashKey]":"object:40",
       "reserveSetting[items][6][nametag]":"message",
        "reserveSetting[items][6][type]":"textarea",
        "reserveSetting[items][6][key]":"留言",
        "reserveSetting[items][6][value]":"请输入您的留言内容",
        "reserveSetting[items][6][check]":"false",
        "reserveSetting[items][6][addtype]":"system",
        "reserveSetting[items][6][$$hashKey]":"object:41",
        "reserveSetting[items][7][nametag]":"fShop",
        "reserveSetting[items][7][type]":"select",
        "reserveSetting[items][7][key]":"预约店铺",
        "reserveSetting[items][7][value]":"分店测试0207|YT测试分店2|YT测试分店",
        "reserveSetting[items][7][check]":"false",
        "reserveSetting[items][7][addtype]":"system",
        "reserveSetting[items][7][$$hashKey]":"object:42",
        "reserveSetting[start_time]":start_time,
        "reserveSetting[end_time]":end_time,
        "reserveSetting[document_id]":250,
        "reserveSetting[per_count]":200,
        "reserveSetting[share_type]":1,
        "news[title]":"各就各位，预约正式开始~",
        "news[description]":"亲，点击进入活动主页，意外惊喜等着你！",
        "news[document_id]":2,
        }

        return g.get_params(template,kwargs)



    def signin_setting_add(self,**kwargs):
        '''
        签到活动API测试
    =============     ===========    ============     ===================================
     字段              类型              默认               描述
    =============     ===========    ============     ===================================
     name               string          随机
     start_time         timestamp     当前时间          开始时间
     end_time           timestamp     明天              到期时间
    =============     ===========    ============     ===================================

        '''
        start_time = int(time.time()) - 3600
        end_time = start_time + 3600*24
        name = u"签到活动-" + self.Utils.rand_str()
        template = {
        "end_time": end_time,
        "name": name,
        "start_time": start_time,
        }
        return  g.get_params(template,kwargs)


    def giftpack_add(self,**kwargs):
        '''
        节日礼包API测试
    =============     ===========    ============     ===================================
     字段              类型              默认               描述
     =============     ===========    ============     ===================================
     name               string          随机
     start_time         timestamp     当前时间          开始时间
     end_time           timestamp     明天              到期时间
     =============     ===========    ============     ===================================
        '''
        start_time = int(time.time()) - 3600
        end_time = start_time + 3600*24
        name = u"节日礼包-" + self.Utils.rand_str()
        template={"start_time":start_time,"end_time":end_time,"gift_num":3,"gift_pack_desc":"活动说明。。。","name":name,"shop_sub_range":[],"num_limit":1,"user_type":1,"show_page":[1,2,3],"shop_sub_show_page":None,"show_mode":1,"user_type_limit":"","quota":"100","gift":[{"gift_type":1,"name":"测试卡dxelp","gift_id":991,"gift_pic":"http://imgcache.vikduo.com/static/105807a761f0383a34502b0f5776b9ad.png","num":0,"invalidInfo":"","wx_card_type":2},{"gift_type":1,"name":"测试卡cxjuz","gift_id":989,"gift_pic":"http://imgcache.vikduo.com/static/105807a761f0383a34502b0f5776b9ad.png","num":0,"invalidInfo":"","wx_card_type":2},{"gift_type":1,"name":"测试卡券4","gift_id":976,"gift_pic":"http://imgcache.vikduo.com/static/105807a761f0383a34502b0f5776b9ad.png","num":0,"invalidInfo":"","wx_card_type":2}]}

        return  g.get_params(template,kwargs)



    def cardpack_add(self,**kwargs):
        '''
        购物礼包API测试
     =============     ===========    ============     ===================================
     字段              类型              默认               描述
     =============     ===========    ============     ===================================
     name               string          随机
     start_time         timestamp     当前时间          开始时间
     end_time           timestamp     明天              到期时间
     =============     ===========    ============     ===================================
        '''
        start_time = int(time.time()) - 3600
        end_time = start_time + 3600*24
        name = u"购物礼包-" + self.Utils.rand_str()
        template={"start_time":start_time,"end_time":end_time,"desc":"活动说明。。","name":name,"shop_sub_range":[],"product_type":"2","num_per_order":"100","quota":"200","send_type":1,"buy_limit":1,"normal_flag":1,"scan_flag":1,"receive_type":1,"message":[{"id":1,"message":"有券了，才敢去商城购物啊~","type":1},{"id":2,"message":"哇塞，又有券可以使用了~","type":1},{"id":3,"message":"超优惠的卡券包,领券领到手软呀~","type":1},{"id":4,"message":"购物还送券,优惠翻几倍哦","type":1},{"id":5,"message":"购物有优惠,支付送卡券,大家快来买","type":1},{"id":6,"message":"大家好朋友，有券当然要分享","type":1}],"cards":[{"card_type_info_id":1024,"quota":1}],"products":[1171811],"shareMessage":{"title":"超优惠的购物礼包限量送，再不领就送完了","desc":"超优惠购物大礼包，分享还能送好友，限时领取，先到先得!","pic_id":1240003,"imgsrc":"http://imgcache.vikduo.com/static/f7be799e7d944ea03f589f0bd080a087.png"}}
        return g.get_params(template,kwargs)






        






