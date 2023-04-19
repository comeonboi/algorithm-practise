#!/usr/bin/python
# -*- conding:utf-8 -*-
from tkinter import *
import time
import threading
import random
import math
from tkinter import messagebox

# 变量定义
BIANCHANG = 19
COLOR = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', '#00C5CD', '#00EE76', '#388E8E', '#556B2F', '#6B8E23',
         '#8B2252', '#8B6969', '#A0522D', '#BC8F8F', '#BC8F3F', 'black']
COLUMN = 16
ROW = 30


class fangk:
    def __init__(self, huabu, col, row):
        self.huabu = huabu
        self.col, self.row = col, row
        self.color = COLOR[self.row % 16]
        # self.setvisible(1)
        self.havefk = False

    def setvisible(self, statu):
        if statu > 0:
            x = self.col * (BIANCHANG + 1) + 2
            y = 582 - (ROW - self.row - 1) * (BIANCHANG + 1)
            self.fk = self.huabu.create_rectangle(x, y, x + BIANCHANG, y + BIANCHANG, fill=self.color)
            self.line1 = self.huabu.create_line(x, y, x, y + BIANCHANG, fill='white')
            self.line2 = self.huabu.create_line(x, y, x + BIANCHANG, y, fill='white')
            self.havefk = True
        elif statu == 0 and self.havefk:
            self.huabu.delete(self.fk)
            self.huabu.delete(self.line2)
            self.huabu.delete(self.line1)
            self.havefk = False
        else:
            return -1

    def set_color(self, color):
        self.color = color
        return self


