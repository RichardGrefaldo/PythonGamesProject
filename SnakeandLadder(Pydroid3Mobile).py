import tkinter as tk
from tkinter import Menu
from tkinter import messagebox
import random
root = tk.Tk()
root.geometry('420x610')
root.title('Snake&Ladders')
about = Menu(root)
root.config(menu=about)
help_menu = Menu(about,tearoff = 0)
about.add_cascade(label="Info",menu=help_menu)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About","Snake&Ladders by Richard Grefaldo\nVersion 20240122"))
help_menu.add_command(label="Changelog", command=lambda: messagebox.showinfo("Changelog","Version 20240122\n -Added Animation\n -Dice is now clickable for Reset\nVersion 20240121\n -Added Game Logic\n- Added Two-Player Mode\n -Added dice \nVersion 20240120\n -Initial Release\n -UI only"))
label1 = tk.Label(root,text="Snake and Ladders",font=('Arial',20))
label1.place(x=80,y=50)
label2 = tk.Label(root, text="by Richard",font=('Arial',15))
label2.place(x=320,y=200)
position, position2, counter , p1range,p2range = 1, 1, 0,0,0
ladders = {3:27,38:74,29:98}
snake = {20:6,96:68,51:24}
def start():
    global position, position2,distance,dice
    position = 1 + position - position
    position2 = 1 + position2 - position2
    label1.place_forget()
    label2.place_forget()
    startbutton.place_forget()
    tiles = []
    for i in range(1,100):
        tile = tk.Button(root, bg="white", text=i, height=2, width=1, font=('Arial', 5))
        tile.grid(row=10 - (i - 1) // 9, column=(8 - (i - 1) % 9) if (10 <= i < 19 or 28 <= i < 37 or 46 <= i < 55 or 64 <= i < 73 or 82 <= i < 91) else (i - 1) % 9)
        tiles.append(tile)
    t1, t2, t3, t4, t5, t6, t7, t8, t9 = tiles[0], tiles[1], tiles[2], tiles[3], tiles[4], tiles[5], tiles[6], tiles[7],tiles[8]
    t10, t11, t12, t13, t14, t15, t16, t17, t18 = tiles[9], tiles[10], tiles[11], tiles[12], tiles[13], tiles[14],tiles[15], tiles[16], tiles[17]
    t19, t20, t21, t22, t23, t24, t25, t26, t27 = tiles[18], tiles[19], tiles[20], tiles[21], tiles[22], tiles[23],tiles[24], tiles[25], tiles[26]
    t28, t29, t30, t31, t32, t33, t34, t35, t36 = tiles[27], tiles[28], tiles[29], tiles[30], tiles[31], tiles[32],tiles[33], tiles[34], tiles[35]
    t37, t38, t39, t40, t41, t42, t43, t44, t45 = tiles[36], tiles[37], tiles[38], tiles[39], tiles[40], tiles[41],tiles[42], tiles[43], tiles[44],
    t29, t38, t51, t68, t96, t99 = tiles[28], tiles[37], tiles[50], tiles[67], tiles[95], tiles[98]
    t27, t28, t45, t46, t64 = tiles[26], tiles[27], tiles[44], tiles[45], tiles[63]
    t29, t44, t47, t65 = tiles[28], tiles[43], tiles[46], tiles[64]
    t30, t43, t48, t49, t66, t84 = tiles[29], tiles[42], tiles[47], tiles[48], tiles[65], tiles[83]
    t42, t49, t67, t78, t85 = tiles[41], tiles[48], tiles[66], tiles[77], tiles[84]
    t32, t41, t50, t68, t86 = tiles[31], tiles[40], tiles[49], tiles[67], tiles[85]
    t22, t40, t69 = tiles[21], tiles[39], tiles[68]
    t46, t47, t48, t49, t50, t51, t52, t53, t54 = tiles[45], tiles[46], tiles[47], tiles[48], tiles[49], tiles[50],tiles[51], tiles[52], tiles[53],
    t55, t56, t57, t58, t59, t60, t61, t62, t63 = tiles[54], tiles[55], tiles[56], tiles[57], tiles[58], tiles[59],tiles[60], tiles[61], tiles[62],
    t64, t65, t66, t67, t68, t69, t70, t71, t72 = tiles[63], tiles[64], tiles[65], tiles[66], tiles[67], tiles[68],tiles[69], tiles[70], tiles[71]
    t73, t74, t75, t76, t77, t78, t79, t80, t81 = tiles[72], tiles[73], tiles[74], tiles[75], tiles[76], tiles[77],tiles[78], tiles[79], tiles[80]
    t82, t83, t84, t87, t88, t89, t90 = tiles[81], tiles[82], tiles[83], tiles[86], tiles[87], tiles[88], tiles[89]
    t91, t92, t93, t94, t95, t96, t97, t98, t99 = tiles[90], tiles[91], tiles[92], tiles[93], tiles[94], tiles[95],tiles[96], tiles[97], tiles[98]
    t3.config(text="CAKE")
    t27.config(text="CAKE")
    t29.config(text="Motmot")
    t99.config(text="Motmot")
    t38.config(text="Ladder2")
    t74.config(text="Ladder2")
    t6.config(text="Snake1")
    t20.config(text="Snake1")
    t24.config(text="Snake2")
    t51.config(text="Snake2")
    t68.config(text="Snake3")
    t96.config(text="Snake3")
    def win():
        global dicebutton,rollbutton
        for i, tile in enumerate(tiles):
            row = 10 - (i - 1) // 10
            if 11 <= i < 21 or 31 <= i < 41 or 51 <= i < 61 or 71 <= i < 81:
                col = 9 - (i - 1) % 10
            else:
                col = (i - 1) % 10
            tile.config(text="",bg="white")
        ###### Animation Starts here#######
        def duck1():
            for tile in [t94, t95]:
                tile.config(bg="yellow")

        def duck2():
            for tile in [t85, t86,t87,t88]:
                tile.config(bg="yellow")
        def duck3():
            for tile in [t74, t75,t76,t77,t78,t79]:
                tile.config(bg="yellow")
        def duck4():
            for tile in [t71, t69,t68,t66]:
                tile.config(bg="yellow")
            for tile in [t70, t67]:
                tile.config(bg="black")
        def duck5():
            for tile in [t56, t57,t58,t59,t60,t61]:
                tile.config(bg="yellow")
        def duck6():
            for tile in [t49,t52]:
                tile.config(bg="yellow")
            for tile in [t50, t51]:
                tile.config(bg="brown")
        def duck7():
            for tile in [t38,t39,t42,t43]:
                tile.config(bg="yellow")
            for tile in [t40, t41]:
                tile.config(bg="salmon")

        def duck8():
            for tile in [t29, t30, t31, t32,t33,t34,t35,t36]:
                tile.config(bg="yellow")
        def duck9():
            for tile in [t19, t20, t21, t22,t23,t24,t25,t26]:
                tile.config(bg="yellow")
        def duck10():
            for tile in [t12, t13, t14, t15,t16,t17]:
                tile.config(bg="yellow")
        def duck11():
            for tile in [t3,t6]:
                tile.config(bg="brown")
        def curtain1():
            for tile in [t1,t2, t3, t4,t5, t6,t7,t8,t9,t91,t92,t93,t94,t95,t96,t97,t98,t99]:
                tile.config(bg="black")
        def curtain2():
            for tile in [t10,t11, t12, t13,t14, t15,t16,t17,t18,t82,t83,t84,t85,t86,t87,t88,t89,t90]:
                tile.config(bg="black")
        def curtain3():
            for tile in [t19,t20, t21, t22,t23, t24,t25,t26,t27,t73,t74,t75,t76,t77,t78,t79,t80,t81]:
                tile.config(bg="black")
        def curtain4():
            for tile in [t28,t29, t30, t31,t32, t33,t34,t35,t36,t64,t65,t66,t67,t68,t69,t70,t71,t72]:
                tile.config(bg="black")
        def curtain5():
            for tile in [t37,t38, t39, t40,t41, t42,t43,t44,t45,t55,t56,t57,t58,t59,t60,t61,t62,t63]:
                tile.config(bg="black")
        def curtain6():
            for tile in [t46,t47, t48, t49,t50,t51,t52,t53,t54]:
                tile.config(bg="black")

        def fr1():
            for tile in [t27, t28, t45, t46, t63, t64, t81]:
                tile.config(bg="lightgreen")
        def fr2():
            for tile in [t27,t28, t45, t63,t64, t81]:
                tile.config(bg="black")
            for tile in [t26,t29, t44,t46, t47, t62, t65, t80]:
                tile.config(bg="lightgreen")
        def fr3():

            for tile in [t27,t28, t45, t46,t63, t64, t81]:
                tile.config(bg="lightgreen")
            for tile in [t26,t29, t44,t62, t65, t80]:
                tile.config(bg="black")
            for tile in [t25,t30,t43,t47,t48,t61,t66,t79]:
                tile.config(bg="lightgreen")
        def fr4():
            for tile in [t27,t28, t45, t46,t61, t63, t64, t81]:
                tile.config(bg="black")
            for tile in [t26,t29, t44, t47,t48, t62, t65, t80]:
                tile.config(bg="lightgreen")
            for tile in [t25,t30, t43, t66, t79]:
                tile.config(bg="black")
            for tile in [t24,t31,t42,t49,t60,t67,t78]:
                tile.config(bg="lightgreen")
        def fr5():
            for tile in [t27,t28, t45,t49, t46, t63, t64, t81]:
                tile.config(bg="lightgreen")
            for tile in [t26,t29, t44,t60, t47, t62, t65, t80]:
                tile.config(bg="black")
            for tile in [t25,t30, t43, t48, t61, t66, t79]:
                tile.config(bg="lightgreen")
            for tile in [t24,t31, t42, t67, t78]:
                tile.config(bg="black")
            for tile in [t23,t32,t41,t50,t59,t68,t77]:
                tile.config(bg="lightgreen")
        def fr6():
            for tile in [t28,t45,t63,t64]:
                tile.config(bg="black")
            for tile in [t27,t81]:
                tile.config(bg="lightgreen")
            for tile in [t26,t29, t44,t60, t47, t62, t65, t80]:
                tile.config(bg="lightgreen")
            for tile in [t25,t30, t43, t48, t61, t66, t79]:
                tile.config(bg="black")
            for tile in [t24,t31, t42,t60, t67, t78]:
                tile.config(bg="lightgreen")
            for tile in [t23,t32,t41,t59, t68, t77]:
                tile.config(bg="black")
            for tile in [t22, t33, t40,t50, t51, t58, t69, t76]:
                tile.config(bg="lightgreen")
        def fr7():
            for tile in [t28,t45,t63,t64]:
                tile.config(bg="black")
            for tile in [t27,t81]:
                tile.config(bg="lightgreen")
            for tile in [t44,t29,t65,t62]:
                tile.config(bg="black")
            for tile in [t26,t27, t46,t47, t80,t81]:
                tile.config(bg="lightgreen")
            for tile in [t25,t30, t43, t48, t61, t66, t79]:
                tile.config(bg="lightgreen")
            for tile in [t24,t31, t42,t49,t60, t67, t78]:
                tile.config(bg="black")
            for tile in [t77,t68,t59,t50,t41,t32,t23]:
                tile.config(bg="lightgreen")
            for tile in [t22,t33,t40,t58,t69,t76]:
                tile.config(bg="black")
            for tile in [t21,t34,t39,t52,t57,t70,t75]:
                tile.config(bg="lightgreen")
        def fr8():
            for tile in [t44, t29, t65, t62]:
                tile.config(bg="black")
            for tile in [t26, t47, t80]:
                tile.config(bg="lightgreen")
            for tile in [t64,t63,t28,t45]:
                tile.config(bg="lightgreen")
            for tile in [t43, t30,t46, t61, t66,t81,t27]:
                tile.config(bg="black")
            for tile in [t24, t31, t42, t49, t60, t67, t78]:
                tile.config(bg="lightgreen")
            for tile in [t77, t68, t59, t50, t41, t32, t23]:
                tile.config(bg="black")
            for tile in [t22, t33, t40, t58, t69, t76]:
                tile.config(bg="lightgreen")
            for tile in [t21, t34, t39, t57, t70, t75]:
                tile.config(bg="black")
            for tile in [t20, t35, t38, t53, t56, t71, t74]:
                tile.config(bg="lightgreen")
        def fr9():
            for tile in [t42,t26,t80, t31, t60,t67,t64,t63,t45,t47,t28]:
                tile.config(bg="black")

            for tile in [t79, t44,t29,t65,t62,t48, t25]:
                tile.config(bg="lightgreen")
            for tile in [t24, t49, t78]:
                tile.config(bg="lightgreen")
            for tile in [t77, t68, t59, t50, t41, t32, t23]:
                tile.config(bg="lightgreen")
            for tile in [t22, t33, t40, t51,t58, t69, t76]:
                tile.config(bg="black")
            for tile in [t21, t34, t39, t57, t70, t75]:
                tile.config(bg="lightgreen")
            for tile in [t20, t35, t38, t56, t71, t74]:
                tile.config(bg="black")
            for tile in [t73, t72, t55, t54, t37, t36, t19]:
                tile.config(bg="lightgreen")

        def fr10():
            for tile in [t81, t64, t63,t46 ,t45,t28,t27]:
                tile.config(bg="lightgreen")
            for tile in [ t43, t30, t61,t50 ,t66]:
                tile.config(bg="lightgreen")
            for tile in [ t68, t59, t41,t48, t32,t65,t62,t44,t29]:
                tile.config(bg="black")
            for tile in [t22, t33, t40, t51, t58, t69, t76]:
                tile.config(bg="lightgreen")
            for tile in [t21, t34, t39,t52, t57, t70, t75]:
                tile.config(bg="black")
            for tile in [t20, t35, t38, t56, t71,t79,t25 ,t74]:
                tile.config(bg="lightgreen")
            for tile in [t73, t72, t55,t37, t36,t25,t79, t19]:
                tile.config(bg="black")
        def fr11():

            for tile in [ t28, t45, t46,t63, t64]:
                tile.config(bg="black")
            for tile in [t80, t65, t62, t47, t44, t29, t26]:
                tile.config(bg="lightgreen")
            for tile in [t24,t30,t33, t40,t43,t49, t58,t61,t66,t69,t78]:
                tile.config(bg="black")
            for tile in [t75, t70,t67,t60, t57, t52,t42,t31, t39,t34,t21]:
                tile.config(bg="lightgreen")
            for tile in [t74, t71, t56,t53, t38,t35,t20]:
                tile.config(bg="black")
            for tile in [t19, t36, t37, t55, t72, t73]:
                tile.config(bg="lightgreen")
        def fr12():
            for tile in [t79, t66, t61,t48,t43,t30, t25,t59,t68,t71,t74]:
                tile.config(bg="lightgreen")
            for tile in [t23,t39, t34,t42,t31,t65,t62,t47,t44,t29, t57,t67,t60,t77,t70]:
                tile.config(bg="black")
            for tile in [t20, t35, t38,t41,t32,t53, t56,t59,t68,t71,t74]:
                tile.config(bg="lightgreen")
            for tile in [t19, t36, t37,t54,t50, t55, t72, t73]:
                tile.config(bg="black")
        def fr13():
            for tile in [t78, t67, t60,t49,t42,t45,t28,t31,t46,t64,t63, t24]:
                tile.config(bg="lightgreen")
            for tile in [t23,t39, t34,t65,t81,t27,t62,t47,t44,t29, t57,t77,t70]:
                tile.config(bg="black")
            for tile in [t35, t38,t41,t32,t51,t50,t66,t61,t48,t43,t30, t56,t59,t68,t71,t76,t22,]:
                tile.config(bg="black")
            for tile in [t19, t36,t40,t33, t37,t54,t67, t69,t58,t55, t72, t73]:
                tile.config(bg="lightgreen")
        def fr14():
            for tile in [t23,t32,t41,t50,t59,t68,t77]:
                tile.config(bg="lightgreen")
            for tile in [t31,t42,t49,t60,t67]:
                tile.config(bg="black")
            for tile in [t23,t32,t41,t50,t59,t68,t77,t78,t79,t24,t25]:
                tile.config(bg="lightgreen")
            for tile in [t74,t53,t65,t62,t47,t29,t44,t20,t39,t34,t57,t70]:
                tile.config(bg="lightgreen")
            for tile in [t36,t37,t55,t72,t21,t64,t63,t46,t45,t28,t75,t80,t26,t52,t69,t58,t40,t33]:
                tile.config(bg="black")
        def fr15():

            for tile in [t66,t35,t38,t71,t56,t61,t48,t43,t30,t76,t69,t58,t51,t40,t33,t22]:
                tile.config(bg="lightgreen")
            for tile in [t74,t53,t20,t39,t79,t34,t25,t57,t70,t68,t59,t50,t41,t32,t65,t62,t47,t44,t29]:
                tile.config(bg="black")
        def fr16():
            for tile in [t72,t55,t37,t36,t21,t34,t39,t52,t57,t70,t75,t67,t60,t49,t42,t31]:
                tile.config(bg="lightgreen")
            for tile in [t73,t54,t19,t35,t38,t56,t71,t69,t58,t51,t40,t33,t66,t61,t48,t43,t30,t78,t24]:
                tile.config(bg="black")
        def fr17():
            for tile in [t74,t71,t56,t53,t38,t35,t20,t32,t41,t50,t59,t68]:
                tile.config(bg="lightgreen")
            for tile in [t72,t55,t37,t36,t34,t39,t52,t57,t70,t67,t60,t49,t42,t31,t45,t23,t77]:
                tile.config(bg="black")
        def fr18():
            for tile in [t73,t72,t55,t54,t37,t36,t19,t33,t40,t51,t58,t69,]:
                tile.config(bg="lightgreen")
            for tile in [t35,t38,t53,t56,t71,t68,t59,t50,t41,t32,t22,t28,t76]:
                tile.config(bg="black")
        def fr19():
            for tile in [t70,t57,t52,t39,t34]:
                tile.config(bg="lightgreen")
            for tile in [t36,t37,t54,t55,t72,t69,t58,t51,t40,t33,t21,t75,t29]:
                tile.config(bg="black")
        def fr20():
            for tile in [t71,t56,t53,t38,t35]:
                tile.config(bg="lightgreen")
            for tile in [t70,t57,t52,t39,t34,t20,t74]:
                tile.config(bg="black")
        def fr21():
            for tile in [t72,t55,t54,t37,t36]:
                tile.config(bg="lightgreen")
            for tile in [t73,t19,t53,t71,t56,t38,t35]:
                tile.config(bg="black")
        def fr22():
            for tile in [t72,t55,t54,t37,t53,t36]:
                tile.config(bg="black")
        def jh1():
            for tile in [t28, t27]:
                tile.config(bg="pink")

        def jh2():
            for tile in [t26, t29]:
                tile.config(bg="pink")
            for tile in [t28]:
                tile.config(bg="black")
        def jh3():
            for tile in [t30, t25]:
                tile.config(bg="pink")
            for tile in [t29]:
                tile.config(bg="black")
        def jh4():
            for tile in [t31, t24,t28,t45,t46,t63,t64,t81]:
                tile.config(bg="pink")
            for tile in [t30]:
                tile.config(bg="black")
        def jh5():
            for tile in [t31,t27,t28,t45,t46,t63,t64,t81]:
                tile.config(bg="black")
            for tile in [t32,t23,t29,t44,t47,t62,t65,t80]:
                tile.config(bg="pink")
        def jh6():
            for tile in [t33,t22,t27,t28,t45,t46,t63,t64,t81,t79,t66,t61,t48,t43,t30]:
                tile.config(bg="pink")
            for tile in [t32,t26,t29,t44,t47,t62,t65,t80]:
                tile.config(bg="black")
        def jh7():
            for tile in [t34,t21,t78,t67,t60,t49,t42,t31,t80,t65,t62,t47,t44,t29,t26]:
                tile.config(bg="pink")
            for tile in [t33,t79,t66,t61,t48,t43,t30,t25,t81,t64,t63,t45,t28,t27]:
                tile.config(bg="black")
        def jh8():
            for tile in [t77,t68,t59,t50,t41,t32,t35,t20,t79,t66,t61,t48,t43,t30,t25]:
                tile.config(bg="pink")
            for tile in [t34,t24,t78,t67,t60,t49,t42,t31,t80,t65,t62,t44,t29,t26]:
                tile.config(bg="black")
        def jh9():
            for tile in [t36,t19,t76,t69,t58,t51,t40,t33,t78,t67,t60,t49,t42,t31,t24,t81,t64,t63,t45,t28,t27]:
                tile.config(bg="pink")
            for tile in [t35,t77,t68,t59,t50,t41,t32,t23,t79,t66,t61,t43,t30,t25]:
                tile.config(bg="black")
        def jh10():
            for tile in [t75,t70,t57,t52,t39,t34,t77,t68,t59,t50,t41,t32,t23,t80,t65,t62,t44,t29,t26]:
                tile.config(bg="pink")
            for tile in [t36,t76,t69,t58,t51,t40,t33,t22,t78,t67,t60,t42,t31,t24,t81,t64,t63,t46,t45,t28,t27]:
                tile.config(bg="black")
        def jh11():
            for tile in [t74,t71,t56,t53,t39,t35,t76,t38,t69,t58,t81,t27,t51,t40,t33,t22,t79,t66,t61,t43,t30,t25,t64,t63,t46,t45,t28]:
                tile.config(bg="pink")
            for tile in [t21,t34,t39,t52,t57,t70,t75,t77,t68,t59,t41,t32,t23,t26,t29,t44,t47,t62,t65,t80,]:
                tile.config(bg="black")
        def jh12():
            for tile in [t73,t72,t55,t54,t37,t36,t19,t75,t70,t57,t52,t39,t34,t21,t78,t67,t60,t42,t31,t24,t29,t44,t47,t62,t65,t81,t27,t80,t26]:
                tile.config(bg="pink")
            for tile in [t74,t71,t56,t53,t38,t35,t20,t76,t69,t58,t40,t33,t22,t79,t66,t61,t48,t43,t30,t25,t64,t63,t46,t45,t28]:
                tile.config(bg="black")
        def jh13():
            for tile in [t73,t72,t55,t54,t37,t36,t19,t75,t70,t57,t39,t34,t21,t49,t42,t31,t24,t65,t62,t47,t44,t29,t78,t67,t60]:
                tile.config(bg="black")
            for tile in [t74,t79,t25,t71,t56,t53,t23,t38,t35,t20,t77,t68,t59,t41,t32,t66,t61,t48,t43,t30,t26,t80]:
                tile.config(bg="pink")
        def jh14():
            for tile in [t74,t71,t56,t38,t35,t20,t77,t68,t59,t50,t41,t32,t23,t66,t61,t48,t43,t30,t81,t27]:
                tile.config(bg="black")
            for tile in [t73,t24,t27,t78,t81,t72,t55,t54,t37,t36,t19,t76,t69,t58,t40,t33,t22,t67,t60,t49,t42,t31,t25,t79,t64,t63,t46,t45,t28]:
                tile.config(bg="pink")
        def jh15():
            for tile in [t73,t72,t55,t37,t36,t19,t76,t69,t58,t51,t40,t33,t22,t67,t60,t49,t42,t31,t27,t81,t28,t45,t46,t63,t64]:
                tile.config(bg="black")
            for tile in [t75, t70, t57, t39, t34, t21, t77, t68, t59, t50, t41, t32, t23, t65, t62, t47, t44, t29]:
                tile.config(bg="pink")
        def jh16():
            for tile in [t75,t70,t57,t52,t39,t34,t21,t80,t65,t62,t47,t44,t29,t26,t59,t50,t41,t32,t68]:
                tile.config(bg="black")
            for tile in [t74,t71,t56,t38,t35,t20,t22,t33,t40,t51,t58,t69,t76,t66,t61,t48,t43,t30,t81,t64,t63,t46,t45,t28,t27]:
                tile.config(bg="pink")
        def jh17():
            for tile in [t71,t74,t56,t53,t38,t35,t20,t69,t58,t51,t40,t33,t30,t25,t43,t48,t61,t66,t79,t64,t63,t45,t28]:
                tile.config(bg="black")
            for tile in [t55,t72,t73,t37,t36,t19,t21,t34,t39,t52,t57,t70,t75,t67,t60,t49,t42,t31,t80,t65,t62,t47,t44,t29,t26]:
                tile.config(bg="pink")

        def jh18():
            for tile in [t73,t72,t55,t54,t37,t36,t19,t70,t57,t52,t39,t34,t78,t67,t60,t49,t42,t31,t24,t65,t62,t44,t29]:
                tile.config(bg="black")
            for tile in [t74,t71,t56,t53,t38,t35,t20,t68,t59,t50,t41,t32,t79,t66,t61,t48,t43,t30,t25]:
                tile.config(bg="pink")
        def jh19():
            for tile in [t71,t56,t53,t38,t35,t68,t59,t50,t41,t32,t30,t43,t61,t66,t81,t46,t27,t23,t77]:
                tile.config(bg="black")
            for tile in [t72,t73,t55,t54,t37,t36,t19,t69,t58,t40,t33,t51,t78,t67,t60,t49,t42,t31,t24]:
                tile.config(bg="pink")
        def jh20():
            for tile in [t76,t69,t58,t51,t40,t33,t22,t67,t60,t42,t31,t72,t55,t54,t37,t36,t47,t80,t26]:
                tile.config(bg="black")
            for tile in [t70,t57,t39,t34,t32,t23,t41,t52,t59,t50,t68,t77,t81,t64,t63,t46,t27,t45,t28]:
                tile.config(bg="pink")
        def jh21():
            for tile in [t75,t70,t57,t52,t39,t34,t21,t79,t48,t25,t68,t59,t41,t32,t64,t63,t45,t28]:
                tile.config(bg="black")
            for tile in [t71,t56,t53,t38,t35,t22,t33,t40,t51,t58,t69,t76,t80,t65,t62,t47,t44,t29,t26]:
                tile.config(bg="pink")
        def jh22():
            for tile in [t35,t56,t71,t74,t38,t20,t69,t58,t40,t33,t44,t29,t62,t53,t65,t78,t49,t24]:
                tile.config(bg="black")
            for tile in [t36,t37,t54,t55,t72,t75,t70,t57,t52,t39,t34,t21,t79,t66,t61,t48,t43,t30,t25]:
                tile.config(bg="pink")
        def jh23():
            for tile in [t73,t72,t55,t54,t37,t36,t19,t77,t50,t23,t70,t57,t39,t34,t43,t30,t61,t66,t81,t27,t46]:
                tile.config(bg="black")
            for tile in [t74,t71,t56,t53,t38,t35,t20,t24,t31,t42,t49,t60,t67,t78,t64,t63,t28,t45]:
                tile.config(bg="pink")
        def jh24():
            for tile in [t71,t56,t38,t35,t22,t51,t76,t80,t64,t47,t26,t63,t45,t28,t67,t60,t42,t31]:
                tile.config(bg="black")
            for tile in [t72,t74,t55,t54,t37,t36,t19,t77,t68,t59,t50,t41,t73,t32,t23,t65,t62,t44,t29]:
                tile.config(bg="pink")
        def jh25():
            for tile in [t72,t55,t37,t36,t21,t52,t75,t79,t65,t62,t44,t29,t48,t25,t59,t68,t41,t32]:
                tile.config(bg="black")
            for tile in [t22,t33,t40,t51,t58,t69,t76,t81,t64,t63,t66,t61,t43,t30,t46,t45,t28,t27]:
                tile.config(bg="pink")
        def jh26():
            for tile in [t74,t53,t20,t49,t66,t61,t78,t43,t30,t24,t40,t33,t58,t69,t64,t63,t45,t28]:
                tile.config(bg="black")
            for tile in [t70,t75,t52,t39,t34,t21,t57,t67,t60,t42,t31,t80,t26,t65,t62,t47,t44,t29]:
                tile.config(bg="pink")
        def jh27():
            for tile in [t73,t54,t19,t77,t67,t60,t50,t42,t31,t23,t34,t39,t57,t70,t65,t62,t44,t29]:
                tile.config(bg="black")
            for tile in [t74,t71,t56,t53,t38,t35,t20,t32,t41,t59,t68,t79,t66,t61,t48,t43,t30,t25]:
                tile.config(bg="pink")
        def jh28():
            for tile in [t76,t68,t59,t51,t41,t32,t22,t35,t38,t56,t71,t30,t43,t61,t66,t81,t46,t27]:
                tile.config(bg="black")
            for tile in [t72,t55,t73,t54,t37,t36,t19,t40,t33,t58,t69,t78,t67,t60,t49,t42,t31,t24]:
                tile.config(bg="pink")
        def jh29():
            for tile in [t72,t55,t37,t36,t75,t69,t58,t40,t52,t33,t21,t80,t67,t60,t47,t42,t31,t26]:
                tile.config(bg="black")
            for tile in [t70,t57,t39,t34,t41,t32,t23,t50,t59,t68,t77,t81,t64,t63,t46,t45,t28,t27]:
                tile.config(bg="pink")
        def jh30():
            for tile in [t74,t70,t57,t53,t39,t34,t20,t79,t68,t59,t48,t41,t32,t25,t81,t64,t63,t46,t45,t28]:
                tile.config(bg="black")
            for tile in [t71,t56,t38,t35,t33,t22,t40,t51,t58,t69,t76,t80,t65,t62,t47,t44,t29,t26]:
                tile.config(bg="pink")
        def jh31():
            for tile in [t73,t71,t56,t54,t38,t35,t19,t78,t69,t58,t49,t40,t33,t24,t80,t65,t62,t47,t44,t29]:
                tile.config(bg="black")
            for tile in [t72,t55,t37,t36,t25,t21,t34,t39,t52,t57,t70,t75,t79,t66,t61,t48,t43,t30]:
                tile.config(bg="pink")
        def jh32():
            for tile in [t72,t55,t37,t36,t77,t70,t57,t50,t39,t34,t23,t79,t66,t61,t48,t43,t30,t27]:
                tile.config(bg="black")
            for tile in [t74,t71,t56,t53,t38,t35,t20,t78,t67,t60,t49,t42,t31,t24]:
                tile.config(bg="pink")
        def jh33():
            for tile in [t76,t71,t56,t51,t35,t38,t35,t22,t78,t67,t60,t49,t42,t31,t26]:
                tile.config(bg="black")
            for tile in [t72,t73,t55,t54,t37,t36,t19,t77,t68,t59,t50,t41,t32,t23,t81,t64,t63,t46]:
                tile.config(bg="pink")
        def jh34():
            for tile in [t75,t72,t55,t52,t37,t36,t21,t77,t68,t59,t50,t41,t32,t25,t81,t64,t63]:
                tile.config(bg="black")
            for tile in [t76,t69,t58,t51,t40,t33,t22,t80,t65,t62,t47,t45,t28,t27]:
                tile.config(bg="pink")
        def jh35():
            for tile in [t74,t53,t20,t76,t51,t69,t58,t55,t40,t33,t24,t80,t65,t62,t45,t28,t27]:
                tile.config(bg="black")
            for tile in [t75,t70,t57,t52,t39,t34,t21,t79,t66,t61,t48,t44,t29,t26,t81,t64,t63]:
                tile.config(bg="pink")
        def jh36():
            for tile in [t73,t54,t19,t75,t70,t57,t52,t39,t34,t23,t79,t66,t61,t81,t64,t63,t46,t44,t26,t29]:
                tile.config(bg="black")
            for tile in [t74,t71,t56,t53,t38,t35,t20,t78,t67,t60,t49,t43,t30,t25,t62,t65,t80]:
                tile.config(bg="pink")
        def jh37():
            for tile in [t74,t71,t56,t53,t38,t35,t22,t78,t67,t60,t47,t62,t65,t80,t43,t30,t25]:
                tile.config(bg="black")
            for tile in [t73,t72,t55,t54,t37,t36,t19,t77,t68,t59,t50,t42,t31,t24,t79,t66,t61,t81,t64,t63,t46,t45,t28,t27]:
                tile.config(bg="pink")
        def jh38():
            for tile in [t73,t72,t55,t54,t37,t36,t21,t77,t68,t59,t42,t31,t81,t24,t48,t61,t66,t79,t27,t28,t45,t46]:
                tile.config(bg="black")
            for tile in [t76,t69,t58,t51,t41,t32,t23,t80,t65,t62,t47,t44,t29,t26,t60,t67,t78]:
                tile.config(bg="pink")
        def jh39():
            for tile in [t20,t76,t69,t58,t41,t32,t80,t23,t26,t29,t44,t47,t81,t64,t49,t60,t67,t78,]:
                tile.config(bg="black")
            for tile in [t75,t70,t57,t52,t40,t33,t46,t45,t22,t77,t68,t59,t79,t66,t61,t48,t43,t30,t25]:
                tile.config(bg="pink")
        def jh40():
            for tile in [t19,t75,t70,t57,t40,t50,t33,t22,t77,t68,t59,t25,t30,t43,t46,t63,t29,t48,t79,t80,t65]:
                tile.config(bg="black")
            for tile in [t74,t71,t56,t53,t39,t34,t21,t58,t69,t76,t78,t45,t28,t67,t60,t49,t42,t47,t44,t31,t24]:
                tile.config(bg="pink")
        def jh41():
            for tile in [t74,t71,t56,t39,t34,t21,t76,t69,t58,t51,t78,t66,t62,t47,t49,t42,t31,t24]:
                tile.config(bg="black")
            for tile in [t73,t72,t55,t54,t38,t64,t81,t27,t46,t48,t43,t29,t63,t35,t20,t75,t70,t57,t77,t68,t59,t50,t41,t32,t23]:
                tile.config(bg="pink")
        def jh42():
            for tile in [t73,t72,t55,t38,t35,t20,t75,t70,t57,t52,t77,t67,t61,t48,t23,t32,t41,t50,t81,t64,t63,t46,t45,t28,t27]:
                tile.config(bg="black")
            for tile in [t74,t71,t56,t37,t36,t19,t76,t69,t58,t51,t40,t33,t22,t49,t42,t30,t26,t47,t62,t65,t80]:
                tile.config(bg="pink")
        def jh43():
            for tile in [t53,t56,t71,t74,t76,t37,t36,t19,t22,t33,t40,t51,t68,t60,t49,t26,t29,t44,t47,t62,t65,t80]:
                tile.config(bg="black")
            for tile in [t55,t72,t73,t75,t70,t57,t52,t39,t34,t21,t50,t41,t31,t25,t48,t61,t66,t79]:
                tile.config(bg="pink")
        def jh44():
            for tile in [t73,t72,t55,t54,t75,t69,t59,t50,t52,t39,t34,t21,t25,t30,t43,t48,t61,t66,t79]:
                tile.config(bg="black")
            for tile in [t74,t71,t56,t53,t38,t35,t20,t51,t40,t32,t24,t49,t60,t67,t78]:
                tile.config(bg="pink")
        def jh45():
            for tile in [t35,t53,t38,t20,t74,t70,t58,t51,t78,t67,t60,t49,t42,t31,t24]:
                tile.config(bg="black")
            for tile in [t73,t72,t55,t54,t37,t36,t19,t52,t39,t33,t23,t50,t59,t68,t77]:
                tile.config(bg="pink")
        def jh46():
            for tile in [t73,t71,t57,t52,t54,t37,t36,t19,t23,t32,t41,t50,t59,t68,t77]:
                tile.config(bg="black")
            for tile in [t53,t38,t34,t22,t51,t58,t69,t76]:
                tile.config(bg="pink")
        def jh47():
            for tile in [t72,t56,t53,t33,t22,t40,t58,t69,t76,t51]:
                tile.config(bg="black")
            for tile in [t54,t37,t35,t21,t52,t57,t70,t75]:
                tile.config(bg="pink")
        def jh48():
            for tile in [t55,t54,t21,t75,t70,t57,t52,t39,t34]:
                tile.config(bg="black")
            for tile in [t36,t20,t53,t56,t71,t74]:
                tile.config(bg="pink")
        def jh49():
            for tile in [t74,t71,t56,t53,t38,t35,t20]:
                tile.config(bg="black")
            for tile in [t19,t54,t55,t72,t73]:
                tile.config(bg="pink")
        def jh50():
            for tile in [t73,t72,t55,t54,t37,t36,t19]:
                tile.config(bg="black")
        def lab():
            for tile in [t77,t68,t59,t50,t41,t32,t23]:
                tile.config(bg="pink")
        def lab2():
            for tile in [t71,t56,t75,t76,t71,t70,t77,t78,t79,t66,t67,t69,t68,t58,t57,t59,t50,t41,t32,t40,t52,t51,t60,t61,t49,t42,t48,t65,t62]:
                tile.config(bg="red")
            for tile in [t77,t23]:
                tile.config(bg="black")
        def lab3():
            for tile in [t71,t56,t75,t76,t71,t70,t77,t78,t79,t66,t67,t69,t68,t58,t57,t59,t50,t41,t32,t40,t52,t51,t60,t61,t49,t42,t48,t65,t62]:
                tile.config(bg="black")
        def lab4():
            for tile in [t75,t39,t34,t70,t57,t52,t79,t66,t61,t48,t43,t30,t22,t23,t24]:
                tile.config(bg="pink")





        root.after(1000,duck1);root.after(1500,duck2);root.after(2000,duck3);root.after(2500,duck4)
        root.after(3000,duck5);root.after(3500,duck6);root.after(4000, duck7);root.after(4500,duck8)
        root.after(5000,duck9); root.after(5500,duck10);root.after(6000,duck11)
        animation = [curtain1,curtain2,curtain3,curtain4,curtain5,curtain6,fr1,fr2,fr3,fr4,fr5,fr6,fr7,fr8,fr9,fr10,fr11,fr12,fr13,fr14,fr15,fr16,fr17,fr18,fr19,fr20,fr21,fr22,jh1,jh2,jh3,jh4,jh5,jh6,jh7,jh8,jh9,jh10,jh11,jh12,jh13,jh14,jh15,jh16,jh17,jh18,jh19,jh20,jh21,jh22,jh23,jh24,jh25,jh26,jh27,jh28,jh29,jh30,jh31,jh32,jh33,jh34,jh35,jh36,jh37,jh38,jh39,jh40,jh41,jh42,jh43,jh44,jh45,jh46,jh47,jh48,jh49,jh50,lab,lab2,lab3,lab4]
        delay = 6500
        for frame in animation:
            root.after(delay, frame)
            delay += 700
        #Animation Ends Here
    def roll():
        global position, position2, counter,p1range,p2range,dice,dice2,player
        dice = random.randint(1, 6)
        origdice = dice
        counter = counter + 1
        player = counter % 2
        dicebutton = tk.Button(root, text="⬤", command=start)
        dicebutton.place(x=700, y=1200, height=150, width=150)


        def animate1():
            dicebutton.config(text="⬤")

        def animate2():
            dicebutton.config(text="⬤ ⬤\n⬤")

        def animate3():
            dicebutton.config(text="⬤ ⬤ ⬤\n⬤ ⬤ ⬤")

        def animate4():
            dicebutton.config(text="⬤ ⬤\n⬤ ⬤")

        def result():
            diceresult = origdice
            if diceresult == 1:
                dicebutton.config(text="⬤")
            elif diceresult == 2:
                dicebutton.config(text="⬤ ⬤")
            elif diceresult == 3:
                dicebutton.config(text="⬤ ⬤\n⬤")
            elif diceresult == 4:
                dicebutton.config(text="⬤ ⬤\n⬤ ⬤")
            elif diceresult == 5:
                dicebutton.config(text="⬤ ⬤\n⬤\n⬤ ⬤")
            elif diceresult == 6:
                dicebutton.config(text="⬤ ⬤ ⬤\n⬤ ⬤ ⬤")


        root.after(50, animate1)
        root.after(100, animate2)
        root.after(150, animate3)
        root.after(200, animate4)
        root.after(250, result)

        def crawl1():
            global position,position2, p1range,dice,player,distance,fpos1,fpos2
            fpos1 = position + dice
            fpos2 = position2 + dice

            distance = dice


            if player == 1:
                rollbutton.config(bg="blue",text="Blue Turn",state="active")
                if fpos1 in ladders:
                    dice = ladders[fpos1]
                    dice = dice - 1
                elif fpos1 in snake and position in snake:
                    dice = snake[fpos1]
                    dice = dice + 1 - fpos1
                    distance = dice

                if distance > 0:
                    position = position + 1
                    dice = dice - 1
                    root.after(100, crawl1)
                    rollbutton.config(state="disabled")
                    if position > 98:
                        win()
                if distance < 0:
                    position = position - 1
                    dice = dice + 1
                    root.after(100, crawl1)
                    rollbutton.config(state="disabled")

                for i, tile in enumerate(tiles):
                    if position == i + 1:
                        tile.config(bg="red")
                    elif position2 == i + 1:
                        tile.config(bg="blue")
                    else:
                        tile.config(bg="white")

            else:
                rollbutton.config(bg="red", text="Red Turn",state="active")
                if fpos2 in ladders:
                    dice = ladders[fpos2]
                    dice = dice - 1
                elif fpos2 in snake and position2 in snake:
                    dice = snake[fpos2]
                    dice = dice + 1 - fpos2
                    distance = dice

                if distance > 0:
                    position2 = position2 + 1
                    dice = dice - 1
                    root.after(100, crawl1)
                    rollbutton.config(state="disabled")
                    if position2 > 98:
                        win()

                elif distance < 0:
                    position2 = position2 - 1
                    dice = dice + 1
                    root.after(100, crawl1)
                    rollbutton.config(state="disabled")

                for i, tile in enumerate(tiles):
                    if position2 == i + 1:
                        tile.config(bg="blue")
                    elif position == i + 1:
                        tile.config(bg="red")
                    else:
                        tile.config(bg="white")

                distance = dice

        crawl1()

    rollbutton = tk.Button(root, text="Red Turn", bg="red", command=roll)
    rollbutton.place(x=300, y=1200, height=150, width=300)


startbutton = tk.Button(root, text="Start", command=start)
startbutton.place(x=400, y=700, height=150, width=300)
root.mainloop()