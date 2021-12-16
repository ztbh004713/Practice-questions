country = input("请输入您是哪个国家： ")
age = input("请输入您的年龄为： ")
age = int(age)
if country == "TW":
	if age >= 18:
		print("您可以考取驾照。")
	else:
		print("您目前无法考取驾照。")