#两种形态的回圈：for loop、while loop
#回圈的功用：能够让程式 『重复』 的执行
x = 5
while x < 10:         #while可以解释为『当』：当x小于十的时候，就会持续『重复』下方程式码的字串
	print("x小于10")  
	print("回圈开始")
	x = 10             #再进入下方程式码执行时，有设置条件，再结果为False时程式

#    while x < 10:    当 x < 10 为True时就会执行后续撰写的程式码
#    print("x小于10")  再下方程式码执行完后，会在回到while x < 10:又在得到True的结果，就会再次执行
#    print("回圈开始")

x = 3
while x < 10:         
	print("x小于10")  
	print("回圈开始")
	x ＝ x + 1          