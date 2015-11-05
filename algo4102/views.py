from django.shortcuts import render
from .models import Board

blank_board = [[ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

blank_sure_board = [[ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
               [ True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, True , True , True , True , True , True ],
               [ True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, True , True , True , True , True , True ],
               [ True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, True , True , True , True , True , True ],
               [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False],
               [ False, False, False, False, False, False, False, False, False, True , True , True , False, False, False, False, False, False, False, False, False]]

xnotiles1 = (9,10,11)
ynotiles1 = (0,1,2,3,4,5,15,16,17,18,19,20)
xnotiles2 = ynotiles1
ynotiles2 = xnotiles1

TOP_LEFT = 0
TOP_RIGHT = 1
MIDDLE = 2
BOT_LEFT = 3
BOT_RIGHT = 4
NONE = -1

def index(request):
	context = {('lengthRange',xrange(21)),('widthRange',xrange(21)),('xnotiles1',xnotiles1),('ynotiles1',ynotiles1),('xnotiles2',xnotiles2),('ynotiles2',ynotiles2)}
	return render(request, 'test_index.html',context)

def solve(request):
	if request.method != "POST":
		return "You shouldn't be here yet"
	given = blank_board
	sure = blank_sure_board
	answer = [[(x%10) for x in range(21)] for x in range(21)]


	for i in request.POST:
		if not i[0]=='c':
			rc = i.split('-')
			r = int(rc[0])
			c = int(rc[1])
			if (request.POST[i]):
				given[r][c]=int(request.POST[i])
				sure[r][c]=True
			else:
				given[r][c]=0


	# preliminary implementation

	endval=9
	nr=0
	nc=0

	prog = True
	f = open('test.txt', 'w')
	f.truncate()
	while nr < endval and nc < endval:
		val = given[nr][nc]
		print str(nr) + ", " + str(nc)
		f.write(str_2d_array(given))
		if sure[nr][nc]:
			if prog:
				#PROGRESS
				tog = progress(nr,nc)
				nr = tog[0]
				nc = tog[1]
			else:
				# REGRESS
				tog = regress(nr,nc)
				nr = tog[0]
				nc = tog[1]
		else:
			something_found = False
			for i in range(val+1,10):
				if valid_move(given,nr,nc,i):
					prog = True
					given[nr][nc]=i
					something_found=True
					break
			if something_found:
				#PROGRESS
				tog = progress(nr,nc)
				nr = tog[0]
				nc = tog[1]
			else:
				prog = False
				given[nr][nc]=0
				#REGRESS
				tog = regress(nr,nc)
				nr = tog[0]
				nc = tog[1]

	#print_2d_array(given)
	#please do not modiy below here in this method either
	#everything is held together by spit and prayers

	ansstr = two_d_list_to_string(given)
	context = {('ansstr',ansstr),('lengthRange',xrange(21)),('widthRange',xrange(21)),('xnotiles1',xnotiles1),('ynotiles1',ynotiles1),('xnotiles2',xnotiles2),('ynotiles2',ynotiles2)}
	return render(request, 'solved.html',context)

def progress(nr,nc):
	nr=nr+(nc+1)//9
	nc=(nc+1)%9
	return (nr,nc)
def regress(nr,nc):
	if (nc == 0):
		nr = nr - 1
		nc = 8
	else:
		nc = nc - 1
	return(nr,nc)


def print_2d_array(board):
	for r in board:
		for c in r:
			print c,
		print " "

def str_2d_array(board):
	ret = ""
	for r in board:
		for c in r:
			if len(str(c)) == 1:
				ret = ret + str(c) + " "
			else:
				ret = ret + str(c)
		ret = ret + "\n"
	ret = ret +"\n\n\n\n\n"
	return ret

def two_d_list_to_string(list):
	ansstr = "test"
	for row in list:
		for col in row:
			if col >= 0:
				ansstr = ansstr + str(col)
			elif col == 0:
				ansstr = ansstr + "z"
			else:
				ansstr = ansstr + "x"
	return ansstr

def is_valid(r,c):
	return not (c in xnotiles1 and r in ynotiles1 or c in xnotiles2 and r in ynotiles2)

def valid_move(board,r,c,val):
	bi_s = determine_boards_or_invalid(r,c)
	final_validity = val <= 9 and val >=1
	if -1 in bi_s:
		return False
	for bi in bi_s:
		b = get_board(board, bi)
		newr = convert_r_for_board(bi,r)
		newc = convert_c_for_board(bi,c)
		final_validity = final_validity and reg_val(b,newr,newc,val)
	return final_validity

def convert_r_for_board(board_index,r):
	r_offset = {
		TOP_LEFT:0,
		TOP_RIGHT:0,
		MIDDLE:6,
		BOT_LEFT:12,
		BOT_RIGHT:12,
	}
	return r-r_offset.get(board_index,0)

def convert_c_for_board(board_index,c):
	c_offset = {
		TOP_LEFT:0,
		TOP_RIGHT:12,
		MIDDLE:6,
		BOT_LEFT:0,
		BOT_RIGHT:12,
	}
	return c - c_offset.get(board_index,0)

def reg_val(board,r,c,val):
	# print "r:" + str(r) + ",c:" + str(c) + ",val:" + str(val),
	# print "reg_col_val:" + str(reg_col_val(board,c,val)),
	# print "reg_row_val:" + str(reg_row_val(board,r,val)),
	# print "reg_blk_val:" + str(reg_blk_val(board,r,c,val))
	return reg_row_val(board,r,val) and reg_col_val(board,c,val) and reg_blk_val(board,r,c,val)

# return true if move is valid
def reg_row_val(board,r,val):
	return val not in board[r]

# return true if move is valid
def reg_col_val(board,c,val):
	for r in range(9):
		if board[r][c]==val:
			return False;
	return True

def reg_blk_val(board,r,c,val):
	base_r = r//3*3
	base_c = c//3*3
	for test_r in range(base_r,base_r+3):
		for test_c in range(base_c,base_c+3):
			if board[test_r][test_c]==val:
				return False
	return True

def determine_boards_or_invalid(r,c):
	if not is_valid(r,c):
		return [NONE]
	ret = []
	if c < 9 and r < 9:
		ret.append(TOP_LEFT)
	if c > 11 and r < 9:
		ret.append(TOP_RIGHT)
	if c > 11 and r > 11:
		ret.append(BOT_RIGHT)
	if c < 9 and r > 11:
		ret.append(BOT_LEFT) 
	if c > 5 and c < 15 and r > 5 and r < 15:
		ret.append(MIDDLE)
	return ret

def get_board(board,b_index):
	if b_index==TOP_LEFT:
		return get_top_left(board)
	elif b_index==TOP_RIGHT:
		return get_top_right(board)
	elif b_index==BOT_LEFT:
		return get_bot_left(board)
	elif b_index==BOT_RIGHT:
		return get_bot_right(board)
	elif b_index==MIDDLE:
		return get_middle(board)
	else:
		return null;

def get_top_left(board): 
	ret = [[c for c in r[:9]] for r in board[:9]]
	return ret

def get_top_right(board): 
	ret = [[c for c in r[12:]] for r in board[:9]]
	return ret

def get_bot_right(board): 
	ret = [[c for c in r[12:]] for r in board[12:]]
	return ret

def get_bot_left(board): 
	ret = [[c for c in r[:9]] for r in board[12:]]
	return ret

def get_middle(board):
	ret = [[c for c in r[6:15]] for r in board[6:15]]
	return ret

def validate(board):
	return True