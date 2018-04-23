import ml
import tensorflow as tf
import numpy as np
import random



train_data, train_target = ml.load_train_data()
l = len(train_target)
target = np.zeros((l, 13))
for i in range(target.shape[0]):
    target[i,train_target[i]] = 1


sess = tf.InteractiveSession()



def get_batch(size=256):
    index = random.sample(range(l), size)
    return train_data[index], target[index]


def weight_varible(shape,name):
    initial = tf.truncated_normal(shape, stddev=0.01)
    return tf.Variable(initial, name=name) * 0.01


def bias_varible(shape, name):
    initial = tf.constant(0.1, shape = shape)
    return tf.Variable(initial, name=name)


def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1,1,1,1], padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

x = tf.placeholder(tf.float32, [None, 240*120], name='x')
y_ = tf.placeholder(tf.float32, [None, 13], name='y_')
x_image = tf.reshape(x, [-1, 240, 120, 1])

W_conv1 = weight_varible([5,5,1,32],name='W_conv1')
b_conv1 = bias_varible([32], name='b_conv1')
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

W_conv2 = weight_varible([5,5,32,64], name='W_conv2')
b_conv2 = bias_varible([64], name='b_conv2')
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

W_fc1 = weight_varible([60*30*64,1024], name='W_fc1')
b_fc1 = bias_varible([1024], name='b_fc1')
h_pool2_flat = tf.reshape(h_pool2, [-1, 60*30*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

keep_prob = tf.placeholder(tf.float32, name='keep_prob')
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

W_fc2 = weight_varible([1024, 13], name='W_fc2')
b_fc2 = bias_varible([13],name='b_fc2')
y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2, name='y_conv')

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y_conv), reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

saver = tf.train.Saver()

tf.global_variables_initializer().run()
for i in range(20):
    if i % 5 == 0:
        _x,_y = get_batch()
        train_accuracy = accuracy.eval(feed_dict={x:_x, y_:_y, keep_prob:1.0})
        print("step %d, training accuracy %g" %(i, train_accuracy))
        print(sess.run(W_conv1))
    _x, _y = get_batch()
    train_step.run(feed_dict={x:_x, y_:_y, keep_prob:0.75})

saver.save(sess, './data.chkp')