# ### 需求分析

card 卡类
卡号    密码      余额    锁定状态
cardid  password   money   islock


person 用户类
姓名   身份证号  手机号   卡对象
name   userid     phone    card

view   视图类
登录 打印欢迎界面 打印操作界面

operation 操作类
完成10个功能

main 类,统一调用分模块的功能;
开户(1)   register 
查询(2)   query          
存钱(3)   save_money
取钱(4)   get_money
转账(5)   trans_money
改密(6)   change_pwd
锁卡(7)   lock
解卡(8)   unlock       
补卡(9)   new_card
退出(0)   save


请输入管理员的账户:admin
请输入管理员密码111
*******************************************
*                                         *
*                                         *
*         Welcome To OldBoy Bank          *
*                                         *
*                                         *
*******************************************
*******************************************
*           开户(1)    查询(2)             *
*           存钱(3)    取钱(4)             *
*           转账(5)    改密(6)             *
*           锁卡(7)    解卡(8)             *
*           补卡(9)    退出(0)             *
*******************************************
请选择需要办理的业务


用户和卡以什么形式存储在文件中 pickle
# json不能存储对象
user.txt   => {卡号:用户对象} {"555666": 用户对象}    =>  user_dict
 通过卡号 -> 用户对象 -->卡对象-->卡的各个属性

userid.txt => {身份证号:卡号}   {"111": "555666" , "222":"777888"} => user_id_dict
通过身份证号 ->卡号--> 用户对象 -->卡对象-->卡的各个属性
通过身份证号 -> 用户对象 -->卡对象-->卡的各个属性














