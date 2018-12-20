class point:
	def __init__(self,d):
		self.d = d
	'''
	magnitude功能擴充，可以對多維多個群中心進行距離的比較後
	輸出最短距離
	'''
	def magnitude(self):
		p=0
		dis_lst=[]
		for i in range(len(center_lst)):	
			p = 0
			for num in range(m):
				p += (p_dict[self.d][num] -p_dict[center_lst[i]][num])**2
				ans = p**0.5
			dis_lst.append(ans)
		
		min_dis =999999
		for dis in dis_lst:
			if dis <= min_dis:
				min_dis = dis
		return min_dis


#輸入
n_m_k_j = input().split(',')
n,m,k,j = int(n_m_k_j[0]),int(n_m_k_j[1]),int(n_m_k_j[2]),int(n_m_k_j[3])
p_lst=[]
for i in range(n): 
	p_data = [float(j) for j in input().split(',')]
	p_lst.append(p_data)
#將輸入轉變成包含點位置資訊的dict
p_dict = dict()
center_lst=[]									#建立群中心list作為存放答案處	
center_unuse_lst=[]
for i in range(n):
	p_num =int('%d'%(i+1))
	center_unuse_lst.append(i+1)
	if p_num not in p_dict.keys():
		p_dict[p_num] = []
	for h in range(m):
		p_dict[p_num].append(p_lst[i][h])
center_unuse_lst.reverse()						#建立由大到小還沒做為群中的list，以符合距離一樣時以編號小者為群中心的要求



#演算法
for center in range(k-1):
	max = 0	
	new_center = 0
	if j in center_unuse_lst:     			 	#建立題目給定的群中心編號，加入center list，並從center unuse list刪除
		center_unuse_lst.remove(j)
		center_lst.append(j)
		
	for i in center_unuse_lst:					#貪婪演算法的機制，最後把距離最遠的點作為新的群中心，加入center list
		p 	= point(i)
		mag = p.magnitude()
		if mag >= max:
			max 		= mag
			new_center 	= i		
	center_lst.append(new_center)
	center_unuse_lst.remove(new_center)
	j = new_center

#輸出
output_lst=[]
for i in center_lst:	
	output_lst.append(str(i))
print(','.join(output_lst))	