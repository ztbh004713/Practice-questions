country = input("请输入您是哪个国家： ")
age = input("请输入您的年龄为： ")
age = int(age)
if country == "TW":
	if age >= 18:
		print("您可以考取驾照。")
	else:
		print("您目前无法考取驾照。")
elif country == "USA":
	if age >= 16:
		print("您可以考取驾照。")
	else:
		print("您目前无法考取驾照。")
elif country == "HK":
	if age >= 20:
		print("可以考照喔")
	else:
		print("不能考照喔")
else:
	print("不再记录中")