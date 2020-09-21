driving = input('你有沒有開過車呢?')
if driving != '有' and  driving != '沒有':
	print('只能回答 有/沒有')
	raise SystemExit
age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age > 18:
		print('通過測驗')
	else:
		print('不可以無照駕駛!')
elif driving == '沒有':
	if age >= 18:
		print('可以考駕照啦!快去吧!')
	else:
		print('再等等就能考駕照了')