class elsfk:
    def __init__(self):
        self.fk_type = [[(0, 0, 1, 1), (0, 1, 0, 1)],  # 正方形
                        [(0, 0, 0, 0), (1, 0, -1, -2)],  # 长条
                        [(-1, 0, 1, 2), (0, 0, 0, 0)],
                        [(0, 1, 0, -1), (0, 1, 1, 0)],  # 右Z
                        [(0, -1, -1, 0), (0, 1, 0, -1)],
                        [(0, -1, 0, 1), (0, 1, 1, 0)],  # 左Z
                        [(0, 1, 1, 0), (0, 1, 0, -1)],
                        [(0, 0, -1, 1), (0, 1, 0, 0)],  # T型
                        [(0, 0, 0, 1), (0, 1, -1, 0)],
                        [(0, 1, 0, -1), (0, 0, -1, 0)],
                        [(0, 0, -1, 0), (0, 1, 0, -1)],
                        [(0, 1, 1, -1), (0, -1, 0, 0)],  # 左钩
                        [(0, 1, 0, 0), (0, 1, 1, -1)],
                        [(0, -1, -1, 1), (0, 1, 0, 0)],
                        [(0, 0, 0, -1), (0, 1, -1, -1)],
                        [(0, 1, 1, -1), (0, 1, 0, 0)],  # 右钩
                        [(0, -1, 0, 0), (0, 1, 1, -1)],
                        [(0, -1, -1, 1), (0, -1, 0, 0)],
                        [(0, 0, 0, 1), (0, 1, -1, -1)]]

        # 窗口
        self.win = Tk()
        self.win.title("俄罗斯方块")
        # self.win.attributes("-alpha",0.95)
        self.win.geometry('450x610')
        self.win.resizable(0, 0)
        self.nandu_stat=IntVar()
        self.huabu = Canvas(self.win, bg="light grey", height=600, width=COLUMN * (BIANCHANG + 1), takefocus=True)
        self.huabu_right = Canvas(self.win, height=100, width=100)
        self.pauseBut = Button(self.win, text="暂停", bg='light green', height=1, width=12, font=(10), command=self.pause)
        self.pauseBut.place(x=335, y=450)
        self.startBut = Button(self.win, text="开始", height=1, width=12, font=(10), command=self.startgame)
        self.startBut.place(x=335, y=483)
        self.restartBut = Button(self.win, text="重新开始", height=1, width=12, font=(10), command=self.restart)
        self.restartBut.place(x=335, y=516)
        self.quitBut = Button(self.win, text="退出", height=1, width=12, font=(10), command=self.win.quit) #self.quitgame)
        self.quitBut.place(x=335, y=549)
        self.lab_score = Label(self.win, text="分数：0", font=(24))
        self.lab_score.place(x=335, y=50)
        self.lab_grade = Label(self.win, text="等级：1", fg='red', font=(24))
        self.lab_grade.place(x=335, y=70)
        self.check_box1 = Checkbutton(self.win, text="难度", variable=self.nandu_stat, height=1, width=3)
        # 菜单
        self.initgame()
        # self.test = True

        #for i in range(12):
        #    self.base_map[29 - i] = [1] * 15 + [0] * 1
        #self.base_map[28][2] = 0
        #self.base_map[24][5] = 0
        #self.base_map[20][9] = 0
        self.menu = Menu(self.win)
        self.win.config(menu=self.menu)
        self.startMenu = Menu(self.menu)
        self.menu.add_cascade(label='游戏', menu=self.startMenu)
        self.startMenu.add_command(label='开始', command=self.startgame)
        self.startMenu.add_separator()
        self.startMenu.add_command(label='重新开始', command=self.restart)
        self.exitMenu = Menu(self.menu)
        self.menu.add_cascade(label='退出', command=self.quitgame)
        self.setMenu = Menu(self.win)
        self.menu.add_cascade(label='设置', menu=self.setMenu)
        self.setMenu.add_command(label='颜色', command=self.set_color)
        # self.setMenu.add_command(label='难度', command=self.set_nandu)
        # self.helpMenu.add_command(label='How to play', command=self.rule)
        # self.helpMenu.add_separator()
        # self.helpMenu.add_command(label='About...', command=self.about)

        # self.huabu.focus_set()
        self.huabu.bind_all('<KeyPress-a>', self.move_left)
        self.huabu.bind_all('<KeyPress-d>', self.move_right)
        self.huabu.bind_all('<KeyPress-j>', self.rotate)
        # self.huabu.bind_all('<KeyPress-k>', self.change)
        self.huabu.bind_all('<KeyPress-s>', self.quick_drop)
        self.huabu.bind_all('<Left>', self.move_left)
        self.huabu.bind_all('<Right>', self.move_right)
        self.huabu.bind_all('<Up>', self.rotate)
        self.huabu.bind_all('<Down>', self.quick_drop)
        self.huabu.bind_all('<KeyPress-space>', self.down_straight)
        self.huabu.place(x=2, y=2)
        self.huabu_right.place(x=335, y=200)
        self.check_box1.place(x=335,y=100)
        self.fangkuai_map = [[fangk(self.huabu, i, j) for i in range(COLUMN)] for j in range(ROW)]

        # self.startgame()
        self.win.mainloop()

    def set_nandu(self):
        self.nandu_stat = not self.nandu_stat

    def nandu(self):
        if self.nandu_line > 10:
            self.nandu_line = 0
            self.base_map.pop(0)
            self.base_map.append([0] + [1] * 15)  # [random.randrange(0, 2) for i in range(16)])
            self.color_map.pop(0)
            self.color_map.append([random.randrange(0, 17) for i in range(16)])
            self.combind()
            self.draw_map()
            self.win.update()

    def set_color(self):
        self.muti_color = not self.muti_color

    def pause(self):
        messagebox.showinfo("暂停", "游戏暂停中")

    def restart(self):
        messagebox.askquestion("重新开始", "确定要重新开始游戏吗？")
        for i in self.huabu.find_all():
            self.huabu.delete(i)
        self.initgame()
        self.startgame()

    def cal_score(self, row):
        self.score = self.score + [row * 10, int(row * 10 * (1 + row / 10))][self.last_row == row]
        self.lab_score.config(text="分数：" + str(self.score))
        self.last_row = row
        self.sum_row += row
        self.grade = self.sum_row // 50 + 1
        self.lab_grade.config(text="等级：" + str(self.grade))
        if self.nandu_stat:
            self.nandu_line += row
            self.nandu()

    def initgame(self):
        self.map = [[0] * COLUMN for _ in range(ROW)]
        self.map_before = [[0] * COLUMN for _ in range(ROW)]
        self.base_map = [[0] * COLUMN for _ in range(ROW)]
        self.color_map = [[0] * COLUMN for _ in range(ROW)]
        self.score = 0
        self.lock_operation = False
        self.speed = 20
        self.last_row = 0
        self.sum_row = 0
        self.grade = 1
        self.interval = 0
        # self.nandu_stat = True
        self.nandu_line = 0
        self.next_fangk_type = random.randrange(0, 19)
        self.next_color = random.randrange(0, 17)
        self.lab_score.config(text="分数：0")
        self.lab_grade.config(text="等级：1")
        self.muti_color = True  # 设置是否启用多色彩，还未弄

    def quitgame(self):
        q = messagebox.askquestion("退出", "确定要退出吗？")
        if q == 'yes': self.win.destroy(); exit()

    def startgame(self):
        self.check_box1.config(state=DISABLED)
        self.startBut.config(state=DISABLED)
        self.next_fk()
        while not self.lock_operation:
            time.sleep(0.05)
            if self.interval == 0: self.drop()
            self.interval = (self.interval + 1) % (22 - self.grade * 2)
            self.win.update()

    def flash(self, del_rows):
        self.lock_operation = True
        for times in range(6):
            for j in del_rows:
                for i in self.fangkuai_map[j]:
                    i.setvisible(int(0.5 + times % 2 * 0.5))
            self.win.update()
            time.sleep(0.2)
        self.lock_operation = False

    def next_fk(self):
        self.cur_color = self.next_color
        self.cur_fk_type = self.next_fangk_type
        self.next_color = random.randrange(0, 17)
        self.next_fangk_type = random.randrange(0, 19)
        for i in self.huabu_right.find_all():
            self.huabu_right.delete(i)
        for i in range(4):
            fangk(self.huabu_right, 2 + self.fk_type[self.next_fangk_type][0][i],
                  2 - self.fk_type[self.next_fangk_type][1][i]).set_color(COLOR[self.next_color]).setvisible(1)
        self.cur_fk = self.fk_type[self.cur_fk_type]
        self.cur_location = [{'x': 7, 'y': 1}, {'x': 7, 'y': 0}][self.cur_fk_type in (2, 11, 17)]
        self.combind()
        self.draw_map()
        if not self.test_map():
            messagebox.showinfo("失败", "游戏失败了")
            self.lock_operation = True

    def rotate(self, event):
        if not self.lock_operation:
            if self.cur_fk_type != 0:
                temp = self.cur_fk_type
                self.cur_fk_type = [(self.cur_fk_type - 7) // 4 * 4 + self.cur_fk_type % 4 + 7,
                                    (self.cur_fk_type - 1) // 2 * 2 + self.cur_fk_type % 2 + 1][
                    self.cur_fk_type in range(1, 7)]
                self.cur_fk = self.fk_type[self.cur_fk_type]
                if self.cur_location['x'] + min(self.cur_fk[0]) + 1 <= 0 or self.cur_location['x'] + max(
                        self.cur_fk[0]) >= COLUMN or not self.test_map() or self.cur_location['y'] + min(
                    self.cur_fk[1]) + 1 < 0:
                    print('testmap')
                    self.cur_fk_type = temp
                    self.cur_fk = self.fk_type[self.cur_fk_type]
                self.combind()
                self.draw_map()

    def combind(self):
        self.map = [a[:] for a in self.base_map]
        for i in range(len(self.cur_fk[1])):
            x = self.cur_location['x'] + self.cur_fk[0][i]
            y = self.cur_location['y'] - self.cur_fk[1][i]
            self.map[y][x] = 1
            self.color_map[y][x] = self.cur_color

    def test_map(self):
        for i in range(len(self.cur_fk[0])):
            x = self.cur_location['x'] + self.cur_fk[0][i]
            y = self.cur_location['y'] - self.cur_fk[1][i]
            if self.base_map[y][x] > 0: return False
        return True

    def draw_map(self):
        for i in range(ROW):
            for j in range(COLUMN):
                if self.map[i][j] != self.map_before[i][j]:
                    self.fangkuai_map[i][j].set_color(COLOR[self.color_map[i][j]]).setvisible(self.map[i][j])
        self.map_before = [i[:] for i in self.map]
        self.win.update()

    def quick_drop(self, event):
        if not self.lock_operation: self.drop()

    def drop(self):
        self.cur_location['y'] += 1
        if self.cur_location['y'] - min(self.cur_fk[1]) < ROW and self.test_map():
            self.combind()
            self.draw_map()
            return True
        else:
            self.cur_location['y'] -= 1
            self.base_map = [i[:] for i in self.map]
            self.delete_row()
            self.draw_map()
            self.next_fk()
            return False

    def delete_row(self):
        del_row = []
        for i in range(max(self.cur_fk[1]) - min(self.cur_fk[1]) + 1):
            if self.base_map[self.cur_location['y'] - min(self.cur_fk[1]) - i] == [1] * COLUMN:
                del_row.append(self.cur_location['y'] - min(self.cur_fk[1]) - i)
        if not del_row == []:
            self.flash(del_row)
            self.base_map = [r for r in self.base_map if not r == [1] * COLUMN]
            self.base_map = ([[0] * COLUMN] * (30 - len(self.base_map))) + self.base_map
            self.cal_score(len(del_row))

    def move_left(self, event):
        if not self.lock_operation:
            self.cur_location['x'] -= 1
            if self.cur_location['x'] + min(self.cur_fk[0]) + 1 > 0 and self.test_map():
                self.combind()
                self.draw_map()
            else:
                self.cur_location['x'] += 1

    def move_right(self, event):
        if not self.lock_operation:
            self.cur_location['x'] += 1
            if self.cur_location['x'] + max(self.cur_fk[0]) < COLUMN and self.test_map():
                self.combind()
                self.draw_map()
            else:
                self.cur_location['x'] -= 1

    def down_straight(self, event):
        while not self.lock_operation and self.drop(): pass

    # def change(self, event):
    #     self.cur_fk_type = (self.cur_fk_type + 1) % 18
    #     self.cur_fk = self.fk_type[self.cur_fk_type]
    #     self.combind()
    #     self.draw_map()


elsfk()