import tensorflow as tf
import numpy as np
import  pandas as pd
pd.read_csv()
pd.DataFrame
tf.Variable
tf.nn.softmax
# 1.定义一个常量c1，值为小数3.3（8分）
c1=tf.constant(3.3,dtype=tf.float32,name='c1')
# 2.定义一个变量a，值为整数10（8分）
a=tf.Variable(10,dtype=tf.float32,name='a')
# 3.定义另一个变量b，值为5.6（8分）
b=tf.Variable(5.6,dtype=tf.float32,name='b')
# 4.定义变量a与常量c1的和的操作（8分）
a_c1=a+c1
# 5.定义两个变量a和b的和的操作（8分）
a_b_add=a+b
# 6.定义两个变量a和b的差的操作（8分）
a_b=a-b
# 7.创建Session对象（8分）
sess=tf.Session()
# 8.执行全局变量初始化（8分）
sess.run(tf.global_variables_initializer())
# 9.输出变量a的值（6分）
print(sess.run(a))
# 10.输出变量b的值（6分）
print(sess.run(b))
# 11.输出变量a与常量c1的和的值（8分）
print(sess.run(a_c1))
# 12.输出两个变量a和b的和的值（8分）
print(sess.run(a_b))
# 13.输出两个变量a和b的差的值（8分）
print(sess.run(a_b_add))