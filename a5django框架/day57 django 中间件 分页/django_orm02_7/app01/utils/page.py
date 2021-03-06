#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author: wangtongpei
#@time:  2020/12/6 21:13

from django.utils.safestring import mark_safe
# 标识字符串是安全的,可以直接展示成标签,前端页面不需要用safe过滤器

class Pagenation():
	def __init__(self,current_page,total_count):
		# 参数1是当前是第几页
		# 参数2是总记录数
		self.per_page_num = 3  # 每页展示3条数据
		self.current_page = current_page

		total_page_number,b = divmod(total_count,self.per_page_num)
		# 总页码数量
		if b:
			total_page_number += 1

		show_page_number = 11 # 总共展示11个页码

		half_page_number = show_page_number // 2  #地板除
		if current_page <= half_page_number:
			page_number_start = 1
			page_number_end = show_page_number + 1
			# 左闭右开
		elif (current_page + half_page_number) > total_page_number:
			page_number_start = total_page_number - show_page_number + 1
			page_number_end = total_page_number + 1
		else:
			page_number_start = current_page - half_page_number
		#当前页是11  起始页是6
			page_number_end = current_page + half_page_number + 1
			#结束页是16

		self.page_num_range = range(page_number_start,page_number_end)
	#   range(6,16)

	@property   #方法转属性
	def page_data_start(self):
		return (self.current_page - 1) * self.per_page_num
	# 第一页的第一条记录

	@property
	def end_data_start(self):
		return self.current_page * self.per_page_num
	# 第一页的最后一条记录

	def page_html(self):
		page_html_start = '''
		<nav aria-label="Page navigation">
		  <ul class="pagination">
		    <li>
		      <a href="#" aria-label="Previous">
		        <span aria-hidden="true">&laquo;</span>
		      </a>
		    </li>		
		'''

		for i in self.page_num_range:
			s = f'<li><a href="?page={i}">{i}</a></li>'
			page_html_start += s

		page_html_end = '''
		    <li>
		      <a href="#" aria-label="Next">
		        <span aria-hidden="true">&raquo;</span>
		      </a>
		    </li>
		  </ul>
		</nav>		
		'''
		page_all_html = page_html_start + page_html_end
		return mark_safe(page_all_html)


# <nav aria-label="Page navigation">
#   <ul class="pagination">
#     <li>
#       <a href="#" aria-label="Previous">
#         <span aria-hidden="true">&laquo;</span>
#       </a>
#     </li>

#     <li><a href="#">1</a></li>
#     <li><a href="#">2</a></li>
#     <li><a href="#">3</a></li>
#     <li><a href="#">4</a></li>
#     <li><a href="#">5</a></li>

#     <li>
#       <a href="#" aria-label="Next">
#         <span aria-hidden="true">&raquo;</span>
#       </a>
#     </li>
#   </ul>
# </nav>






































